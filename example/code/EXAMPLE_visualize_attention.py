from nmtvis.AttentionVisualizer import visualize_attention
import json

with open("../data/target2source_attention.json", 'r') as f:
    data = json.load(f)

print(type(data))
print(data[0].keys())

visualize_attention(data)
