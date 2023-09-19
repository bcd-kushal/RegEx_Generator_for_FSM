

from utils.remove_extra_spaces import formalities


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
    