# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 23:17:01 2019

@author: setat
"""

import pandas as pd
import matplotlib.pyplot as plt; plt.style.use('ggplot')

# https://twitter.com/NeilWarner_/status/1210929335458291715

sdp = """Social democratic parties at beginning of century, beginning of \
decade & now (vote % in latest legislative election):
🇬🇧
 43 35 32
🇩🇪
 41 23 21
🇮🇹
 42 33 19
🇫🇷
 24 25 7
🇪🇸
 38 44 28
🇵🇹
 44 37 36 
🇬🇷
 42 44 8
🇸🇪
 36 35 28
🇩🇰
 36 26 26
🇫🇮
 23 21 18
🇦🇹
33 29 21
🇳🇱
29 21 6
🇧🇪
 20 21 16
🇮🇪
 10 10 7"""
 
sdp = sdp.split('\n')
sdp = sdp[1:]
sdp = [i.strip() for i in sdp]
sdp = pd.DataFrame(
        index=sdp[0::2],
        data=[i.split(" ") for i in sdp[1::2]]
        )

# Format the df
sdp.columns = ['start_century', 'start_decade', 'now']
for i in sdp.columns:
    sdp.loc[:, i] = pd.to_numeric(sdp.loc[:, i])

# https://en.wikipedia.org/wiki/Regional_Indicator_Symbol
OFFSET = ord('🇦') - ord('A')
unflag = lambda f: chr(ord(f[0])-OFFSET)+chr(ord(f[1])-OFFSET)
sdp.index = [unflag(f) for f in sdp.index]

sdp.to_csv('AmendedData\\SDPShare.csv')

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

# Spaghetti plot
num = 0
size = 4
plt.figure(figsize=(10,10))
for country in sdp.T:
    num += 1
    # Get the right subplot
    plt.subplot(size, size, num)
    # Plot all lines as a base
    for base in sdp.T:
        plt.plot(sdp.T.index, sdp.T[base], marker='',
                 color='grey', linewidth=0.6, alpha=0.3)
    # Plot the focus line
    plt.plot(sdp.T.index, sdp.T[country], marker='', color=colours[country],
             linewidth=2.4, alpha=0.9, label=country)
    # Not ticks everywhere
    if num in list(range(1, len(sdp)+1))[:-size] :
        plt.tick_params(labelbottom='off')
    plt.xticks(rotation=70)
    if num not in range(1,size**2, size):
        plt.tick_params(labelleft='off')
    # Add title
    plt.title(country, loc='left', fontsize=12,
              fontweight=3, color=colours[country])
    plt.gca().set_yticklabels(['{:.0f}%'.format(x) for x in plt.gca().get_yticks()])
sdp_ttl = "Social democratic party vote %s\n in latest legislative election"
plt.suptitle(sdp_ttl, fontsize=20, color='black')
plt.savefig('Outputs\\SDPShare.png')