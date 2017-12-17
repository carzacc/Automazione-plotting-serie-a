#!/usr/bin/env python

from matplotlib import pyplot as plt
import pandas as pd
import requests
linkbase = 'http://algorest.carzacc.info/?g='

for giornatacorrente in range(4,15):
    r = requests.get(linkbase+str(giornatacorrente)).json()
    print(r)
df # dove prende i dati

y = df['Alternativa']
x = df['Gol Subiti']
n = df['Squadra']
plt.scatter(x, y)
plt.ylabel("Punti Alternativa")
plt.xlabel("Gol Subiti")
for i, txt in enumerate(n):
    plt.annotate(txt, (x[i], y[i]))
plt.savefig('alternativa-subiti.png')
