


import multiprocessing




def startJarvis():
    print("process 1 is running")
    from main import start
    start()
def listenHotWord():
    print("process2 is running")
    from  engine.feature import hotword
    hotword()
    

if __name__=='__main__':
    p1=multiprocessing.Process(target=startJarvis)
    p2=multiprocessing.Process(target=listenHotWord)

    p1.start()
    # subprocess.call([r'device.bat'])
    p2.start()

    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join()
   
    print("system stop")