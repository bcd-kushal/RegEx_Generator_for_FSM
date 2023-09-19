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
