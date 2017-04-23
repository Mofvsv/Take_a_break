import time
import webbrowser

total_breaks = 3
break_counter = 0

print("This program started on" + time.ctime() )
while(break_counter < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/")
    break_counter = break_counter + 1
