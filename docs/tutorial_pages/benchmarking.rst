======================
Automatic Benchmarking
======================

As before, we begin by specifying a network and simulating a contagion, per the boilerplate of previous sections:

::

    import networkx as nx
    import cosasi
    import random
    import numpy as np

    seed = 42
    random.seed(seed)
    np.random.seed(seed)

    G = nx.fast_gnp_random_graph(200, 0.1, seed=seed)

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.01,
        number_infected = 4,
        seed=seed
    )
    contagion.forward(100)
    I = contagion.get_infected_subgraph(10)
    true_source = contagion.get_source()


The ``benchmark`` sub-module takes information about your contagion process, detects which available source inference algorithms are applicable to the problem at hand, and produces an evaluation dictionary with information about their results. This can be done in two ways:

Benchmark From Details
----------------------

The user provides a few details about the simulation - minimally, the true source, the graph the diffusion process was run on, the information type, and the information relevant for that information type - and the ``benchmark`` sub-module will handle the rest. For example:

::

    benchmark = cosasi.BenchmarkFromDetails(
        true_source=true_source,
        G=G,
        I=I,
        t=10,
        number_sources=len(true_source),
        information_type="single snapshot"
    )
    results = benchmark.go()

``results`` is a dictionary-of-dictionaries containing a ``SourceResult`` object and an evaluation dictionary for each inference algorithm applied.


Benchmark From Simulation
-------------------------

Since the contagion object is already available, however, it would be easier to simply pass *that* to the benchmark tool. This is done via ``BenchmarkFromSimulation``:

::

    benchmark = cosasi.BenchmarkFromSimulation(
        contagion=contagion,
        information_type="single snapshot",
        t=10
    )
    results = benchmark.go()

which achieves the same result as above.
