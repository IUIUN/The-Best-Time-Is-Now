def link(s1, s2, s3):
    res = []
    if helper(s1, s2):
        res.append(s1)
    
def helper(s1, s2):
    if len(s1) > len(s2):
        return helper(s2, s1)
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return True
        elif s1[i] > s2[i]:
            return False
        else:
            continue
    return 