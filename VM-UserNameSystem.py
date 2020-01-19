1   Usernames System
create the username portion of a registration sys that requires all usernames are unique.

#输入list：[bob, alice, bob, alice,bob] 输出：[bob,alice,bob1,alice1,bob2]

def usernamesSystem(inputList):
uniqueNameMap = {} # map name to curr number
resList = []
for name in inputList:
  if name not in uniqueNameMap:
   uniqueNameMap[name] = 0
  else:
   uniqueNameMap[name] += 1
   name = name + str(uniqueNameMap[name])

  resList.append(name)
return resList

print("################## usernamesSystem ########################")
print(usernamesSystem(["bob", "alice", "bob", "alice", "bob"]))
