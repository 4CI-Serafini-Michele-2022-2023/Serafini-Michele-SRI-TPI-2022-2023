@echo off

set "programma=kill_process.py"

if exist "%programma%" (
  python "%programma%"
) else (
  echo Il programma "%programma%" non è stato trovato.
)