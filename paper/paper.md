---
title: 'cosasi: Graph Diffusion Source Inference in Python'
tags:
  - Python
  - network science
  - graph algorithms
  - network analysis
  - epidemics
  - simulation
  - communication
  - information theory
authors:
  - name: Lucas H. McCabe
    orcid: 0000-0002-7383-2823
    affiliation: "1, 2"
affiliations:
 - name: Digital and Analytic Solutions, Logistics Management Institute
   index: 1
 - name: Department of Mathematics, The George Washington University
   index: 2
date: 3 October 2022
bibliography: references.bib
---


# Summary

`cosasi` (COntagion Simulation And Source Inference) is, to the author's knowledge, the first extensible open-source framework for graph diffusion source inference that allows users to:

- **perform and evaluate** source localization using standard techniques from literature,

- **contribute** innovative algorithms to a growing core library, and

- **benchmark** new techniques against a battery of comparable schemes.

The software is currently used within the Logistics Management Institute. Additional development continues, and we welcome contribution from the broader academic and industrial communities.

# Statement of Need

Because spreading phenomena - including viral epidemics, rumors, and malware - often proceed as a function of pairwise interactions, it is practical to model their propagation as diffusion processes on networks. The source inference/localization problem is that of estimating the inverse of this cascade, aimed at identifying the "patient(s) zero" from partial observations. This problem has captured the attention of epidemiologists, security researchers, social scientists, and more, dating back to Shah and Zaman's seminal work on rumor centrality [@shah2011rumors].

Since then, source inference algorithms have been developed across subject areas, with practitioners often contributing new techniques in domain-specific venues. Additionally, algorithms tend to be problem-specific, with various solutions preferable for different diffusion processes and network topologies. Finally, researchers interested in novel source localization algorithms may not have time to implement a robust battery of alternatives to compare new schemes against the state-of-the-art.

``cosasi`` provides a standard framework for researchers and practitioners alike to perform graph diffusion source inference. The package implements a number of prominent techniques from literature and provides utilities for estimating the number of sources, partitioning infection subgraphs, and more. Where possible, source identification methods are extended as ranking algorithms for hypothesis comparison. ``cosasi`` also offers a ``benchmark`` suite, which automatically implements a battery of comparable localization methods applicable to the graph diffusion use case at hand, enabling users to easily evaluate novel techniques against appropriate baselines. Standardization is emphasized; for instance, all source inference methods return a `SourceResult` object, which provides resources for analyzing, ranking, comparing, and learning more about hypothesized sources and the techniques used.

# Background

Given an undirected graph $G=(V, E)$ with vertex set $V$ and edge set $E$, a diffusion process begins with a source set $S \subseteq V$ and spreads along the edges according to some (usually stochastic) propagation function. It is common for diffusion processes to invoke formalizations from epidemiology, such as the Susceptible-Infected (SI) model, which can represent information spread, or the Susceptible-Infected-Recovered (SIR) model, which can represent dynamics more evocative of viral epidemics. Even when describing metaphorical contagion, such as rumors, it is standard to refer to vertices affected by the spreading process as "infected."

The infection subgraph $I_t$ is the subgraph of $G$ induced by the infected vertices at time $t$. In the single-source SI model, $I_t$ is guaranteed to be connected. A common setting for source localization is to infer $S$ from some $I_t$. More recently, some techniques have incorporated information from a small set of observers, who record the time at which they become infected [@zhu2016locating].

Broadly speaking, source estimators fall into one of two categories: message-passing algorithms, such as *Short-Fat Tree* [@zhu2014information], or spectral algorithms, such as *NETSLEUTH* [@prakash2012spotting]. An extensive overview of source localization techniques is provided by Ying and Zhu [@ying2018diffusion].



# Availability and Documentation

``cosasi`` is available under the [MIT License](https://choosealicense.com/licenses/mit/). The package may be cloned from the [GitHub repository](https://github.com/lmiconsulting/cosasi) or via [PyPI](https://pypi.org/project/cosasi/): ``pip install cosasi``.

Documentation is provided via [Read the Docs](https://cosasi.readthedocs.io/), including a [tutorial](https://cosasi.readthedocs.io/en/latest/tutorial.html) introducing major functionality and a detailed [API reference](https://cosasi.readthedocs.io/en/latest/apiref.html). Extensive unit testing is employed throughout the library, with ~97% code coverage.


# Similar Software

To the author's knowledge, the only comparable and active source localization software is `RPaSDT` [@frkaszczak2022rpasdt]. Here, we enumerate a handful of differences between `RPaSDT` and `cosasi`, which we believe make `cosasi` preferable for user accessibility, scalability, and community contribution:

- **Presentation**: `RPaSDT` is a GUI toolkit. `cosasi` is an importable package, with extensive documentation and unit testing.

- **Benchmarking**: `RPaSDT` does not provide automatic benchmarking, whereas this is a core feature of `cosasi`.

- **Multi-Source Capabilities**: Multi-source inference in `RPaSDT` is generally performed by partitioning the infection subgraph and applying single-source algorithms to each partition. `cosasi` implements this strategy, as well, but also supports "natural" multi-source inference that does not require repurposing single-source techniques.

- **Estimator Utilities**: When extending single-source algorithms to the multi-source regime (as described above), it is generally necessary to specify the number of clusters into which we partition the infection subgraph - that is, the hypothesized number of infection sources. `cosasi` provides a handful of relevant techniques for estimating this quantity, including the *Eigengap* heuristic [@von2007tutorial] and *Minimum Description Length* [@prakash2012spotting].

- **Multiple Information Types**: Some source inference algorithms require information other than an infection subgraph. For instance, *Earliest Infection First* relies on a collection of observers, who report the time at which they become infected [@zhu2016locating]. `cosasi` provides multiple methods for providing state information to the source inference modules, enabling a wider array of potential localization algorithms.

[`Whisper`](http://temigo.github.io/projects/whisper-app/) was an earlier, thematically similar web application. The project has been inactive since 2016, the web interface is no longer online, and the underlying library is less feature-rich than `cosasi` or `RPaSDT`.

A recent graph autoencoder-based approach by Ling and colleagues performs maximum a posteriori source estimation using a generative prior over diffusion sources [@ling2022source]. Their corresponding [GitHub repository](https://github.com/triplej0079/SLVAE) implements their SL-VAE method, but is not a general-purpose diffusion source localization framework.

A handful of libraries exist to simulate diffusion processes on complex networks; `OONIS` [@karczmarczyk2021oonis], `EoN` [@miller2020eon], `contagion` [@lucas_mccabe_2021_4456181], `EpiModel` [@jenness2018epimodel], and `NDlib` [@rossetti2018ndlib] are examples with tens of thousands of downloads among them. These, however, only address the *forward* problem (contagion propagation), whereas `cosasi` is focused on the *inverse* problem (source inference).


# Acknowledgements

`cosasi` was developed in [Forge](https://www.lmi.org/forge), the technology accelerator of the [Logistics Management Institute](https://www.lmi.org/about-lmi).


# References
