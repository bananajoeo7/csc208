# Coloring
## Coloring in General:
<b>Definition</b>: Coloring refers to the assignment of labels/colors to the subject of constraint. <b>Vertex coloring</b> is a more
commonly used type of coloring where each vertex has a color assigned to it, and no connected/adjacent vertices can have the same color (no
vertices that have an edge between them). In graphing, there is something called a <b>clique</b> in a graph is a set of vertices all of
which are pairwise adjacent which is practically a size n is just a copy of the complete graph Kn. From this the <b>clique number</b> of a
graph can be made which is the largest n for which the graph contains a clique of size n. The goal when coloring is often to find the
<b>chromatic number</b>, which is the smallest amount of numbers to complete the coloring task, or the smallest clique number possible.

To talk about Brook's Theorem, a theory devised from this we go to (Johan's Presentation)[Insert Johan Link Here].

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
and $K_{49}$. This area of graph theory is rich with open questions and is known as Ramsey Theory.

Now we continue on to (Johan's Presentation)[Insert Johan Link Here] once again.
