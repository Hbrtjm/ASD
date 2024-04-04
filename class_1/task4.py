def containers(clist:tuple[int,int],A:int):
    length = 0
    answer = 0
    for cont in clist:
        length += cont[0][0] - cont[1][0]
    height = A / length
    for cont in clist:
        if height > cont[1][0]-cont[1][1]:
            answer+=1
    return answer
