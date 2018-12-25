import inspect

def __Title__(title) :
    print("\n")
    print("###################################")
    print("## ", title)
    print("###################################")

def __print__(var) :
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    name = [var_name for var_name, var_val in callers_local_vars if var_val is var]
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

__Title__("2.2 단방향 리스트에서 뒤에서 N번째 원소")
