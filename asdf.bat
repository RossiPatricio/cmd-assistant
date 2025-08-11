@echo off
REM Activar entorno virtual
call "C:\Users\PRossi\code\.programming\.PROJECTS\7- cmd-assistant\cmd-assistant\.env\Scripts\activate.bat"

REM Cambiar a la carpeta del proyecto
cd /d "C:\Users\PRossi\code\.programming\.PROJECTS\7- cmd-assistant\cmd-assistant"

REM Ejecutar el script Python
python main.py
pause

