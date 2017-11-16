#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

df  = pd.read_csv("dati.csv")
print (df)
# Fixing random state for reproducibility

y = df['Tradizionale']
x = df['Gol Subiti']
plt.scatter(x, y)
plt.ylabel("Punti Tradizionale")
plt.xlabel("Gol Subiti")
plt.show()
