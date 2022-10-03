========================
Source Results
========================

.. currentmodule:: cosasi.source_inference

All source localization algorithms in ``cosasi`` return an instance of ``SourceResult`` (or a child class thereof, i.e. ``SingleSourceResult`` or ``MultiSourceResult``). This object provides information about the algorithm's results on the problem at hand (e.g. node scores), details and references about the algorithm used, and convenience functions for decision-making.





.. toctree::
   :maxdepth: 5

   source_results_pages/source_result
   source_results_pages/single_source_result
   source_results_pages/multiple_source_result