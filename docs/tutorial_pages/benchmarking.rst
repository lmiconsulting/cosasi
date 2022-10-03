======================
Automatic Benchmarking
======================

The ``benchmark`` sub-module takes information about your contagion process, detects which available source inference algorithms are applicable to the problem at hand, and produces an evaluation dictionary with information about their results. This can be done in two ways:

Benchmark From Details
----------------------

The user provides a few details about the simulation - minimally, the true source, the graph the diffusion process was run on, the information type, and the information relevant for that information type - and the ``benchmark`` sub-module will handle the rest. For example:

::

    benchmark = cosasi.BenchmarkFromDetails(
        true_source=true_source,
        G=G,
        I=I,
        t=15,
        number_sources=len(true_source),
        information_type="single snapshot"
    )
    results = benchmark.go()

``results`` is a dictionary-of-dictionaries containing a ``SourceResult`` object and an evaluation dictionary for each inference algorithm applied.


Benchmark From Simulation
-------------------------

Since the contagion object is already available, however, it would be easier to simply pass *that* to the benchmarker. This is done via ``BenchmarkFromSimulation``:

::

    benchmark = cosasi.BenchmarkFromSimulation(
        contagion=already_run_simulation,
        information_type="single snapshot",
        t=15
    )
    results = benchmark.go()

which achieves the same result as above.