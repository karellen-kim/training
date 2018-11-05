import math

print("""
###################################
##  1.2 같은 순열인지 확인하는 함수
###################################
""")
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

print("""
###################################
## 1.3 모든 공백을 %20로 변경하는 함수
###################################
""")
def replaceSpace(str) :
    list = []
    for ch in str :
        if (ch == ' ' or ch == '\t') :
            list.append("%20")
        else :
            list.append(ch)
    return ''.join(list)

print(replaceSpace("Hello   World!"))

print("""
###################################
## 1.4 회문의 순열인지 확인하는 함수
###################################
""")
## O(n^2)
def isPalindrome(str) :
    map = {}
    for ch in str :
        if (map.get(ch) is None) : map[ch] = 1
        else : map[ch] = map.get(ch) + 1

    for k in map.keys() :
        if (map.get(k) % 2 != 0) :
            return False
    return True

## 성능을 높여보자
def isPalindrome_v2(str) :
    array = [0] * getCharIndex('z')
    for ch in str :
        array[getCharIndex(ch)] = array[getCharIndex(ch)] + 1

    for k in array :
        if k % 2 != 0 :
            return False
    return True

## for 문을 줄여보자
def isPalindrome_v3(str) :
    odd = 0
    array = [0] * getCharIndex('z')
    for ch in str :
        array[getCharIndex(ch)] = array[getCharIndex(ch)] + 1
        if array[getCharIndex(ch)] % 2 != 0 :
            odd = odd + 1
        else :
            odd = odd - 1
    return odd <= 1

def getCharIndex(ch) :
    return ord(ch) - ord('a')

print(isPalindrome_v3("aaaaoo"))
print(isPalindrome_v3("aaacccoo"))

print("""
###################################
## 1.5 수정 횟수가 1회 이내인지 확인하는 함수
###################################
""")
def diff(str1, str2)