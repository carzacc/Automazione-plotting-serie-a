#!/usr/bin/env python

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("csvs/dati.csv")
print (df)

y = df['Alternativa']
x = df['Gol Fatti']
plt.scatter(x, y)
plt.ylabel("Punti Alternativa")
plt.xlabel("Gol Fatti")
plt.savefig('alternativa-fatti.png')
