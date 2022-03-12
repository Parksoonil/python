def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i], i])
        else:
            dic[genres[i]] = [[plays[i], i]]
    total_plays = {}
    for genre in dic.keys():
        play = dic[genre]
        plays_sum = 0
        for i in play:
            plays_sum += i[0]
        total_plays[genre] = plays_sum
    total_plays = sorted(total_plays.items(),\
                         key = lambda x: x[1],reverse=True)
    for genre in total_plays:
        song_rank = sorted(dic[genre[0]],\
                          key = lambda x: (-x[0], x[1]))
        best = 0
        for song in song_rank:
            answer.append(song[1])
            best += 1
            if best == 2:
                break
    
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key = lambda x: sum(\
                    map(lambda y : y[0], d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key= lambda x:\
                        (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp), 2)]
    return answer
print(solution2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
