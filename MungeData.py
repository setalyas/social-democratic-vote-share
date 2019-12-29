# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 01:07:28 2019

@author: setat
"""

import pandas as pd

# Data from https://twitter.com/NeilWarner_/status/1210929335458291715

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

sdp_plus = """Combined vote % of social democrats, greens & far left at \
beginning of century, beginning of decade & now:
🇬🇧
 44 37 36
🇩🇪
 53 46 41
🇮🇹
 45 36 25
🇫🇷
 48 40 28
🇪🇸
 49 49 44
🇵🇹
 56 55 54 
🇬🇷
 57 58 50
🇸🇪
 36 35 28
🇩🇰
 47 41 40
🇫🇮
 43 39 38
🇦🇹
53 47 37
🇳🇱
40 43 27
🇧🇪
 34 31 36
🇮🇪
 19 23 32"""

splits = {'SDP': sdp, 'SDPPlus': sdp_plus}
 
for k, data in splits.items():
    data = data.split('\n')
    data = data[1:]
    data = [i.strip() for i in data]
    data = pd.DataFrame(
            index=data[0::2],
            data=[i.split(" ") for i in data[1::2]]
            )
    
    # Format the df
    data.columns = ['start_century', 'start_decade', 'now']
    for i in data.columns:
        data.loc[:, i] = pd.to_numeric(data.loc[:, i])
    
    # https://en.wikipedia.org/wiki/Regional_Indicator_Symbol
    OFFSET = ord('🇦') - ord('A')
    unflag = lambda f: chr(ord(f[0])-OFFSET)+chr(ord(f[1])-OFFSET)
    data.index = [unflag(f) for f in data.index]
    print(data)
    data.to_csv('AmendedData\\' + k + 'Share.csv')