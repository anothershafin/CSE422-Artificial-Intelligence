pool=input().strip().split(",")
target=input().strip()
sid=list(map(int,input().strip().split()))
weights = sid[-len(target):]
print(pool,target,sid,weights)
