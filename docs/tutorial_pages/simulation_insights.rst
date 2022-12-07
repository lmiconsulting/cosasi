=================================
Extracting Simulation Information
=================================

``StaticNetworkContagion`` objects save their compartmental histories. These can be retrieved via their ``history`` attribute.

The user may only be interested in recalling the set of source vertices of a simulation named ``contagion``; this is achievable via ``contagion.get_source()``. By passing an additional ``return_subgraph=True`` argument, the source set will be returned as the subgraph induced by the source nodes.

Source inference algorithms require information about the contagion's status. We begin with standard graph generation and contagion simulation (as outlined in the previous section):

::

    import networkx as nx
    import cosasi
    import random
    import numpy as np

    seed = 42
    random.seed(seed)
    np.random.seed(seed)

    G = nx.fast_gnp_random_graph(200, 0.15, seed=seed)

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.01,
        number_infected=4,
    )
    contagion.forward(steps=100)


The most common information type in source inference literature is a "snapshot,"" where complete information about the infection is provided for a particular time step:

::

    contagion.get_infected_indices(step=10)

retrieves the the indices of all vertices in the infected compartment at simulation step 10, and

::

    contagion.get_infected_subgraph(step=10)

returns the induced subgraph of the vertices in the infected compartment at the provided step. Alternately, some algorithms employ "observers," a handful of vertices that are designated to record when they become infected. In our implementation, the user specifies the number of observers, and the particular selection is performed uniformly at random:

::

    contagion.get_observers(observers=5)


Note that, if the infection model is SIS, nodes may be reinfected, so observers record a list of the timestamps at which they are infected. Otherwise, observers record one timestamp (step number) only.

A common analytical tool is the infection frontier, which is the set of infected vertices with infected neighbors:

::

    contagion.get_frontier(step=10)

This is especially pertinent to the SI epidemic model, because vertices do not recover. In this case, the frontier set consists of nodes that may have been infected last, by the given timestep.
