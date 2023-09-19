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
            
