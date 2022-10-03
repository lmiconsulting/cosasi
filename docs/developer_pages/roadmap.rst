===================
Roadmap/Future Work
===================


There are a few areas of development we'd like to prioritize for the future of ``cosasi``:

- **More localization algorithms.** The source inference space is fairly large. We're always looking to extend existing functionality to cover a greater portion of the algorithms prominent in literature.
- **Handle more complex contagions.** We currently implement graph diffusion on static networks. While this can be a satisfactory approximation, realistic contact networks can vary over time; we would like to handle this situation, as well.
- **Implement tools for running and detecting adversarial methods.** Recent progress has been made toward protocols that obfuscate sources, although standard methods like adaptive diffusion are not resilient to adversaries with access to three or more independent "snapshots" (source_). We would like to extend ``cosasi`` to handle both sides of this problem.


.. _source: https://arxiv.org/pdf/2006.11211.pdf