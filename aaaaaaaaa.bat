@echo
echo msgbox "±èÀ±ÇÏ ÇÏÆ® ÀÌµ¿°Ç",0,"¤»¤»¤»¤»¤»¤»" > msg.vbs
start /wait msg.vbs
del msg.vbs
 
:_loop
start chrome https://www.youtube.com/watch?v=N-YUCwc7bCE
timeout 5 > NUL
start chrome https://www.youtube.com/watch?v=CleIGYOpj7Q
timeout 4 > NUL
start chrome https://www.youtube.com/watch?v=-8RYVIoYYp8
 
timeout 2 > NUL
 
echo msgbox "Å·¹ÞÁê",0,"o kawaii koto" > msg.vbs
start /wait msg.vbs
del msg.vbs

star dataa.dat
 
goto _loop