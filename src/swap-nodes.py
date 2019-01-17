from collections import deque

class Node :
    def __init__(self, item):
        self.item = item
        self.r = None
        self.l = None

    def right(self, right):
        if right.item != -1 :
            self.r = right

    def left(self, left):
        if left.item != -1 :
            self.l = left

class Tree :
    def __init__(self, indexes):
        self.root = Node(1)
        q = deque()
        q.append(self.root)

        for datas in indexes :
            left = Node(datas[0])
            right = Node(datas[1])

            curNode = q.popleft()
            curNode.left(left)
            curNode.right(right)

            if left.item != -1 :
                q.append(left)
            if right.item != -1 :
                q.append(right)

    def getNodesByDepth(self, depth) :
        list = []
        self.__getNodesByDepth(self.root, 1, depth, list)
        return list

    def __getNodesByDepth(self, n, curDepth, targetDepth, list) :
        if n.l != None :
            self.__getNodesByDepth(n.l, curDepth + 1, targetDepth, list)
        if n.item != None and curDepth % targetDepth == 0 :
            list.append(n)
        if n.r != None :
            self.__getNodesByDepth(n.r, curDepth + 1, targetDepth, list)

    def toList(self) :
        list = []
        self.__toList(self.root, list)
        return list

    def __toList(self, n, list) :
        if n.l != None :
            self.__toList(n.l, list)
        if n.item != None :
            list.append(n.item)
        if n.r != None :
            self.__toList(n.r, list)
        return list

def swapNodes(indexes, queries):
    tree = Tree(indexes)

    result = []
    for depth in queries :
        nodes = tree.getNodesByDepth(depth)
        for node in nodes :
            tmp = node.r
            node.r = node.l
            node.l = tmp
        result.append(tree.toList())
    return result

print(swapNodes([[-1,-1]], [1,1]))
#print(swapNodes([[2,3], [-1,-1], [-1,-1]], [1,1]))
#print(swapNodes([[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]], [2, 1]))
print(swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2,4]))