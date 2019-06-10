def List_Sort_Same(klist=[],r=True):
    """klist = list , r = mode True"""
    rlist=[]
    clist=list(set(klist))
    for i in range(len(clist)):
        clist[i]=[klist.count(clist[i]), clist[i]]
    clist.sort(reverse=r)
    for i in range(len(clist)):
        rlist+=[clist[i][1]]*int(clist[i][0])
    return rlist
    
    
def List_to_Str(Keylist=[],mode=0):
    """Keylist = list ,mode=0&1 null&\n"""
    if mode ==0:
        Resulttextstr=""
        for i in range(len(Keylist)):
            Resulttextstr+=Keylist[i]
        return Resulttextstr
    else:
        Resulttextstr=""
        for i in range(len(Keylist)):
            Resulttextstr+=Keylist[i]+"\n"
        return Resulttextstr
if __name__ == "__main__":
    pass