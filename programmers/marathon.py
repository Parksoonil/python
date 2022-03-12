def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    for comp in completion:
        sumHash -= hash(comp)
        
    return hashDict[sumHash]
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution2(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
