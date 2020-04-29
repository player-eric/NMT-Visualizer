from nmtvis.AttentionVisualizer import visualize_transformer_attention
import json

with open("../data/Transformer_encoder_self_attention.json", 'r') as f:
    encoder_self_attention = json.load(f)

print(type(encoder_self_attention))
#print(encoder_self_attention[0].keys())

with open("../data/Transformer_decoder_self_attention.json", 'r') as f:
    decoder_self_attention = json.load(f)

print(type(decoder_self_attention))
#print(decoder_self_attention[0].keys())

with open("../data/Transformer_decoder_encoder_attention.json", 'r') as f:
    decoder_encoder_attention = json.load(f)

print(type(decoder_encoder_attention))
#print(decoder_encoder_attention[0].keys())

visualize_transformer_attention(
    encoder_self_attention=encoder_self_attention,
    decoder_self_attention=decoder_self_attention,
    decoder_encoder_attention=decoder_encoder_attention)
