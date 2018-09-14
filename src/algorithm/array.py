import math

###################################
##  1.2 같은 순열인지 확인하는 함수
###################################
def hasSameChars(a, b) :
    listA = dic_v2(a)
    listB = dic_v2(b)
    if listA == listB : return True
    else : return False

## O(n^2)
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

###################################
## 1.3 모든 공백을 %20로 변경하는 함수
###################################
def replaceSpace(str) :
    list = []
    for ch in str :
        if (ch == ' ' or ch == '\t') :
            list.append("%20")
        else :
            list.append(ch)
    return ''.join(list)

print(replaceSpace("Hello   World!"))

###################################
## 1.4 회문의 순열인지 확인하는 함수
###################################
## O(n^2)
def isPalindrome(str) :
    map = {}
    for ch in str :
        if (map.get(ch) is None) : map[ch] = 1
        else : map[ch] = map.get(ch) + 1

    oddCount = 0
    for k in map.keys() :
        if (map.get(k) % 2 != 0) :
            if (oddCount > 0) : return False
            else : oddCount += 1
    return True

print(isPalindrome("aaaaoo"))
print(isPalindrome("aaacccoo"))

###################################
## 1.5 수정 횟수가 1회 이내인지 확인하는 함수
###################################
def getModifyCount(str1, str2) :
    idx1 = 0
    idx2 = 0
    if (str1[idx1] == str2[idx2]) :
        idx1 += 1
        idx2 += 1

