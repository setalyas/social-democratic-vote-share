# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 23:17:01 2019

@author: setat
"""

import pandas as pd
import matplotlib.pyplot as plt; plt.style.use('ggplot')

colours = {
        'GB': '#0000CC',
        'DE': '#000000',
        'IT': '#CB333B',
        'FR': '#0055a4',
        'ES': '#EF3340',
        'PT': '#046A38',
        'GR': '#001489',
        'SE': '#004B87',
        'DK': '#DA291C',
        'FI': '#002F6C',
        'AT': '#EF3340',
        'NL': '#C8102E',
        'BE': '#000000',
        'IE': '#FF8200'
        }

data = {'SDP': {"title": "Social democratic party vote %",
                "data": ""},
        "SDPPlus": {"title": "Combined vote % of social democrats,\n greens & far left",
                    "data": ""}
        }
size = 4
    
for k, v in data.items():
    data[k]['data'] = pd.read_csv('AmendedData\\' + k + 'Share.csv', index_col=0)
    flip = data[k]['data'].copy().T
    full_len = len(data[k]['data'])

    # Spaghetti plot
    num = 0
    plt.figure(figsize=(10,10))
    for country in flip:
        num += 1
        # Get the right subplot
        plt.subplot(size, size, num)
        # Plot all lines as a base
        for base in flip:
            plt.plot(flip.index, flip[base], marker='',
                     color='grey', linewidth=0.6, alpha=0.3)
        # Plot the focus line
        plt.plot(flip.index, flip[country], marker='', color=colours[country],
                 linewidth=2.4, alpha=0.9, label=country)
        # Not ticks everywhere
        if num in list(range(1, full_len+1))[:-size] :
            plt.tick_params(labelbottom='off')
        plt.xticks(rotation=70)
        if num not in range(1,size**2, size):
            plt.tick_params(labelleft='off')
        # Add title
        plt.title(country, loc='left', fontsize=12,
                  fontweight=3, color=colours[country])
        plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])
    plt.suptitle(data[k]['title'], fontsize=20, color='black')
    plt.savefig('Outputs\\' + k + 'Share.png')