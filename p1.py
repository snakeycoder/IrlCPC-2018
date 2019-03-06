def toExec():
    N = int(input())
    a = list(map(int,input().split()))

    print(organizer(sorted(a))[:-3])

def organizer(aSorted):
    #print(str(aSorted[0]),aSorted)
    if len(aSorted)==1:
        return(str(aSorted[0]))
    if aSorted==[]:
        return()
    print(organizer(aSorted[1:-1]), aSorted[1:-1], aSorted)
    return(str(aSorted[0])+' '+str(aSorted[-1])+' '+str(organizer(aSorted[1:-1])))
