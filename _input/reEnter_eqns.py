
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

