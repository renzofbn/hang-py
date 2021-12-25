@echo off
Title Hang-py installer
cd %HOMEDRIVE%\ && if not exist "Games\" mkdir Games
cd Games && git clone https://github.com/Renzofbn/hang-py.git && cd hang-py && copy hangpy.bat %windir%\System32