import threading,time
def Multithreading_Run(function=[],functionkey=[]):
    """function : which function(def) need to run ,must be a list
    functionkey : key of function,must be a bivariate table"""
    subthreadinglist=[""]*len(function)
    
    i=0
    while i < len(subthreadinglist):
        subthreadinglist[i] = threading.Thread(target=function[i], args=functionkey[i])
        i+=1
    for i in subthreadinglist:
        i.start()
    return subthreadinglist
    
def Delay_Threading_To_Exit(subthreadinglist=[],Delaytime=0,tips=False):
    """subthreadinglist: which list of need to delay
    Delaytime: Delay seconds
    tips: True to print Finished in the end """
    i=0
    while i<len(subthreadinglist):
        if subthreadinglist[i].is_alive():
            time.sleep(Delaytime)
        else:
            i+=1
    if tips:
        print("Finished")
    return True
    
def Check_Threading_isalive(subthreadinglist=[]):
    """subthreadinglist: which need to check """
    threadingstatus=[]
    for i in subthreadinglist:
        if i.is_alive():
            threadingstatus+=[True]
        else:
            threadingstatus+=[False]
    return threadingstatus

def BackgroundRunTask(function,**argv):
    """Run a threading in background. 
    you can start it with ".start()" """
    return threading.Thread(target=function, args=argv)

def BackgroundRunTask(function,**argv):
    """Run a threading in background now."""
    threading.Thread(target=function, args=argv).start()

if __name__ == "__main__":
    pass