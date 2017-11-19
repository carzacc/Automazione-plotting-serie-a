#!/usr/bin/env python

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("csvs/dati.csv")
print (df)

y = df['Alternativa']
x = df['Gol Subiti']
n = df['Squadra']
plt.scatter(x, y)
plt.ylabel("Punti Alternativa")
plt.xlabel("Gol Subiti")
for i, txt in enumerate(n):
    plt.annotate(txt, (x[i], y[i]))
plt.savefig('alternativa-subiti.png')
