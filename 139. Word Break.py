
def wordBreak(s, wordDict):
    return dfs(s, wordDict)
def dfs(s, wordDict):
    for word in wordDict:
        if not s:
            return True
        elif s.startswith(word):
            return dfs(s[len(word):], wordDict)
        
        continue
    return False
if __name__ == "__main__":
    s = "cars"
    wordDict = ["car","ca","rs"]
    print(wordBreak(s, wordDict))