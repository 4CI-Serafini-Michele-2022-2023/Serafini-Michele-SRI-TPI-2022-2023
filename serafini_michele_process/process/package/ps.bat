@echo off

set "programma=ps.py"

if exist "%programma%" (
  python "%programma%"
) else (
  echo Il programma "%programma%" non è stato trovato.
)