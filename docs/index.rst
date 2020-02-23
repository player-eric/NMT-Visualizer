**Overview**
================

**nmtvis** is a visualization toolkit for NMT(Neural Machine Translation) model.

It aims at helping researchers better understand how their model works so that they can further adjust or improve the model.

Installation
------------
   Use pip to install **nmtvis**::

      pip install nmtvis

Requirements
------------
- Python3

- Numpy

Features
--------

- Visualize attention weights in attention-based NMT models
- Other features to be developed


Links
----------

- Source Code: https://github.com/player-eric/NMT-Visualizer
- Documentation: https://nmtvis.readthedocs.io/en/latest

License
----------

The project is licensed under the MIT license.

Support
-------

If you are having issues, please let me know.
Contact me at digimonyan@gmail.com

**Attention Visualization**
====================================
Module **nmtvis.AttentionVisualizer** provides two methods to 
visualize the attention weights in attention-based NMT 
models. 

One method, *visualize_attention()*, aims at visualizing attention between target 
sentence and source sentence in translation. And the other method *visualize_transformer_attention()* 
is targeted at visualizing attention weights in Transformer-based models.

By processing the attention weights into specified format and calling the corresponding method, a temporary web server rendering the visualization 
result will be lauched.

Detailed introduction to this module and its potentioal usage can be view at: https://player-eric.github.io/2020/02/20/nmtvis-attention/

For example code and data, please refer to: https://github.com/player-eric/NMT-Visualizer/tree/master/example

Visualization Views
----------------------
Optionally, the attention weights can be visualized in three views:
 Alignment graph view, Heatmap view, and Highlighted-words view.

   In the alignment view, the source sentence and target sentence are displayed parallelly. Pairs of words from the sentences are connected by lines, with stroke width proportional to the corresponding attention weight.
   
   .. figure:: alignment_view.gif
      :scale: 100 %

      *Alignment View*

   In the heatmap view, attention weights are ploted as a partitioned matrix. Blocks within the matrix are of different color, indicating the extent of attention.

   .. figure:: heatmap_view.png
      
      *Heatmap View*
   
   In the highlighted-words view, a word is selected when the mouse pointer hovers over it. Then all the words(including the selected one) are highlighted according to the attention strength.

   .. figure:: highlight_view.gif
      
      *Heatmap View*


nmtvis.AttentionVisualizer.visualize_attention(*data:List[dict]*)
-------------------------------------------------------------------
.. table::
   :widths: grid
   :align: left

   ===========  ====================================
     Parameter             Detail
   ===========  ====================================
      data      Parameter 'data' is a list of dictionaries.
      
                The length of this list corresponds to number of sentence pairs.
                
                Each dictionary should contain the following keys and value:

                - key 'source_sentence': source sentence consist of M tokens
                - key 'target_sentence': target sentence consist of N tokens
                - key 'attention_matrix': attention matrix of shape (N,M)
   ===========  ====================================

nmtvis.AttentionVisualizer.visualize_transformer_attention(*\*\*kwargs*)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*visualize_transformer_attention()* takes three keyword parameters:
   #. encoder_self_attention
   #. decoder_self_attention
   #. decoder_encoder_attention

Seperately these three parameters are lists of dictionaries, with lengths equal to the number of sentence pairs.
Note that at least one type of attention weights should be passed in.

.. table::
   :widths: grid
   :align: left

   =============================  ====================================
     Parameter                      Detail
   =============================  ====================================
      encoder_self_attention        Each dictionary in 'encoder_self_attention' should contain these keys and value:

                                    - key 'source_sentence': source sentence consist of M tokens
                                    - key 'num_layer': the number of layers in the Transformer model
                                    - key 'num_head': the number of heads in the Transformer model
                                    - key 'layer_x-head_y': the attention matrix of shape(M,M), from head y in layer x

      decoder_self_attention        Each dictionary in 'decoder_self_attention' should contain these keys and value:

                                    - key 'target_sentence': target sentence consist of N tokens
                                    - key 'num_layer': the number of layers in the Transformer model
                                    - key 'num_head': the number of heads in the Transformer model
                                    - key 'layer_x-head_y': the attention matrix of shape(N,N), from head y in layer x  

      decoder_encoder_attention     Each dictionary in 'decoder_encoder_attention' should contain these keys and value:

                                    - key 'source_sentence': source sentence consist of M tokens
                                    - key 'target_sentence': target sentence consist of N tokens
                                    - key 'num_layer': the number of layers in the Transformer model
                                    - key 'num_head': the number of heads in the Transformer model
                                    - key 'layer_x-head_y': the attention matrix of shape(M,N), from head y in layer x  
   =============================  ====================================

