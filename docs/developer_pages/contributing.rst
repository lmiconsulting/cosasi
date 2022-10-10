=================
Contributor Guide
=================


We'd love your help! If you'd like to make an addition or improvement, please submit a pull request consisting of an atomic commit and a brief message describing your contribution.



Adding New Source Inference Algorithms
--------------------------------------

1. Your algorithm should occupy its own file ``your_algorithm_name.py`` within either ``source_inference/single_source`` or ``source_inference/multiple_source``, as appropriate.

2. Import your algorithm ``from .your_algorithm_name import *`` in either ``source_inference/single_source/__init__.py`` or ``source_inference/multiple_source/__init__.py``, as appropriate.

3. Add an entry for your new algorithm to ``utils/algorithm_details.json``. Minimally, this should include details for ``epidemic model`` and ``information type``. If possible, inclusion of a manuscript/pre-print/ArXiv link is desirable so that users may freely review the resource.

    The entry for ``rumor_centrality`` is illustrated below:

    ::

        "rumor centrality": {
            "epidemic model": ["si", "ic"],
            "information type": "single snapshot",
            "reference": {
                "publication link": "https://devavrat.mit.edu/wp-content/uploads/2017/10/Rumors-in-a-network-whos-the-culprit.pdf",
                "manuscript link": "https://core.ac.uk/download/pdf/4434717.pdf"
            },
            "status": "complete",
            "namespace": "cosasi.single_source.rumor_centrality"
        }




Naming Conventions
------------------

When writing source inference algorithms, we follow a few naming conventions for the arguments. Here is a non-exhaustive list:

+-----------------------+--------------------------------------------------------------+
| Param                 | Meaning                                                      |
+=======================+==============================================================+
| G                     | The original graph on which the infection process was run    |
+-----------------------+--------------------------------------------------------------+
| I                     | The infection subgraph observed at a particular time step    |
+-----------------------+--------------------------------------------------------------+
| t                     | the timestep corresponding to I                              |
+-----------------------+--------------------------------------------------------------+
| number_sources        | the hypothesized number of infection sources                 |
+-----------------------+--------------------------------------------------------------+




Testing
-------
All code should be tested. We use `pytest`_.

To run the test suite, run `pytest`_ via `coverage`_:

    ::

        coverage run -m pytest


To read the ``.coverage`` file:

    ::

        coverage report




Guidelines
-------------------
We defer to the `contributor guidelines`_ outlined by `NetworkX`_.



Bugs
-------------------
If you find something wrong, please submit a bug report to the issue tracker.




.. _pytest: https://docs.pytest.org/en/7.1.x/contents.html
.. _coverage: https://coverage.readthedocs.io/en/6.3.2/
.. _contributor guidelines: https://networkx.org/documentation/stable/developer/contribute.html#guidelines
.. _NetworkX: https://networkx.org/documentation/stable/index.html
