import json
#import pandas as pd
from bs4 import BeautifulSoup

COLORS = [
  'black', 'red', 'green', 'yellow', 'blue', 'purple', 'aqua', 'white'
]


#  Color Palettes of Themes from "https://gogh-co.github.io/Gogh/"
with open('./palettes') as f:
  data = f.readline()

soup = BeautifulSoup(data, 'lxml')
out_palettes = {}

for theme_palette_container in soup.select('.terminal'):
  them_name = theme_palette_container.select_one('.bar__title').get_text()
  out_palettes[them_name] = {}

  top_colors = theme_palette_container.select_one('.body__bar--top')\
    .find_all('span')
  n = 0
  for span in top_colors:
    rgb_str = span.attrs['style'].split('rgb')[1].split('(')[1].\
      split(')')[0].split(',')
    rgb = [int(i) for i in rgb_str]
    out_palettes[them_name][COLORS[n] + '_1'] = rgb
    n += 1

  bottom_colors = theme_palette_container.select_one('.body__bar--bottom')\
    .find_all('span')
  n = 0
  for span in bottom_colors:
    rgb_str = span.attrs['style'].split('rgb')[1].split('(')[1].\
      split(')')[0].split(',')
    rgb = [int(i) for i in rgb_str]
    out_palettes[them_name][COLORS[n] + '_2'] = rgb
    n += 1


with open('themes_colors_palettes.json', 'w') as f:
  json.dump(out_palettes, f, indent=2)