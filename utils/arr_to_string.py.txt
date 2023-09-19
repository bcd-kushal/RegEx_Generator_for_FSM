def arrToStr(array):
    if len(array)==0:
        return ""
    return array[0]+(arrToStr(array[1:]) if len(array)>1 else "")

