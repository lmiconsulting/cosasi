====================
Running a Simulation
====================

While ``cosasi``'s focus is on the inverse problem of inferring the origin of a diffusion process, we provide a simulator of the forward problem for convenience. This functionality is found in ``cosasi.contagion``, which is built on ``NetworkX`` and ``NDlib``.

``StaticNetworkContagion`` objects need:

- A contact network to spread on (``NetworkX`` graph)
- An epidemic model to run (one of SI, SIS, or SIR)
- An ``infection_rate`` specifying the infectivity of the contagion

We first define a contact network for the diffusion process to spread on; these are implemented as ``NetworkX`` graphs.

::

    import networkx as nx
    import cosasi
    import random
    import numpy as np

    seed = 42
    random.seed(seed)
    np.random.seed(seed)

    G = nx.fast_gnp_random_graph(200, 0.01, seed=seed)


Then define a contagion object:

::

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.2,
        seed=seed
    )

By default, one vertex, selected uniformly at random, is "infected" at initialization. Alternately, the user can specify a number of "patients zero":

::

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.2,
        number_infected=4,
        seed=seed
    )

or a fraction to be "infected" at initialization:

::

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.2,
        fraction_infected=0.05,
        seed=seed
    )

If the epidemic model is SIR or SIS, the user must provide a recovery rate at which vertices in the infected compartment switch to the recovered or susceptible compartments:

::

    contagion = cosasi.StaticNetworkContagion(
        G=G,
        model="si",
        infection_rate=0.2,
        recovery_rate=0.005,
        seed=seed
    )


After initialization, run the contagion process for as many steps as desired:

::

    contagion.forward(steps=100)

To reset compartmental histories, simply run:

::

    contagion.reset_sim()
