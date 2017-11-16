#!/bin/bash
if command -v python &>/dev/null; then
    echo "Python è installato, proseguo..."
else
    echo "Devi installare python"
fi

if command -v pip &>/dev/null; then
    echo "Pip è installato, proseguo..."
else
    echo "Devi installare pip (PyPi)"
fi

if [ "$1" == "installa" ] ; then
  cd request;
  npm install;
  cd ../makeplots;
  pip install virtualenv --user;
  virtualenv venv;
  source venv/bin/activate;
  pip install -r req.txt;
fi
if [ "$1" == "genera" ] ; then
  node request/get;
  source makeplots/venv/bin/activate;
  python makeplots/alternativa-fatti.py;
  python makeplots/alternativa-subiti.py;
  python makeplots/tradizionale-fatti.py;
  python makeplots/tradizionale-subiti.py;
fi
