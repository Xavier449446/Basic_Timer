import threading
import time
def gfg(): 
    print("Abhishek\n") 
while True:  
    timer = threading.Timer(0.5, gfg)
    timer.start()
    time.sleep(0.6)
    timer.cancel()

print("Hi SIr")