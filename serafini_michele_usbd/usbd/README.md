# Controllo USB


![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)


## Descrizione

In questo progetto useremo i dati del programma `USBDview.exe` che tiene traccia di tutti i dispositivi USB connessi e tiene anche lo storico di essi, in ambito sicurezza (`SIEM`) questo software è importante perchè grazie ad esso potrò monitorare tutti i dispositivi USB connessi al computer, quindi se nel computer ci fosse un virus, i dispositivi USB saranno una delle prime cose da controllare per capire la provenienza della minaccia (per evitare il tutto sarebbe meglio utilizzare solo chiavette USB registrate nel pc oppure non utilizzarle proprio).
Per fare questo progetto ci sono più step, il primo è creare lo script .bat che prima esegue il programma USBDview.exe mettendo in un file csv chiamato 'nome_macchina'_usbd.csv tutti i dispositivi USB con le loro proprietà (il comando è: `START USBDeview.exe /scomma 'percorso_del_file'/'nomefile'.csv`) e poi avvia il programma python.
Il programma python invece, deve controllare tutto il file csv, prendere gli attributi più importanti e salvarli in un altro file csv aggiungendo anche il timestamp che segna l'ora in cui viene eseguito il file python.

## Requisiti

python

## Esecuzione

Andare nella cartella package del deploy ed eseguire il file .bat

## Tags

python, csv, windows, usb, librerie, standard


## Author

Serafini Michele