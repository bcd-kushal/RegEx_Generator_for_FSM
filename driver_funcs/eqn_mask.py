
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

