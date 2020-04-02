# Billiard project

## Group affected: group 5 and 7

The goal of this project is to be able to produce videos and widget representing a point/ball on a billiard with a simple shape and showing its trajectory.

Elements for help could be obtained here:
<https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/>

## Square case

The simple case would be a square billiard, with no friction and satisfying the Descartes rules.

A game to play with this billiard would be to create words associated to trajectories:

Start with an empty word.
Then, when the ball hit the top or bottom part you add an `H` (`H` for horizontal) and when the ball it the left or right part, add a `V` (`V` for vertical).
Perform a statistical analysis of the words creating depending on the angle use to start the trajectory (restrict may be to words of size `<2000`).

## Flat Torus case

You then will study the case of the flat torus billiard. A flat toru is described here <https://en.wikipedia.org/wiki/Torus#Flat_torus>, if needed.

## Elliptic case

Finally, provide elements mimicking the following video: <https://www.youtube.com/watch?v=A7mPzrNJHkA&list=PLTgIq68k2wHH31X-pkBDu2QVeA85G8OHV&index=2&t=0s>
