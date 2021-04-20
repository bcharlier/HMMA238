# Feedback --- Most common errors/ issues



 ## Prediction part
- get more data
- respect guidelines (less than 2 pages, means 4 is bad!)
- spellchecker, ALWAYS!
- no jpg, no png from R/python figures. Export in pdf!!! [<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/no_bitmap_please.png?sanitize=true" height="400">](https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/no_bitmap_please.png?sanitize=true)
- the bike project was short (try to make it one file if possible)
- do not duplicate code (after copy pasting 3 times the same, stop and think!)
- PEP8 of course (linter: flake8, etc.)!
- Excel was forbidden by the way, it was a course on Python !

### Statistical issues

- subsampling only the time stamps between 00:00 and 09:00 would lead to a downward bias, since by doing so you have very few data point around 09:00, while this is a rush hour (so many bikes around that time).
- train/test is tricky on dates. Read https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split for instance, to master nested versions.
- testing the prediction on your own test/train sets would have been important to avoid being confident in your own predictions.
- Merge the two datasets from the challenge (code will be posted), this would provide additional insight...


### TeX tips:

- Use \varepsilon for random variables / \epsilon for small quantities.


## Visualization part

- Make the visual part self-contained. What is displayed should be crystal clear.
- Image resolution: not too small, otherwise details are lost, or it is ugly.
- jittering (to avoid!)
- Add the time information otherwise your visualization is useless:
  date / hour, etc.
- Explain / add legend: what is the unit for your disks size?
- Don't use **RED / GREEN** (10% of men are colorblind)
- Using open resources was a bonus!

### Interesting solutions

- [<img src="https://mohamedfattouhy" height="300">](https://rawcdn.githack.com/mohamedfattouhy/Challenge_bike/b31c12cfbe272a823c3e4c574c6dc161f30c9728/map.html)
 
- https://github.com/Nathanesteve/Challenge_prediction/blob/main/Gif/Montpellier_cycliste.gif
 (nice time evolution)

- https://github.com/Assiab2707/packaging_challenge_brda
 (nice time evolution, can you improve using Amelie's work for minutes prediction)

- https://github.com/lllinares/challengebike238/blob/master/montmap.html

- https://bhayou.pythonanywhere.com

- https://github.com/chloesrcb/bike_challenge

- https://amelievernay.pythonanywhere.com

- https://giphy.com/gifs/wrdRBkkA3CbaL37GD9 / https://github.com/otmanejb/challenge-/blob/main/Visualization/visualization.ipynb
 (simple yet original: display a bit weak though, color and legend to improve)