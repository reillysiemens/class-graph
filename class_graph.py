#!/usr/bin/env python

from py2neo import Graph, Path

graph = Graph()
tx = graph.cypher.begin()

for cl in ["CSCI 141", "CSCI 145"]:
    tx.append("CREATE (class:Class {name:{name}}) RETURN class", name=cl)
csci141, csci145 = [result.one for result in tx.commit()]

classes = Path(csci145, "REQUIRES", csci141)
graph.create(classes)
