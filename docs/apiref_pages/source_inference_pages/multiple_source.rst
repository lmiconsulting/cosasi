=========================
Multiple-Source Inference
=========================

.. currentmodule:: cosasi.source_inference


Some single-source algorithms have known multi-source counterparts; where available, we implement these. Other single-source algorithms may be extended to the multi-source regime by partitioning the infection subgraph into sub-subgraphs attributable to each infection source and running the single-source algorithm on each sub-subgraph; such implementations are denoted ``fast_multisource_X`` to distinguish from any standard multi-source implementation of ``X``.






.. toctree::
   :maxdepth: 5

   multiple_source_pages/netsleuth
   multiple_source_pages/jordan_centrality
   multiple_source_pages/lisn