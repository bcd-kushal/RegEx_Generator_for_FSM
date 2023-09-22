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





from utils import arr_to_string.arrToStr, remove_extra_spaces.formalities
from driver_funcs import ardens.ardens, eqn_mask.convertToOurEqns
from globals.global import null_state,






#================================================================

# =============================================================================
# ======= Convert user input equations to code understanding equations ========
# =============================================================================


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