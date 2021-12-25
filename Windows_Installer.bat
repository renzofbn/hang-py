@echo off
Title Hang-py installer
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
cd %HOMEDRIVE%\ && if not exist "Games\" mkdir Games
cd Games && git clone https://github.com/Renzofbn/hang-py.git && cd hang-py && copy hangpy.bat %windir%\System32 && exit