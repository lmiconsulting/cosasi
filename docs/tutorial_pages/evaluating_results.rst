==================
Evaluating Results
==================

Source inference algorithms in ``cosasi`` return children of the ``SourceResult`` base class. These come with functions for evaluating the quality of the inference results. Due to the stochasticity of diffusion processes, it is not always common to identify the *exact* source of the infection. Instead, it is reasonable for algorithms to identify a likely source that is very close to the infection center. For this reason, metrics like accuracy may understate the quality of inferences; we employ two alternatives:

Assume we run the following diffusion simulation:

::

    import networkx as nx
    import cosasi
    import random
    import numpy as np

    seed = 42
    random.seed(seed)
    np.random.seed(seed)

    G = nx.fast_gnp_random_graph(200, 0.25, seed=seed)

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.01,
        number_infected = 2
    )
    contagion.forward(100)
    I = contagion.get_infected_subgraph(step=15)


And we run three source localization processes, one implementation of LISN assuming two sources, one of NETSLEUTH providing no information about the number of sources, and one of NETSLEUTH assuming three sources:

::

    two_source_result_lisn = cosasi.source_inference.multiple_source.fast_multisource_lisn(G=G, I=I, t=15, number_sources=2)
    multi_source_result_netsleuth = cosasi.source_inference.multiple_source.netsleuth(G=G, I=I)
    three_source_result_netsleuth = cosasi.source_inference.multiple_source.fast_multisource_netsleuth(G=G, I=I, number_sources=3)

For reference, the true source is available via:

::

    true_source = contagion.get_source()


Calling ``.evaluate()`` from any ``SourceResult`` object runs our evaluation methods (detailed below) and returns a dictionary of results:

::

    two_source_result_lisn_eval = two_source_result_lisn.evaluate(true_source)
    multi_source_result_netsleuth_eval = multi_source_result_netsleuth.evaluate(true_source)
    three_source_result_netsleuth_eval = three_source_result_netsleuth.evaluate(true_source)



Solution Rank
-------------

Where possible, ``cosasi`` extends localization algorithms to perform ranking over many hypotheses. This way, we may rank all hypotheses according to the algorithm's implicit scoring criteria and return the rank of the true source among all hypotheses. This is similar to the "precision at k" metric prevalent in information retrieval.

We can find this in the ``two_source_result_lisn_eval`` dictionary:

::

    >>> two_source_result_lisn_eval["rank"]
    12

So the true source was the 12th highest-ranking hypothesis by this algorithm.


Distance from True Source
-------------------------

In the single-source setting, it is typical for all vertices to be evaluated. In the multi-source regime, however, this is intractable for large graphs. Furthermore, when the number of "patients zero" is unknown, it is not unusual for the hypothesized source set to be of a different size than the true source set. As such, it is possible - if not likely - for the true source set to not be found among the evaluated hypotheses at all, making solution rank a poor evaluation metric.

We implement a metric that assesses the minimum graph distance between vertex sets that may be of different sizes. In particular, we pair nodes in Set 1 with nodes in Set 2, subject to the constraint that every node in Set 1 is paired to a node in Set 2 and vice-versa. For any such pairing, we measure the sum of shortest-path lengths between each pair. Our algorithm returns the minimum such sum across possible pairings.

We can find this in the ``multi_source_result_netsleuth_eval`` dictionary:

::

    >>> multi_source_result_netsleuth_eval["distance"]["top score's distance"]
    {(93, 81): 4}

The top-scoring hypothesis was close to the true source.

We also evaluate the distance from true source of all computed hypotheses, although this is not very useful for the standard NETSLEUTH algorithm, since it only generates one hypothesized source. The ``fast_multisource_netsleuth`` version is not always as accurate in the best case, but is better-suited for ranking, because it assesses many hypotheses:

::

    >>> distances = three_source_result_netsleuth_eval["distance"]["all distances"].values()
    >>> min(distances), max(distances)
    (4, 8)

We see that the distance from true source of these hypotheses ranged from 4 to 8.
