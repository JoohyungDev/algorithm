def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if '#' == wallpaper[i][j] and len(answer)==0:
                answer.append(i), answer.append(j), answer.append(i), answer.append(j)
            if '#' == wallpaper[i][j] and answer[0] > i:
                answer[0] = i
            if '#' == wallpaper[i][j] and answer[1] > j:
                answer[1] = j
            if '#' == wallpaper[i][j] and answer[2] < i+1:
                answer[2] = i+1
            if '#' == wallpaper[i][j] and answer[3] < j+1:
                answer[3] = j+1
    return answer