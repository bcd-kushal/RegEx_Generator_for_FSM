from utils.syntax_check import syntaxChecker


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
        