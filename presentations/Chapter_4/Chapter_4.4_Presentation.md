# Coloring
## Coloring in General:
<b>Definition</b>: Coloring refers to the assignment of labels/colors to the subject of constraint. <b>Vertex coloring</b> is a more
commonly used type of coloring where each vertex has a color assigned to it, and no connected/adjacent vertices can have the same color (no
vertices that have an edge between them). In graphing, there is something called a <b>clique</b> in a graph is a set of vertices all of
which are pairwise adjacent which is practically a size n is just a copy of the complete graph Kn. From this the <b>clique number</b> of a
graph can be made which is the largest n for which the graph contains a clique of size n. The goal when coloring is often to find the
<b>chromatic number</b>, which is the smallest amount of numbers to complete the coloring task, or the smallest clique number possible.

![image](https://github.com/bananajoeo7/csc208/assets/112637228/79463752-7aa3-45a6-a405-30fe8dd47718)


To talk about Brook's Theorem, a theory devised from this we go to [Johan's Presentation](https://github.com/johan-franco/csc208/blob/main/ch4_GraphTheory/sect4.4.md).

## Coloring Edges:
<b>Vizing's Theorem</b>: Vizing's Theorem is a key result in graph theory concerning the edge coloring of simple graphs. It states that for
any simple graph  $G$, the chromatic index $x'(G)$, which is the minimum number of colors needed to color the edges such that no two
edges sharing a vertex have the same color, is either $\Delta(G)$ or $\Delta(G) + 1$, where $\Delta(G)$ is the maximum degree of
any vertex in the graph. This means the number of colors required will be at most one more than the maximum number of edges incident to any
vertex.

<b>Ramsey Theory</b>: is the coloring of graphs with the aim of avoiding monochromatic subgraphs, such as triangles. For instance, when
coloring edges of $K_n$ (complete graphs) either red or blue, some graphs like $K_4$ can avoid forming a monochromatic triangle, but others
like $K_5$ cannot. The theory extends to using more colors and larger subgraphs, though much remains unknown. For example, it’s known that
$K_{17}$ is the smallest graph forcing a monochromatic triangle with three colors, and $K_{18}$ is the smallest for forcing a monochromatic
$K_4$ with two colors. However, the exact size required to force a monochromatic $K_5$ remains uncertain, estimated to be between $K_{43}$
and $K_{49}$. This area of graph theory is rich with open questions and is known as Ramsey's Theory.

![image](https://github.com/bananajoeo7/csc208/assets/112637228/99abb30a-d772-4799-bf53-770e32e4b4f4)


Now we continue on to [Luis's Presentation](https://github.com/ledmer/CSC208/blob/main/4.Graph_Theory/4.Coloring/exercises.md) once again.

#### sources:
[Wiki Graph Coloring](https://en.wikipedia.org/wiki/Graph_coloring) \
[Wiki Ramsey Theory](https://en.wikipedia.org/wiki/Ramsey_theory)
