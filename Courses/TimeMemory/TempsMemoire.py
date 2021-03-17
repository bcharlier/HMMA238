#!/usr/bin/env python
# coding: utf-8

# # Efficacité en temps, mémoire et matrices sparse
#
# ***
# > __Auteur__: Joseph Salmon <joseph.salmon@umontpellier.fr>

# %%

import time
import numpy as np
import matplotlib.pyplot as plt


# ## Time / computation: usage of `%timeit`
# Other *magic*  comme are  %timeit, %matplotlib, %autoreload:
#
# cf.
# https://ipython.org/ipython-doc/3/interactive/magics.html
# https://ipython.org/ipython-doc/3/config/extensions/autoreload.html

# %%
n = 1000
val = 5.4


# %%
%timeit a = np.empty(n); a.fill(val)
# get_ipython().run_line_magic('timeit', 'a = np.empty(n); a.fill(val)')


# %%

%timeit a = np.empty(n); a[:] = val


# %%

%timeit a = np.full((n,), val)


# %%

%timeit a = np.ones(n) * val


# %%

%timeit a = np.repeat(val, n)


# ## Alternatives
# Use the time module:
#
# ```import time```
#

# %%

import time

start = time.time()
a = np.ones(n) * val
end = time.time()

print("Temps passé pour exécuter la commande: {0:.5f} s.".format(end - start))


# ## For more on profiling
#
# In Python `snakeviz` could help, see https://jiffyclub.github.io/snakeviz/
#
# In R, `profvis` is equivalent, see https://rstudio.github.io/profvis/

# ## Debogage : package `pdb`
# Insipiré du site: https://davidhamann.de/2017/04/22/debugging-jupyter-notebooks/
# On va utiliser  `import pdb; pdb.set_trace()` pour rentrer dans un code et requêter les informations des valeurs. Enfin pour continuer le code entre `c` et la touche `enter`.
#
# On peut consulter aussi:
# https://www.codementor.io/stevek/advanced-python-debugging-with-pdb-g56gvmpfa.

# Une première manière de procéder est d'utiliser `pdb` et la commande `pdb.set_trace()` de ce package. Une invite de commande se lance alors quand on a un soucis, et on peut alors reprendre la main voir ce qu'il se passe.
#
# On pourra consulter les raccourcis clavier (e.g., touche c, touche j etc) ici: https://docs.python.org/3/library/pdb.html)

# %%

def illustrate_pdb(x):
    answer = 42
    import pdb; pdb.set_trace()
    answer += x

    return answer

illustrate_pdb(12)


# Une autre manière de procéder est d'allumer le debogueur `pdb`. Une invite de commande se lance alors quand on a un soucis, et on peut alors reprendre la main voir ce qu'il se passe.

# %%

get_ipython().run_line_magic('pdb', '')


# %%

def blobl_func(x):
    answer = 0
    for i in range(x,-1,-1):
        print(i)
        answer += 1 / i

    return answer


# %%

blobl_func(4)


# # Matrices creuses, graphes et mémoire
#
# L'intérêt des matrices creuses est de pouvoir manipuler des matrices, potentiellement énormes, mais qui ont un nombre de coefficients non nuls très petit devant les nombres d'entrées de la matrice, par exemple moins de 1%.
#
# http://scipy-lectures.org/advanced/scipy_sparse/introduction.html#why-sparse-matrices
#
# https://rushter.com/blog/scipy-sparse-matrices/
#
# http://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/
#
# **Examples**:
#
# - natural language processing: we encode the presence of a word from a dictionary (let's say the set of French words) and we put 0 / 1 in case of absence / presence of a word.
# - the discretization of a physical system where very distant influences are set to zero (e.g. heat diffusion, fluid mechanics, electro/magnetism, etc.)
# - graphs: graphs are naturally represented by adjacency or incidence matrices (cf. below), and therefore beyond the graphs, maps!

# %%

from scipy.sparse import isspmatrix


# %%

