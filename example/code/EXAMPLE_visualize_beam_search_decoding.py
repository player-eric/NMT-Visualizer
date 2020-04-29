import numpy as np
from nmtvis.BeamSearchVisualizer import visualize_beam_search_decode
with open("../data/beam_source_sentences",'r') as f:
    source=f.read().split('\n')[:-1]

with open("../data/beam_target_sentences",'r') as f:
    target=f.read().split('\n')[:-1]

parent=np.load("../data/parent.npy")
predict=np.load("../data/predict.npy")
probs=np.load("../data/probs.npy")

# print(source)
# print(target)

# print(parent.shape)
# print(predict.shape)
# print(probs.shape)

visualize_beam_search_decode(source,target,predict,parent,probs,5)
