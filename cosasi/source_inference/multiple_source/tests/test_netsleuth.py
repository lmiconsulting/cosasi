import os, sys

sys.path.insert(0, os.getcwd())

from unittest import TestCase

import pytest
import networkx as nx
import numpy as np
import random
import math

import cosasi


class TestNETSLEUTH(TestCase):
    def setUp(self):
        self.G = nx.complete_graph(n=100)
        contagion = cosasi.StaticNetworkContagion(
            G=self.G, model="si", infection_rate=0.1, number_infected=1
        )
        contagion.forward(50)
        self.t = 25
        self.I = contagion.get_infected_subgraph(self.t)
        return None

    def test_fast_multisource_netsleuth(self):
        result = cosasi.source_inference.multiple_source.fast_multisource_netsleuth(
            self.I, self.G, number_sources=3
        )
        assert isinstance(
            result, cosasi.source_inference.source_results.MultiSourceResult
        )
        top5 = result.topn(5)
        assert [len(i) == 3 for i in top5]
        result = cosasi.source_inference.multiple_source.fast_multisource_netsleuth(
            self.I, self.G
        )
        l = None
        for k in result.data["scores"].keys():
            if not l:
                l = len(k)
            else:
                assert len(k) == l

    def test_netsleuth(self):
        result = cosasi.source_inference.multiple_source.netsleuth(self.I, self.G)
        assert isinstance(
            result, cosasi.source_inference.source_results.MultiSourceResult
        )
        result = cosasi.source_inference.multiple_source.netsleuth(self.I, self.G)
        l = None
        for k in result.data["scores"].keys():
            if not l:
                l = len(k)
            else:
                assert len(k) == l
            assert result.data["scores"][k] > 0