# Testing when a matrix is sparse or not:
nx, ny = (50, 20)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y, sparse=True)
# print(xv)
print(yv)
isspmatrix(yv)
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)
plt.show()


# ## Graphs and sparsity
#
# Un cadre classique d'application des matrices creuses est le cadre des graphes: bien que le nombre de noeuds puissent être énorme, chaque noeud d'un graphe n'est en général pas relié à tous ses voisins. Si on représente un graphe par sa matrice d'adjacence:

# ## Définition: *matrice d'adjacence*:
# Supposons que $G=(V,E)$ est un graphe, où $\left|V\right|=n$.
# Supposons que les sommets de $G$ sont numérotés arbitrairement $v_1,\ldots,v_n$.
# La matrice d'adjacence $A$ de $G$ est la matrice $n \times n$ de terme général:
#
# $$a_{ij}=\left\{\begin{array}{rl}
# 	1 & \mbox{si } (v_i,v_j) \in E \\
#         0 & \mbox{sinon.}
# \end{array}\right.$$
#

# %%

import networkx as nx


# %%

nx.__version__


# %%

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'A', weight=2)

nx.draw_networkx(G, with_labels=True)
plt.axis('off')
plt.show()


# %%

A = nx.adjacency_matrix(G)
print(A.todense())


# %%

nx.shortest_path(G, 'A', 'D', weight='weight')


# ## Définition : *matrice d'incidence*
# Soit $G = (V,E)$ un graphe (non-orienté) à $n$ sommets, $V = [1,\dots,n] $, et $p$ arrêtes, $E = [1,\dots,p]$.
# Le graphe peut être représenté par sa matrice d'incidence arrête-sommet $D^\top \in \mathbb{R}^{p \times n}$ défini par
# \begin{equation}
#   (D^\top)_{e,v} =
#   \begin{cases}
#     + 1, & \text{si } v = \min(i,j) \\
#     -1, & \text{si } v = \max(i,j) \\
#     0, & \text{sinon}
#   \end{cases}\enspace,
# \end{equation}
# où $e = \{i,j\}$.

# ## Définition : *matrice d'incidence*
#
# The matrix $L=D D^\top$ is the so-called graph Laplacian of $G$
#

# %%

D = nx.incidence_matrix(G, oriented=True).T
print(D.todense())


# ## Visualisation interactive de graphe
#

# %%

import matplotlib.pylab as plt
g = nx.karate_club_graph()
fig, ax = plt.subplots(1, 1, figsize=(8, 6));
nx.draw_networkx(g, ax=ax)
plt.axis('off')
plt.show()


# ### Possible visualisation with Javascript... not so stable...

# %%

# https://andrewmellor.co.uk/blog/articles/2014/12/14/d3-networks/
# https://github.com/brandomr/ner2sna
# REMARQUE: il faut télécharger les fichiers:
# force.css, force.html, force.js pour l'affichage suivant
from networkx.readwrite import json_graph
import json
# Load the graph from a json file:
with open('force.json') as h:
    js_graph = json.load(h)


# %%

from IPython.display import HTML


# %%

get_ipython().run_cell_magic('HTML', '', "\n<iframe height=400px width=100% src='force.html'></iframe>")


# # Graphe et cartes planaires:
# Open Street Map interfaced with Networkx, using  the package `osmnx`:
#
# !!! Known bug:
#
# https://stackoverflow.com/questions/59658167/cannot-import-name-crs-from-pyproj-for-using-the-osmnx-library
# and
# https://stackoverflow.com/questions/60312055/python-getting-typeerror-argument-of-type-crs-is-not-iterable-with-osmnx
#
# so pick version 0.14 at least
#
# ```conda install osmnx>=0.14```
#
# or
#
# ```pip install osmnx>=0.10```
#
#
#
# For Windows users there might be some trouble with installing the `fiona` package, see:
# https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda
# and
# https://jingwen-z.github.io/how-to-install-python-module-fiona-on-windows-os/
#
#
# Special case for `osmnx` on `Windows` follow the next step in order:
# * `pip install osmnx`
# * `pip install Rtree`
# * `conda install -c conda-forge libspatialindex=1.9.3`
# * `pip install osmnx`
#
# * Install all packages required up to `fiona`.
# * `conda install -c conda-forge geopandas`
# * say yes to everything
# * Once done,  launch `pip install osmnx==0.10`
#
# You will also need to install the package `folium`

