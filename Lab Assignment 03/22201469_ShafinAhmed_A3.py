#22201469_Shafin Ahmed
def utility_score(gene,target,weights):
    neo=max(len(gene),len(target))
    score=0
    for i in range(neo):
        wi=weights[i] if i<len(weights) else 1
        gi=ord(gene[i]) if i<len(gene) else 0
        ti=ord(target[i]) if i < len(target) else 0
        score-=wi*abs(gi-ti)
    return score

def minimax(pool,target,weights,maximizing,alpha,beta,sequence):
  if len(pool)==0:
    return utility_score(sequence, target, weights), sequence
  
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

pool=input().strip().split(",")
target=input().strip()
sid=list(map(int,input().strip().split()))
weights = sid[-len(target):]

a,b=minimax(pool,target,weights,True,float('-inf'),float('inf'), "")
#using thr 4th parameter to decide if its a maximum state or a minimum state
print("Best gene sequence generated:",a)
print("Utility score:",b)
