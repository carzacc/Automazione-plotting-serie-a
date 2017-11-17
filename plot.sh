#!/bin/bash
if command -v python &>/dev/null; then
    echo "Python è installato, proseguo...";
    python=1;
else
    echo "Devi installare python";
    python=0;
fi

if command -v pip &>/dev/null; then
    echo "Pip è installato, proseguo..."
    pip=1;
else
    echo "Devi installare pip (PyPi)"
    pip=0;
fi

if [ "$1" == "installa" ] ; then
  cd request;
  npm install;
  sudo apt install pip || sudo easy_install pip;
  sudo pip install pipenv;
  if [ $python == 1 ] && [ $pip == 1 ] ; then
    echo "Dipendenze installate!\nAvvia il programma con\n\t ./plot.sh genera\n, se non funziona segnala il problema a \n https://github.com/carzacc/Automazione-plotting-serie-a/issues"
  fi
fi
if [ "$1" == "genera" ] ; then
  echo "Sto prendendo i dati..."
  mkdir csvs;
  node request/get;
  echo "Sto generando le immagini..."
  pipenv run python makeplots/alternativa-fatti.py;
  pipenv run python makeplots/alternativa-subiti.py;
  pipenv run python makeplots/tradizionale-fatti.py;
  pipenv run python makeplots/tradizionale-subiti.py;
  echo "Fatto!"
fi
