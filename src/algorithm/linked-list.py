import inspect

def __Title__(title) :
    print("\n")
    print("###################################")
    print("## ", title)
    print("###################################")

def __print__(var) :
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    name = [var_name for var_name, var_val in callers_local_vars if var_val is var]
    if len(name) == 0 :
        print(var)
    else :
        print("%s = %s" % (name[0], str(var)))


__Title__("2.1 연결리스트 중복없애기")
class Node :
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class LinkedList :
    def __init__(self, list = []):
        self.top = None
        for item in list :
            node = Node(item)
            self.append(node)

    def append(self, item) :
        if self.top == None :
            self.top = item
        else :
            cur = self.top
            prev = None
            while cur != None :
                prev = cur
                cur = cur.next
            prev.next = item
            item.prev = prev

    def remove(self, node):
        if node.prev != None :
            node.prev.next = node.next
        if node.next != None :
            node.next.prev = node.prev

    def __repr__(self):
        list = []
        cur = self.top
        while cur != None :
            list.append(cur.item)
            cur = cur.next
        return str(list)

def removeDuplicate(list) :
    uniqItems = set()

    cur = list.top
    while cur != None :
        if cur.item in uniqItems :
            list.remove(cur)
        else :
            uniqItems.add(cur.item)
        cur = cur.next
    return list

list = [1,2,3,1,5,6,7,2,1]
__print__(list)
linkedList = LinkedList(list)
__print__(removeDuplicate(linkedList)) # O(N)


__Title__("2.2 단방향 연결리스트에서 뒤에서 N번째 원소")
def getReverseAt(list, n) :
    pre = list.top
    cur = list.top

    # prefetch iterator
    count = 0
    while pre != None :
        pre = pre.next
        if count == n :
            break
        count = count + 1

    # next iterator
    while pre != None :
        cur = cur.next
        pre = pre.next

    if cur != None :
        return cur.item
    else :
        return None

list = [1,2,3,1,5,6,7,2,1]
__print__(list)
linkedList = LinkedList(list)
__print__(getReverseAt(linkedList, 2)) # O(N)

__Title__("2.3 단방향 연결리스트에서 주어진 노드 삭제 (head 알수 없음)")
def getAt(list, n) :
    cur = list.top
    idx = 1
    while cur != None :
        if idx == n :
            return cur
        cur = cur.next
        idx = idx + 1
    return None

def removeNode(node) :
    next = node.next

    if next != None :
        # 다음 노드의 값을 복사한다.
        node.item = next.item
        # node.next를 다음 노드의 next를 가리킨다
        node.next = next.next

list = [1,2,3,1,5,6,7,2,1]
__print__(list)
linkedList = LinkedList(list)
target = getAt(linkedList, 3)
__print__(target.item)
removeNode(target)
__print__(linkedList) # O(N)

__Title__("2.5 리스트가 하나의 숫자를 가리킨다고 가정할 때, 두 리스트의 합을 반환하는 리스트")
# 7->1->6, 5->9->2 617 + 295 => 912 => 2->1->9
def sumLists_v1(list1, list2) :
    sum = getNumber(list1) + getNumber(list2)
    return LinkedList(toList(sum))

def getNumber(list) : # O(3N)
    nums = []
    cur = list.top
    while cur != None :
        nums.append(str(cur.item))
        cur = cur.next
    nums.reverse()
    return int("".join(nums))

def toList(num) :
    list = [c for c in str(num)]
    list.reverse()
    return list

list1 = LinkedList([7,1,6])
list2 = LinkedList([5,9,2])
sumList = sumLists_v1(list1, list2) # O(8N)
__print__(sumList)

def sumLists_v2(list1, list2) :
    n1 = list1.top
    n2 = list2.top

    list = LinkedList()
    passNum = 0
    while n1 != None or n2 != None :
        sum = getNum(n1) + getNum(n2)
        num = (sum % 10)
        list.append(Node(num + passNum))
        passNum = int(sum / 10)
        n1 = n1.next
        n2 = n2.next
    return list

def getNum(node) :
    if node != None and node.item != None :
        return node.item
    else :
        return 0

list1 = LinkedList([7,1,6])
list2 = LinkedList([5,9,2])
sumList2 = sumLists_v2(list1, list2)
__print__(sumList2)

__Title__("2.6 주어진 연결 리스트가 회문인지 확인하는 함수")
# 0->1->2->1->0 => 회문

__Title__("2.7 값도 위치도 동일한 두 리스트의 교집합 : 마지막 노드가 같아야 함")
# 1->2->3, 2->3 교집합 (2->3)
# 1->2->3, 2->3->1 교집합 없음

__Title__("2.8 순환 연결리스트가 있을 때, 순환되는 첫째 노드는 반환하는 함수")
# A->B->C->D->E->C(앞의 C와 동일한 객체) => C