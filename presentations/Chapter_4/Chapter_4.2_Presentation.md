# Chapter 4.2 Presentation by Trostin, Akshay, and Ved:
## Question #4:
### 4. Suppose you have a graph with vertices and edges that satisfies $v = e + 1$. Must the graph be a tree? Prove your answer.

The question asks in any case that satisfies $v = e + 1$ will the graph always be a tree.

First, let's define what a tree is.
Tree: a tree is a type of graph characterized by being acyclic and connected, meaning it has no cycles and there is a path between 
any pair of vertices. A tree with ( n ) vertices always has ( n-1 ) edges, making it minimally connected—removing any edge would 
disconnect the graph. There is exactly one path between any two vertices, ensuring no redundancy, and adding any edge would create
a cycle. When one vertex is designated as the root, it forms a rooted tree with a hierarchical structure. Trees are fundamental 
structures in graph theory with important properties and applications.

Now that we have defined what a tree is we can begin solving.

We can assume since $v = e + 1$, $e = v - 1$, so for the total amount of vertices there is one less edge.

While in some cases it meets the requirements like the following:

![graph](https://github.com/bananajoeo7/csc208/assets/112637228/95f112a8-7aaf-40c9-b361-939abab6a88b)

![graph (1)](https://github.com/bananajoeo7/csc208/assets/112637228/1e4347d2-155c-4fc8-b24d-2ea85a934aa5)

In others, it doesn't like the following graph:

![graph (2)](https://github.com/bananajoeo7/csc208/assets/112637228/854c28b6-1b6a-4fcf-9801-f57dd77d9145)

Since a graph doesn't require all the vertices to be connected the graph above satisfies the function $v = e + 1$.

Though it does meet the function requirements, there is a cycle (loop) and it doesn't have a path between every vertice, in turn making
it, not a tree, proving that every case of the function isn't a tree.

[Akshays presentation](https://github.com/AkshayKuchibhatla/csc208/blob/main/ch4_graphTheory/sect4.2.md)
