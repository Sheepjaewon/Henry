@echo off
:A
set /a x= %random% %% 10
set /a y= %random% %% 10

color %x%%y%

goto A
