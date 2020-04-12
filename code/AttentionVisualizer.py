from .get_dependency import get_dependency
from .process_data import process_data,process_transformer_data
from .call_html import call_html
from typing import List
import os
import shutil

def visualize_attention(data:List[dict]):
    '''
    Parameter 'data' is a list of dictionaries.
    Each dictionary should contain the following keys and corresponding value:
    1.key 'source_sentence': source sentence consist of M tokens
    2.key 'target_sentence': target sentence consist of N tokens
    3.key 'attention_matrix': attention matrix of shape (N,M)
    '''
    if os.path.exists('vistemp')==True:
        shutil.rmtree('vistemp')
    if os.path.exists('vistemp')==False:
        get_dependency(is_transformer=False)
    process_data(data)
    os.chdir('vistemp')
    call_html()


def visualize_transformer_attention(encoder_self_attention:List[dict]=None,decoder_self_attention:List[dict]=None,decoder_encoder_attention:List[dict]=None):
    '''
    Seperately, parameter encoder_self_attention, decoder_self_attention, decoder_encoder_attention are lists of dictionaries.
    
    Dictionary in 'encoder_self_attention' should contain the following keys and corresponding value:
    1.key 'source_sentence': source sentence consist of M tokens
    2.key 'num_layer': the number of layers in the Transformer model
    3.key 'num_head': the number of heads in the Transformer model
    4.key 'layer_x-head_y': the attention matrix of shape(M,M), from head y in layer x

    Dictionary in 'decoder_self_attention' should contain the following keys and corresponding value:
    1.key 'target_sentence': target sentence consist of N tokens
    2.key 'num_layer': the number of layers in the Transformer model
    3.key 'num_head': the number of heads in the Transformer model
    4.key 'layer_x-head_y': the attention matrix of shape(N,N), from head y in layer x

    Dictionary in 'decoder_encoder_attention' should contain the following keys and corresponding value:
    1.key 'source_sentence': source sentence consist of M tokens
    2.key 'target_sentence': target sentence consist of N tokens
    3.key 'num_layer': the number of layers in the Transformer model
    4.key 'num_head': the number of heads in the Transformer model
    5.key 'layer_x-head_y': the attention matrix of shape(M,N), from head y in layer x
    '''
    if decoder_self_attention is None and encoder_self_attention is None and decoder_encoder_attention is None:
        print("Need at least one type of attention.")
    else:
        if os.path.exists('vistemp')==True:
            shutil.rmtree('vistemp')
        if os.path.exists('vistemp')==False:
            get_dependency(is_transformer=True)
        process_transformer_data(encoder_self_attention,decoder_self_attention,decoder_encoder_attention)
        
        os.chdir('vistemp')
        call_html()
