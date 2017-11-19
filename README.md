# Automazione-plotting-serie-a
> **ATTENZIONE** Il programma potrebbe non essere ancora in grado di installare tutte le dipendenze
## Utilizzo programma (solo Linux/macOS al momento)
Usere cd per navigare alla cartella in cui avete clonato la repository
```shell
./plot.sh installa
```
installa le dipendenze per usare il programma
```shell
./plot.sh genera
```
genera le immagini png con i grafici aggiornati all'ultima giornata che consideriamo.
Invece
```shell
./plot.sh genera nonscaricare
```
Genera le immagini con i grafici con i dati nel csvs/dati.csv già scaricato o creato in precedenza (utile per accelerare la generazione di grafici se li eliminate o dopo un aggiornamento del programma ma non dell'API da cui prende i dati)
