#22201469_Shafin Ahmed
def utility(gene,target,weights):
  neo=max(len(gene),len(target))
  score=0
  for i in range(neo):
    wi=weights[i] if i<len(weights) else 1
    gi=ord(gene[i]) if i<len(gene) else 0
    ti=ord(target[i]) if i < len(target) else 0
    score-=wi*abs(gi-ti)
  return score

#for task 2
def utility_sp(gene,target,weights,sid):
  if 'S' in gene:
    si=gene.index('S')
    factor=(sid[0]*10+sid[1])/100
    new_weights=[]
    for i in range(len(weights)):
      if i>=si:
        new_weights.append(weights[i]*factor)
      else:
        new_weights.append(weights[i])
    weights=new_weights
  return utility(gene,target,weights)

def minimax(pool,target,weights,maximizing,alpha,beta,sequence):
  if len(pool)==0:
    return utility(sequence, target, weights), sequence
  
  if maximizing:
    max_alpha=float('-inf')
    best_seq=None
    for i,n in enumerate(pool):
      eval_score,seq=minimax(pool[:i]+pool[i+1:],target,weights,False,alpha,beta,sequence+n)
      if eval_score>max_alpha:
        max_alpha=eval_score
        best_seq=seq
      alpha=max(alpha,eval_score)
      if beta<=alpha:
        break
    return max_alpha,best_seq

  else:
    min_beta=float('inf')
    best_seq=None
    for i,n in enumerate(pool):
      eval_score,seq=minimax(pool[:i]+pool[i+1:],target,weights,True,alpha,beta,sequence+n)
      if eval_score<min_beta:
        min_beta=eval_score
        best_seq=seq
      beta=min(beta,eval_score)
      if beta<=alpha:
        break
    return min_beta,best_seq

#for task 2
def minimax_sp(pool,target,weights,sid,maximizing,alpha,beta,sequence):
  if len(pool)==0:
    return utility_sp(sequence, target, weights, sid), sequence

  if maximizing:
    max_alpha=float('-inf')
    best_seq=None
    for i,n in enumerate(pool):
      eval_score,seq=minimax_sp(pool[:i]+pool[i+1:],target,weights,sid,False,alpha,beta,sequence+n)
      if eval_score>max_alpha:
        max_alpha=eval_score
        best_seq=seq
      alpha=max(alpha,eval_score)
      if beta<=alpha:
        break
    return max_alpha,best_seq
  else:
    min_beta=float('inf')
    best_seq=None
    for i,n in enumerate(pool):
      eval_score,seq=minimax_sp(pool[:i]+pool[i+1:],target,weights,sid,True,alpha,beta,sequence+n)
      if eval_score<min_beta:
        min_beta=eval_score
        best_seq=seq
      beta=min(beta,eval_score)
      if beta<=alpha:
        break
    return min_beta,best_seq


with open(filename, "r") as file:
  pool=file.readline()
  target=file.readline()
  sid=file.readline()
pool=pool.strip().split(",")
target=target.strip()
sid=list(map(int,sid.strip().split()))
weights = sid[-len(target):]

# pool=["A","T","C","G"]
# target="GCAT"
# sid=[2,3,1,8,8,8,1,1]
# weights = sid[-len(target):]

a,b=minimax(pool,target,weights,True,float('-inf'),float('inf'), "")
#using thr 4th parameter to decide if its a maximum state or a minimum state

#for task 2
new_pool=pool+["S"]
c,d=minimax_sp(new_pool,target,weights,sid,True,float('-inf'),float('inf'), "")


print("Best gene sequence generated:",b)
print("Utility score:",a)

if c>a:
    print("YES")
else:
    print("NO")
print("With special nucleotide")
print("Best gene sequence generated:",d)
print("Utility score:",round(c,2))
print("Task Finished")
