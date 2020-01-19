def buildSequences(string):
    res = [""]  # init for appending single char
    for char in string:
        # res += [r + char for r in res] # this line is same as below
        addition = []   # for extending substring
        for existing_str in res:
            addition.append(existing_str + char)
        res = res + addition
    res.remove("")
    res.sort()
    return res


print("################## buildSequences ########################")
print( buildSequences("abc"))
print( buildSequences("ebda"))
