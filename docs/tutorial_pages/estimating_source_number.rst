=====================================
When the Number of Sources is Unknown
=====================================

Practically, neither the identities nor size of the source set are often known. For this case, we provide functions for estimating the number of infection sources, given the observation of an infection subgraph at one ambiguous time step.

Here, we will specify a network for the diffusion process to spread on, simulate a contagion, and obtain an infection subgraph from time ``t=10``:

::

    import cosasi
    import networkx as nx

    G = nx.fast_gnp_random_graph(200, 0.05)
    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.01,
        number_infected = 4
    )
    contagion.forward(100)
    I = contagion.get_infected_subgraph(10)


Now, we can estimate the number of sources. Our default method is based on spectral analysis, namely the Eigengap heuristic. We calculate the eigenvalues of the infection subgraph's normalized Laplacian matrix, sort it from least to greatest, and report the index at which the difference between consecutive eigenvalues is maximized.

We provide ``number_sources=None`` to instruct ``cosasi`` to automatically estimate the number of sources, and we provide ``return_source_subgraphs=False`` because we're not interested in retrieving anything other than the estimated number of sources (this will be elaborated upon).

::

    m = cosasi.utils.estimators.number_sources(I=I, number_sources=None, return_source_subgraphs=False, number_sources_method="eigengap")


In this particular case, we find ``m==5``, which is close to the true number of sources, 4. Note that, since this is the default method, one achieves the same result by declining to provide any ``number_sources_method`` argument.


An alternative approach is to invoke the NETSLEUTH source inference algorithm, automatically estimates the number of sources via a Minimum Description Length heuristic. The algorithm runs sufficiently quickly to be used for estimating the number of sources on its own. This is achieved by providing ``number_sources_method='netsleuth'`` and an argument for the original graph the infection process was run on:

::

    m = cosasi.utils.estimators.number_sources(I=I, number_sources=None, return_source_subgraphs=False, number_sources_method="netsleuth", G=G)



Some multi-source localization algorithms require the user to guess (sub-)subgraphs of the infection subgraphs that are attributable to each source node. Of course, this is nontrivial when the sources are not known! We estimate each source's attributable infection subgraph via spectral clustering; all the user needs to do is switch ``return_source_subgraphs`` to ``True``:

::

    m, subgraphs = cosasi.utils.estimators.number_sources(I=I, number_sources=None, return_source_subgraphs=True)


If the user knows or conjectures a particular number of sources (e.g. 4, but does not know the infection subgraphs that are attributable to each source node, these can be estimated using the same function:

::

    m, subgraphs = cosasi.utils.estimators.number_sources(I=I, number_sources=4, return_source_subgraphs=True)

