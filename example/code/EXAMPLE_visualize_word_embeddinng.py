import numpy as np
from nmtvis.EmbeddingVisualizer import visualize_embedding_tsne,visualize_embedding_pca

e=np.load("../data/embeddings.npy").tolist()
v=np.load("../data/vocab.npy").tolist()

visualize_embedding_tsne(e,v,3)
#visualize_embedding_pca(e,v,3)
