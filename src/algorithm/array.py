import math
## 같은 순열인지 확인
def hasSameChars(a, b) :
    listA = dic_v2(a)
    listB = dic_v2(b)
    print(listA, listB)
    if listA == listB : return True
    else : return False

def dic_v1(str) :
    map = {}
    for c in list(str) :
        map[ord(c)] = c
    return map

## 공간 효율성을 높여보자
def dic_v2(str) :
    map = 0
    for c in list(str) :
        map = map | int(math.pow(2, ord(c)))
    return map

print(hasSameChars("abba", "baaa"))
print(hasSameChars("abba", "baacca"))