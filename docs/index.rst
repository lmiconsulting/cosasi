.. cosasi documentation master file, created by
   sphinx-quickstart on Fri Jul 29 17:27:10 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``cosasi`` Documentation
=======================================================

.. figure:: _assets/grasshopper.png
   :figwidth: 100%
   :align: left


Overview
=================

``cosasi`` is a Python package for graph diffusion source localization, allowing users to:

- **perform and evaluate** source inference using standard techniques from literature,
- **contribute** innovative localization methods to a growing core library, and
- **benchmark** new techniques against a battery of comparable schemes.


.. figure:: _assets/carbon.png
   :align: center
   
   Above: Carbon_ image of example code snippet; copy-and-paste-able version below.

::

   import networkx as nx
   import cosasi

   G = nx.fast_gnp_random_graph(100, 0.25)
   contagion = cosasi.StaticNetworkContagion(
       G=G,
       model="si",
       infection_rate=0.01,
       number_infected=3,
   )
   contagion.forward(100)
   I = contagion.get_infected_subgraph(step=15)
   result = cosasi.source_inference.multiple_source.netsleuth(G=G, I=I)
   result.evaluate(contagion.get_source())



Table of Contents
=================
.. toctree::
   :titlesonly:
   :maxdepth: 1

   quickstart
   tutorial
   developer
   apiref



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`


.. _Carbon: https://github.com/carbon-app/carbon
