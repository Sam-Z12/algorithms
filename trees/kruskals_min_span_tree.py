"""Given a graph G =(V, E) we want to find a minimum spannning tree in the graph (it may not be unique). 
A minimuim spanning tree is a subset of the edges which connect all vertices in the graph with the minimal total edge cost.

Uses union and find:

Find:
find which component a particular elemnent belongs to find the root of that component by following the parent nodes until a self loop is reached(a node whose parent is itself)


Union:
find the two root elements of each group and make one node the parent of the other."""