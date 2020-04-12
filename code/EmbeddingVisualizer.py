import numpy as np
import os
import shutil
import json
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from .call_html import call_html
from .get_embedding_dependency import get_embedding_dependency

def visualize_embedding_pca(embeddings,vocab,n_dim,n_neighbor=100,copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None):
    '''
    Parameters 'embeddings' should be a list of embedding vectors(with dimensionality >= 3)
    and 'vocab' should be a list consisting words corresponding to the embeddings.
    e.g. embeddings=[[1,0,1],[-1,0,2]],vocab=['man','woman'] 
    In this case, embedding('man')=[1,0,1], embedding('woman')=[-1.0.2]
    
    The reset of the parameters specifies configuration for the PCA process,
    for more details, please refer to https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    
    '''
    if os.path.exists('embeddingvistemp')==True:
        shutil.rmtree('embeddingvistemp')
    if os.path.exists('embeddingvistemp')==False:
        get_embedding_dependency()
    embeddings=np.array(embeddings)
    vocab=np.array(vocab)
    pca=PCA(n_dim,copy,whiten,svd_solver,tol,iterated_power,random_state)
    print("Conducting PCA...")
    pca_result=pca.fit_transform(embeddings)
    get_json(vocab,pca_result,n=n_neighbor)
    os.chdir('embeddingvistemp')
    call_html()

def visualize_embedding_tsne(embeddings,vocab,n_dim,n_neighbor=100,perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, metric='euclidean', init='random', verbose=0, random_state=None, method='barnes_hut', angle=0.5, n_jobs=None):
    '''
    Parameters 'embeddings' should be a list of embedding vectors(with dimensionality >= 3)
    and 'vocab' should be a list consisting words corresponding to the embeddings.
    e.g. embeddings=[[1,0,1],[-1,0,2]],vocab=['man','woman'] 
    In this case, embedding('man')=[1,0,1], embedding('woman')=[-1.0.2]
    
    The reset of the parameters specifies configuration for the TSNE process,
    for more details, please refer to https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
    '''
    if os.path.exists('embeddingvistemp')==True:
        shutil.rmtree('embeddingvistemp')
    if os.path.exists('embeddingvistemp')==False:
        get_embedding_dependency()
    embeddings=np.array(embeddings)
    vocab=np.array(vocab)
    
    pca=PCA(n_components=50)
    after_pca=pca.fit_transform(embeddings)
    print("Conducting TSNE...")
    tsne=TSNE(n_components=n_dim)
    after_tsne=tsne.fit_transform(after_pca)
    after_tsne=after_tsne/100
    get_json(vocab,after_tsne,n=n_neighbor)
    os.chdir('embeddingvistemp')
    call_html()

def calculate_euclidian_distance_matrix(embeddings):
    embeddings=np.array(embeddings)
    result=np.ones([embeddings.shape[0],embeddings.shape[0]])*float("inf")
    for i in range(embeddings.shape[0]):
        for j in range(embeddings.shape[0]):
            if i!=j:
                result[i][j]=np.linalg.norm(embeddings[i]-embeddings[j])
    return result

def calculate_cosine_distance_matrix(embeddings):
    cache_norms=[]
    for i in range(embeddings.shape[0]):
        cache_norms.append(np.linalg.norm(embeddings[i]))
    dotted=np.matmul(embeddings,np.transpose(embeddings))
    num_words=embeddings.shape[0]
    for i in range(num_words):
        for j in range(num_words):
            if i==j:
                dotted[i][j]=float('inf')
            else:
                dotted[i][j]=1-dotted[i][j]/(cache_norms[i]*cache_norms[j])
    return dotted

def sort_distance_matrix(dis_mat):
    sorted_indices=np.argsort(dis_mat,axis=1)
    sorted_result=np.take_along_axis(dis_mat,sorted_indices,axis=1)
    return sorted_indices,sorted_result

def get_json(vocab,embeddings,n=100):
    vocab=np.array(vocab)
    embeddings=np.array(embeddings)
    dis_mat_cos=calculate_cosine_distance_matrix(embeddings)
    sorted_indices_cos,sorted_result_cos=sort_distance_matrix(dis_mat_cos)
    dis_mat_euclidian=calculate_euclidian_distance_matrix(embeddings)
    sorted_indices_euclidian,sorted_result_euclidian=sort_distance_matrix(dis_mat_euclidian)
    result={}
    if embeddings.shape[1]==2:
        embeddings=np.pad(embeddings,((0,0),(0,1)), mode='constant', constant_values=0)
    for i in range(len(vocab)):
        neighbor_list_cos=np.take_along_axis(vocab,sorted_indices_cos[i][0:n],axis=0).tolist()
        neighbor_dis_cos=sorted_result_cos[i][0:n].tolist()
        neighbor_list_euclidian=np.take_along_axis(vocab,sorted_indices_euclidian[i][0:n],axis=0).tolist()
        neighbor_dis_euclidian=sorted_result_euclidian[i][0:n].tolist()
        result[vocab[i]]=[embeddings[i].tolist(),neighbor_list_cos,neighbor_dis_cos,neighbor_list_euclidian,neighbor_dis_euclidian]

    with open('embeddingvistemp/embeddings3d.json','w') as out:
        json.dump(result,out)
