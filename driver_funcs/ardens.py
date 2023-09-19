#===================[ ARDENS METHOD ]================================


def ardens(x,mode=False):
    formalities(x)
    str=x   #work with a copy
    P=str[0]
    R=Q=""
    if str[2]==P:
        R+=getCompanion(str,2)
    else:
        Q+=getCompanion(str,2,mode=False)
    str=getCompanion(str, 2,nextPart=True)
    while str!="":
        if str[0]==P:
            R+=getCompanion(str,0) if R=="" else "+"+getCompanion(str,0)
        else:
            Q+=getCompanion(str,0,mode=False) if Q=="" else "+"+getCompanion(str,0,mode=False)
        str=getCompanion(str, 0,nextPart=True)
        
    #somehow R gets a dual "++" in its expression at times so correcting it:
    while "++" in Q:
        Q=Q.replace("++","+")
    if Q[0]=="+":
        Q=Q[1:]
    if Q[len(Q)-1]=="+":
        Q=Q[:len(Q)-1]
        
    # print("P: "+P)
    # print("R: "+R)
    # print("Q: "+Q)
        
    #-----[ P=Q+PR => P=QR* ]------------------
    
    if mode is True:
        return {"P":P,"Q":Q,"R":R}
    
    if "+" in Q and len(R)>0:
        Q="("+Q+")"
    if len(R)>1:
        R="("+R+")*" 
    elif len(R)==1:
        R+="*"
        
    
    print("RE:"+x)
    print("=> "+P+"="+Q+R)
    if Q==null_state:
        print("=> "+P+"="+R)
    
    return P+"="+Q+R if Q!=null_state else P+"="+R
