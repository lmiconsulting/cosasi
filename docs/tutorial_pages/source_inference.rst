================
Source Inference
================

We implement two flavors of source inference algorithm: single-source, accessible via ``cosasi.source_inference.single_source``, and multi-source, accessible via ``cosasi.source_inference.multiple_source``.

The general pattern for most source inference algorithms consists of the original graph the contagion was run on, the infection subgraph at some designated point, and (sometimes) the timestep marking that point. We begin with standard graph generation, contagion simulation, and infection subgraph extraction (as outlined in previous sections):

::

    import networkx as nx
    import cosasi
    import random
    import numpy as np

    seed = 42
    random.seed(seed)
    np.random.seed(seed)

    G = nx.fast_gnp_random_graph(200, 0.01, seed=seed)

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.2,
        number_infected = 4,
        seed=seed
    )
    contagion.forward(steps=100)
    I = contagion.get_infected_subgraph(step=10)


With ``I`` and ``G``, we may run source inference algorithms. For instance:

::

    single_source_result = cosasi.single_source.netsleuth(I, G)

executes the single-source version of the popular NETSLEUTH algorithm. A timestep parameter ``t`` can be provided, but is not required. Alternately, running:

::

    multi_source_result = cosasi.multiple_source.netsleuth(I, G)

executes the more standard multi-source NETSLEUTH implementation, which employs a Minimum Description Length heuristic to identify the source set size best-suited for the problem. z

A wide variety of source inference algorithms are implemented in ``cosasi``, including NETSLEUTH, Rumor Centrality, Short-Fat Tree, Earliest Infection First, and more; these are detailed further in the API reference. Where possible, source methods are extended as ranking algorithms to support multi-hypothesis tracking.

All source inference results are provided as children of the ``SourceResult`` abstract class - ``SingleSourceResult`` for single-source algorithms and ``MultiSourceResult`` for multi-source algorithms. These come with convenient features for ranking and hypothesis comparison. For example:

::

    single_source_result.rank()

ranks all hypotheses by the algorithm's scoring method. In single-source algorithms, hypotheses are individual nodes, whereas in multi-source algorithms these are sets of several nodes. If the user is only interested in the top few hypotheses:

::

    >>> print(single_source_result.topn(n=5))

    [176, 105, 36, 17, 143]

Any ``SourceResult`` also retains details about the algorithm itself, including model assumptions and literature references:

::

    >>> print(single_source_result.data["inference method"])

    {'name': 'netsleuth',
    'source_type': 'multi-source',
    'epidemic model': ['si', 'ic'],
    'information type': 'single snapshot',
    'reference': {'publication link': 'https://ieeexplore.ieee.org/document/6413787',
    'manuscript link': 'https://faculty.cc.gatech.edu/~badityap/papers/netsleuth-icdm12.pdf'},
    'status': 'complete',
    'namespace': 'cosasi.multiple_source.netsleuth'}
