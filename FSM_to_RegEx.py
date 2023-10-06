# -*- coding: utf-8 -*-
"""
Created on Mon Aug 4 17:44:57 2022
@author: Kushal Kumar
"""

# =============================================================================
"""
user pre-cautions:
    1.enter only distinct state and transition names
    2.enter integer values when asked how many states or transitions
the code takes care of:
      1.proper RE syntax was inserted
      2.no foreign transitions or states are there in local FSM
      3.user receives and stores their own states and transitions variables, making code robust
"""

# =============================================================================
# ======>> PER DEVELOPMENT PROGRESS: 
#     4 aug: ardens method
#            method to return rest of eqn of a particular state
#     6 aug: state/transition/initial,final state inputs
#            regular expression equation inputs
#            masking of user defined equations to code executable eqns
#     7 aug: code to check proper RE syntax is maintained on the fly
#            user driven dynamicness of updation and changing FSM variables even after inputting
#            
# =============================================================================
# ======>> NEXT DEVELOPMENT PHASE WORKS:
    # - no state is left unvisited by any state in state graph of RE eqns
# =============================================================================


null_state = chr(198)  #the lambda of RE
#the next 5 variables store values of RE given by User
state=[]
transition=[]
initial_state=""
final_state=""
eqns={}
#program uses states of a,b,c,.... and 0,1,2,... transitions to be used
states='abcdefghijklmnopqrstuvwxyz'
transitions='0123456789'
#code object stores the same things but masked variations that is used by program
code={
      "eqns":{},
      "state":[],
      "transition":[],
      "initial_state":"",
      "final_state":""
      }


# =============================================================================

def arrToStr(array):
    if len(array)==0:
        return ""
    return array[0]+(arrToStr(array[1:]) if len(array)>1 else "")

# =============================================================================

def formalities(str):
    if " " in str:
        str=str.replace(" ","")
    return str

# =============================================================================

def getCompanion(str,index,mode=True,nextPart=False): 
    #mode:True get companion only, False get state attached to it also
    #nextPart:False-return companion, True-return expression ahead of companion
    formalities(str)
    totalBracesCount=0
    pos=index
    companion=""
    if str[index] in states and mode is True:
        index+=1
    for x in str[index:]:
        if x=="(":
            totalBracesCount+=1
        elif x==")":
            totalBracesCount-=1
        pos+=1
        if totalBracesCount==0 and x=="+":
            if nextPart is False:
                return companion
            else:
                return str[pos:]
        else:
            companion+=x
    if nextPart is False:
        return companion
    else:
        return ""
    
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

#================================================================

# =============================================================================
# ======= Convert user input equations to code understanding equations ========
# =============================================================================

def convertToOurEqns():
    #IMPORTANT CAUTION !!!: only convert to code eqns in base state(so it has a state at left for each sub-machine part)
    for i in range(0,len(state)):
        code["state"].append(states[i])
    for i in range(0,len(transition)):
        code["transition"].append(transitions[i])
    code["initial_state"]=states[state.index(initial_state)]
    code["final_state"]=states[state.index(final_state)]
    # Convert equations now
    for i in range(0,len(state)):
        code['eqns'].update({code['state'][i]:maskEqns(i)})
        

def maskEqns(index):         
    #the equations we will work with throughout
    #makes the program user input constraint independent
    str="="+eqns[state[index]]
    for v in range(0,len(state)):
        str=str.replace(state[v],states[v])
    flag=False
    temp_str=""
    for v in range(0,len(str)):
        if flag is True:
            temp_str+=str[v]
            flag=False
            continue
        if str[v]=='=' or str[v]=='+':
            temp_str+=str[v]
            flag=True
            continue
        temp_str+=transitions[transition.index(str[v])]
    return temp_str[1:]


# =============================================================================
# #================================= ALL INPUTS ===============================
# =============================================================================

#------------------ State Transition Inputs ---------------
def stateInput():
    global state 
    state=[]
    totalStates=int(input("=> How many total distinct states? (max 26) "))
    if totalStates>26 or totalStates<=0:
        print("[!]Max limit:26 ...enter again...") if totalStates>26 else print("[!]Atleast one state has to exist in the FSM")
        stateInput()
    anotherChoice = input("=> Do you want to name the states?\n   (by default, states are named = {"+states[:totalStates]+"}) \n   Y/N(y/n): ")
    for i in range(0,totalStates):
        state.append(input("=> State #"+"%s"%(i+1)+": ") if anotherChoice.lower()=="y" else states[i])
  
     
     
def transitionInput():
    global transition 
    transition=[]
    totalTrans=int(input("=> How many total distinct transitions? (max 9) "))
    if totalTrans>9 or totalTrans<=0:
        print("[!]Max limit:9 ...enter again...") if totalTrans>9 else print("[!]Atleast one transition has to exist in the FSM")
        transitionInput()
    anotherChoice = input("=> Do you want to name the transitions?\n   (by default, transitions are named = {"+transitions[:totalTrans]+"}) \n   Y/N(y/n): ")
    if anotherChoice.lower()=="y":
        print("=> Please enter single letter transitions only...") if anotherChoice.lower() == "y" else print("=>")
        i=0
        while i<totalTrans:
            temp_var=input("=> Transition #"+"%s"%(i+1)+": ")
            if(len(temp_var)!=1):
                print("[!]Only single digit transitions are to be input.")
                i-=1
                continue
            transition.append(temp_var)
            i+=1
    else:
            for i in range(0,totalTrans):
                transition.append(transitions[i])
                #transition.append(input("=> Transition #"+"%s"%(i+1)+": ") if anotherChoice.lower()=="y" else transitions[i])

    
#------------------ Initial Final States Input ---------------------- 
    
