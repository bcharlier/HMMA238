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

- Mohamed Fattouhy, source: https://github.com/mohamedfattouhy/Challenge_bike
 
 [<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/mohamedfattouhy.png?sanitize=true" height="300">](https://rawcdn.githack.com/mohamedfattouhy/Challenge_bike/b31c12cfbe272a823c3e4c574c6dc161f30c9728/map.html)


- Nathan Esteve, source : https://github.com/Nathanesteve/Challenge_prediction

[<img src="https://github.com/Nathanesteve/Challenge_prediction/blob/main/Gif/Montpellier_cycliste.gif?sanitize=true" height="300">](https://github.com/Nathanesteve/Challenge_prediction/blob/main/Gif/Montpellier_cycliste.gif)


- Assia Berrandou, source : https://github.com/Assiab2707/packaging_challenge_brda

[<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/assia_berrandou.png?sanitize=true" height="300">](https://assiab2707.github.io/packaging_challenge_brda/)


- Bouthayna Hayou,  source: https://github.com/B-hayou/Challenge2021

[<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/bouthayna_hayou.png?sanitize=true" height="300">](https://bhayou.pythonanywhere.com)

- Chloé Serre-Combe, source: https://github.com/chloesrcb/bike_challenge

[<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/chloe_serre-combe.png?sanitize=true" height="300">](https://mybinder.org/v2/gh/chloesrcb/bike_challenge/main?filepath=Visualization%2Fwidget.ipynb)

- Amélie Vernay, source: https://github.com/AmelieVernay/MtpBikeViz

[<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/amelie_vernay.png?sanitize=true" height="300">](https://amelievernay.pythonanywhere.com)

- Otmane Jabbar, source:  https://github.com/otmanejb/challenge-/blob/main/Visualization/visualization.ipynb

[<img src="https://raw.github.com/bcharlier/HMMA238/master/Challenge/2020-2021/feedback/otmane_jabbar.png?sanitize=true" height="300">](https://giphy.com/gifs/wrdRBkkA3CbaL37GD9/)
