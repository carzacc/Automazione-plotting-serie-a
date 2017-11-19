#!/usr/bin/env python

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("csvs/dati.csv")
print (df)

y = df['Tradizionale']
x = df['Gol Subiti']
n = df['Squadra']
plt.scatter(x, y)
plt.ylabel("Punti Tradizionale")
plt.xlabel("Gol Subiti")
for i, txt in enumerate(n):
    plt.annotate(txt, (x[i], y[i]))
plt.savefig('tradizionale-subiti.png')
