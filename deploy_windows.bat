@ECHO ON
SET/p "nome=inserisci il nome del pacchetto  "
MKDIR serafini_michele_%nome%
CD serafini_michele_%nome%
MKDIR %nome%
CD %nome%
MKDIR flussi
MKDIR package
MKDIR log
COPY C:\Work\documentazione\README.md
COPY C:\Work\documentazione\CHANGELOG.txt