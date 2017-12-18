#!/usr/bin/env python

import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import requests
from numpy import nditer


linkbase = 'http://algorest.carzacc.info/?g='
giornate = []
puntinter = []
puntijuve = []
puntinapoli = []
puntimilan = []
puntichievo = []
puntibenevento = []
puntiverona = []
puntiroma = []
puntilazio = []
puntisampdoria = []
puntiudinese = []
puntibologna = []
puntigenoa = []
puntiatalanta = []
puntifiorentina = []
puntispal = []
puntitorino = []
puntisassuolo = []
punticrotone = []
punticagliari = []

for giornatacorrente in range(4,16):
    r = requests.get(linkbase+str(giornatacorrente)).json()
    giornate.append(r)

for giornata in range(0,12):
    for squadra in range(0,20):
        if giornate[giornata][squadra]['Squadra']=='Inter':
            puntinter.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='juventus':
            puntijuve.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Napoli':
            puntinapoli.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Milan':
            puntimilan.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Chievo':
            puntichievo.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Cagliari':
            punticagliari.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Crotone':
            punticrotone.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Sassuolo':
            puntisassuolo.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Torino':
            puntitorino.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Spal':
            puntispal.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Genoa':
            puntigenoa.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Atalanta':
            puntiatalanta.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Verona':
            puntiverona.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Roma':
            puntiroma.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Lazio':
            puntilazio.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Sampdoria':
            puntisampdoria.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Udinese':
            puntiudinese.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Bologna':
            puntibologna.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Fiorentina':
            puntifiorentina.append(giornate[giornata][squadra]['Tradizionale'])
        if giornate[giornata][squadra]['Squadra']=='Benevento':
            puntibenevento.append(giornate[giornata][squadra]['Tradizionale'])
punti = [
    puntinter,
    puntijuve,
    puntinapoli,
    puntiatalanta,
    puntilazio,
    puntimilan,
    puntiroma,
    puntisampdoria,
]
squadre = [
    "Inter",
    "Juve",
    "Napoli",
    "Atalanta",
    "Lazio",
    "Milan",
    "Roma",
    "Sampdoria",
]
for c in range(0,7):
    elemento=punti[c]
    y = elemento
    x = range(4,16)
    n = squadre
    plt.plot(x, y, label=squadre[c])

plt.ylabel("Punti")
plt.xlabel("Giornate")
plt.legend()
plt.savefig('puntisutempo.png')