# %%

import folium


# %%

map_osm = folium.Map(location=[43.610769, 3.876716])


# %%

map_osm.add_child(folium.RegularPolygonMarker(location=[43.610769, 3.876716], fill_color='#132b5e', radius=5))
map_osm


# %%

import osmnx as ox
ox.utils.config(use_cache=True) # caching large download
ox.__version__


# %%

G = ox.graph_from_place('Montpellier, France', network_type='bike')


# %%

ox.plot_graph(G)


# %%

print(G.number_of_edges())
print(G.number_of_nodes())


# # Visualisation d'un chemin le plus court entre deux points.

# %%

# https://blog.ouseful.info/2018/06/29/working-with-openstreetmap-roads-data-using-osmnx/
origin = ox.utils.geocode('Place Eugène Bataillon, Montpellier, France')
destination = ox.utils.geocode('Maison du Lez, Montpellier, France')

origin_node = ox.get_nearest_node(G, origin)
destination_node = ox.get_nearest_node(G, destination)

print(origin)
print(destination)
route = nx.shortest_path(G, origin_node, destination_node)  #XXX double check if weights are taken into account.


# %%

ox.plot_graph_route(G, route)


# %%

ox.plot_route_folium(G, route, route_width=2, route_color='#AA1111')  # adapté de : https://blog.ouseful.info/2018/06/29/working-with-openstreetmap-roads-data-using-osmnx/


# %%

G.is_multigraph()


# %%

edges = ox.graph_to_gdfs(G, nodes=False, edges=True)
nodes = ox.graph_to_gdfs(G, nodes=True, edges=False)
# Check columns
print(edges.columns)
print(nodes.columns)


# %%

D = nx.incidence_matrix(G, oriented=True).T


# %%

print('Size of full matrix with zeros: {0:3.2f}  MB'.format(D.data.nbytes/(1024**2)))


# %%

print(isspmatrix(D))
D


# **Alterntively**: you can uncomment the following line, and check that the size of a similar matrix, with non-sparse format would be
#
# ```>>> Size of full matrix with zeros: 1677.47  MB```

# %%

# # Creation d'une matrice de meme taille
# # BEWARE CREATE HUGE MATRIX:
# M = np.random.randn(G.number_of_nodes(), G.number_of_nodes())
# print('Size of full matrix with zeros: {0:3.2f}  MB'.format(M.nbytes/(1024**2)))


# %%




# ## Sparsité du graphe

# %%

print("Il a {0:.2} % d'arrêtes utlile pour représenter le graphe de la ville de Montpellier".format(100 * G.number_of_edges() / G.number_of_nodes() ** 2))


# ### Remarques : divers type de matrices creuses:
#
# 1. bsr_matrix: Block Sparse Row matrix
# 1. coo_matrix: COOrdinate format matrix
# 1. csc_matrix: Compressed Sparse Column matrix
# 1. csr_matrix: Compressed Sparse Row matrix
# 1. dia_matrix: Sparse matrix with DIAgonal storage
# 1. dok_matrix: Dictionary Of Keys based sparse matrix.
# 1. lil_matrix: Row-based linked list sparse matrix
#
#
# Selon la nature et la structure des données, `csc_matrix` est plus efficace pour le `slicing` par colonne, alors que csr_matrix est plus efficace pour le cas ligne.

# # Pour aller plus loin sur la visualisation de graphes géographiques:
#
# 1. https://geoffboeing.com/2016/11/osmnx-python-street-networks/
# 1. https://automating-gis-processes.github.io/2017/lessons/L7/network-analysis.html
# 1. https://automating-gis-processes.github.io/2018/

# %%

import geopandas


# %%

df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
plt.show()

