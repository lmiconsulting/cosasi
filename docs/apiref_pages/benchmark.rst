=============
Benchmark
=============


.. currentmodule:: cosasi.benchmark


Our automatic benchmarking suite handles two input formats. ``BenchmarkFromDetails`` takes arguments that are passed to the inference algorithms, where possible. ``BenchmarkFromSimulation`` takes a ``StaticNetworkContagion`` object and extracts the relevant information to pass to the source inference algorithms.


.. toctree::
   :maxdepth: 5

   benchmark_pages/benchmark_from_details
   benchmark_pages/benchmark_from_simulation