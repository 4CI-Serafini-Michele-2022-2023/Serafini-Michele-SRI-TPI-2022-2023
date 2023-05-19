#!/bin/sh
read -p "Inserisci il nome del pacchetto: " nome
mkdir serafini_michele_"$nome"
cd serafini_michele_"$nome"
mkdir "$nome"
cd "$nome"
mkdir flussi
mkdir package
mkdir log
cp home/Serafini-Michele-SRI-TPI-2022-2023/Work/README.md
cp home/Serafini-Michele-SRI-TPI-2022-2023/Work/CHANGELOG.txt
