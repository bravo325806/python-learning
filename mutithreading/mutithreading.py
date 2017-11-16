import time,threading
print('start of program.')

def tackANap():
    time.sleep(5)
    print('wack up!')

#新的執行緒呼叫 tackANap()
threadObj = threading.Thread(target = tackANap)# NOT tackANap() !

#執行新的執行緒
threadObj.start()
print('END OF PROGRAM')