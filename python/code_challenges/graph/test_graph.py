from graph.graph import Graph, Vertex
import pytest


def test_add_node():
    graph = Graph()
    expected = 'dina'
    actual = graph.add_node('dina').value
    assert actual == expected


def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


def test_size():
    graph = Graph()
    graph.add_node('dina')
    assert graph.size() == 1

    graph.add_node('fouad')
    assert graph.size() == 2


def test_add_edge_start():
    graph = Graph()
    start = Vertex('start')
    end = graph.add_node('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_end():
    graph = Graph()
    end = Vertex('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


