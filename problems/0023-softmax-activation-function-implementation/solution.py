import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    ans=[]
    total=0
    max_score=max(scores)
    for i in range(len(scores)):
        total+=math.exp(scores[i]-max_score)
    for i in range(len(scores)):
        ans.append(math.exp(scores[i]-max_score)/total)
    return ans
    pass