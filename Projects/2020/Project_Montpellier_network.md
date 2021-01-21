# Montpellier network

## Group affected: group 6

The goal of this project is to be able to produce videos and widget representing a car, a pedestrian and a bicycle going from la *maison du Lez* to *Place Eugène Bataillon* in Montpellier with the shortest path possible (w.r.t. the kind of user).

For that you will have to load the graph of the roads/bike trails in Montpellier using the Python package `osmnx`.

Helps on this can be found here:
<http://josephsalmon.eu/HMMA238.html>, see `6-TempsMemoire.ipynb`.

For the shortest path algorithm, standard implementation from `networkx` could be used.

## Video

The video of interest should represent a car, a pedestrian and a bicycle moving on the graph representing the city of Montpellier, at a reasonable speed (say the speed provided by Google maps for the three kind of users).

**Bonus:** provide also a way to produce a video similar to that one below in terms of rendering (use a blurring effect to perform the trail behind the points):
<https://www.youtube.com/watch?v=SKJ6BsycvJA&t=206s>
