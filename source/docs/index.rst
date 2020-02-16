**Overview**
================

**nmtvis** is a visualization toolkit for NMT(Neural Machine Translation) system.

Look how easy it is to use:

Installation
------------
   Use pip to install **nmtvis**::

      pip install nmtvis

Requirements
------------
   Python3

   Numpy

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
**nmtvis.AttentionVisualizer** provides two interfaces to 
visualize the attention weights in attention-based NMT 
models. 

One interface, *visualize_attention()*, aims at visualizing attention between target 
sentence and source sentence in translation. And the other interface *visualize_transformer_attention()* 
is targeted at visualizing attention weights in Transformer-based models.

By processing the attention weights into specified format and calling the interfaces, a temporary web server rendering the visualization 
result will be lauched.

Visualization Views
----------------------
Optionally, the attention weights can be visualized in three views:
 alignment graph view, heatmap view, and highlighted-words view.

   In the alignment view, the source sentence and target sentence are displayed parallelly. Pairs of words from the sentences are connected by lines, with stroke width proportional to the corresponding attention weight.
   
   .. figure:: alignment_view.gif
      :scale: 100 %

      *Alignment View*

   In the heatmap view, attention weights are ploted as a partitioned matrix. Blocks within the matrix are of different color, indicating the extent of atten- tion.

   .. figure:: heatmap_view.png
      
      *Heatmap View*


nmtvis.AttentionVisualizer.visualize_attention(*data:List[dict]*)
-------------------------------------------------------------------
Visualizing 