def initialFinalStateInput(ph,flag=False):
    print("=> Which one is "+ph+"?")
    print("=>",state) if flag is False else print("=>",state,"(previously: "+(initial_state if ph=="initial state" else final_state)+")")
    x=input("=> ")
    if x not in state:
        print("[!]"+ph+" does not exist in state set...")
        return ""+initialFinalStateInput(ph,flag)
    else:
        return x
    
#------------------ RE Eqns Input -------------------------------

def eqnInput():
    print("=> Enter state equations:")
    for x in state:
        eqns.update({x:input(x+"=") if x!=initial_state else null_state+"+"+input(x+"="+null_state+"+")})
        for y in eqns[x]:
            if y not in final_state+initial_state+null_state+"+" and y not in arrToStr(state) and y not in arrToStr(transition):
                print("[!]Improper equation inserted, re-enter correct one: ("+y+" should not exist in equation)")
                reEnterEqn(x)
                break
        #equation syntax must be: "+<one state><one transition>..."
        if checkEqnSyntax(eqns[x]) is False:
            print("[!]Incorrect Regular Expression Syntax, re-enter correct one.")
            reEnterEqn(x)
            

    
#=============================================================================

#---------------- User navigation and choices input --------------------------

def choiceInput():
    choice=int(input("=> \n=> We now enter equations\n=> Select an option: \n    1: Enter state transition table, or \n    2: Enter state equations manually \n   Whats the choice? "))
    if choice not in [1,2]:
        print("[!]Incorrect choice, choose correctly now...")
        choiceInput()
    else:
        return choice
    

def changeSomething(flag=True):
    global initial_state,final_state
    if flag is True:
        print("=>\n=> ==============[ The FSM looks like this ]==============")
        print("=>        States = ",state)
        print("=>   Transitions = ",transition)
        print("=> Initial state = ",initial_state)
        print("=>   Final state = ",final_state)
    
    choice=input("=>\n=> Do you want to change something to this? Y/N(y/n): ")
    if choice.lower()=='y':
        choice=int(input("=> What to change?\n=> 1:Initial State       2:Final State   3:Total states   \n=> 4:Total transitions   5:State names   6:Transition names\n=> "))
        if str(choice) in "123456":
            if choice==1:
                initial_state=initialFinalStateInput("initial state",flag=True)
            elif choice==2:
                final_state=initialFinalStateInput("final state",flag=True)
            elif choice==3:
                stateInput()
                print("=> States have changed so initial and final state need to be re-entered too...")
                initial_state=initialFinalStateInput("initial state",flag=True)
                final_state=initialFinalStateInput("final state",flag=True)
            elif choice==4:
                transitionInput()
            elif choice==5:
                initial_state=state.index(initial_state)
                final_state=state.index(final_state)
                for i in range(0,len(state)):
                    state[i]=input("=> State #"+"%s"%(i+1)+" (originally '"+state[i]+"'): ")
                
                initial_state=state[initial_state]
                final_state=state[final_state]
                print("=> \n\n\n=> Change: initial state = "+initial_state)
                print("=> Change:   final state = "+final_state)
            else:
                for i in range(0,len(transition)):
                    transition[i]=input("=> Transition #"+"%s"%(i+1)+" (originally '"+transition[i]+"'): ")
            return changeSomething()
        else:
            print("[!]Improper choice....")
            return changeSomething(flag=False)
    return ""
 


# =============================================================================
# ==================== VALIDATE RE EXPRESSIONS USER HAS ENTERED ===============
# =============================================================================

def reEnterEqn(x):
    eqns.update({x:input(x+"=") if x!=initial_state else null_state+"+"+input(x+"="+null_state+"+")})
    for y in eqns[x]:
        if y not in final_state+initial_state+null_state+"+" and y not in arrToStr(state) and y not in arrToStr(transition):
            print("[!]AGAIN INCORRECT: ("+y+" should not exist in equation)")
            return reEnterEqn(x)
    if checkEqnSyntax(eqns[x]) is False:
        print("[!]AGAIN INCORRECT RE Syntax, re-enter correct one.")
        return reEnterEqn(x)
    return ""


def syntaxChecker(arr,substr):
    count=0
    for t in arr:
        if t in substr:
            count+=1
            if count>1 or substr.count(t)>1:
                return [substr,False]
            substr=substr.replace(t,"")
    if count==0:
        return [substr,False]
    return [substr,True]


def checkEqnSyntax(eqn):
    eqn="+"+eqn+"+"
    #equation syntax must be: "+<one state><one transition>..."
    i=0
    substr=""
    while i!=len(eqn)-1:
        substr=eqn[(i+1):eqn.index("+",i+1)]
        i=eqn.index("+",i+1)
        # check first element is state itself only
        for v in state:
            if v in substr and substr.index(v)!=0:
                return False
        # check no multiple transition/state exist
        if substr==null_state:
            continue
        if syntaxChecker(state,substr)[1] is False:
            return False
        substr=syntaxChecker(state,substr)[0]
        if syntaxChecker(transition,substr)[1] is False:
            return False
        if syntaxChecker(transition,substr)[0]!="":
            return False
    return True
        
# =============================================================================
# ============================== THE MAIN =====================================
# =============================================================================

def main():
    global initial_state,final_state
    print("\n========================[ FSM to RE ]========================\n")
        
    stateInput()
    initial_state=initialFinalStateInput("initial state")
    final_state=initialFinalStateInput("final state")
    transitionInput()
    changeSomething()
    if choiceInput()==1:
        print("In development...\nRight now, enter equations manually...")
        eqnInput()
    else:
        eqnInput()
    convertToOurEqns()
# =============================================================================

if __name__=='__main__':
    main()

# print("q0q00".index("q0"))