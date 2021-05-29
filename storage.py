class Node():
    id = int(0)

    def __init__(self, id, begin, length):
        self.id = id
        self.begin = begin
        self.length = length
        self.end=self.begin+self.length-1 #末址
        Node.id += 1


class Storage():
    def __init__(self):
        self.length = 10000
        self.store = [0 for x in range(0, self.length)]
        self.full = []
        self.empty = []
        self.empty.append(Node(Node.id, 0, self.length))

    def allocate(self, begin, length):
        if length <= 0 or length > self.length or begin < 0 or begin >= self.length or begin + length > self.length:
            return False
        flag = False
        for i in range(len(self.empty)):
            if begin >= self.empty[i].begin and length <= self.empty[i].length and begin<self.empty[i].length:
                flag = True
                a = Node(Node.id, self.empty[i].begin, begin - self.empty[i].begin)
                b = Node(Node.id, begin + length, self.empty[i].length - (begin + length-self.empty[i].begin))
                print(a.id,a.begin,a.end,a.length)
                print(b.id,b.begin,b.end,b.length)
                self.full.append(Node(Node.id, begin, length))
                self.empty.pop(i)
                sign = False
                if a.length != 0:
                    sign = True
                    self.empty.insert(i, a)
                if sign:
                    i = i + 1
                if b.length != 0:
                    self.empty.insert(i, b)
                break
        return flag

    def recycle(self, id):
        flag = False
        t = 0
        for j in self.full:
            print(j.id, j.begin, j.length)
        for i in range(len(self.full)):
            #print(self.full[i].id)
            if self.full[i].id == id:
                flag = True
                print("hello")
                self.empty.append(self.full[i])
                t = self.full[i].id
                self.full.pop(i)
                break
        self.empty.sort(key=self.getBegin, reverse=False)
        for i in range(len(self.empty)):
            if self.empty[i].id == t:
                print(i)
                a = self.empty[i - 1]
                b = self.empty[i]
                c = self.empty[i + 1]
                d = Node(Node.id, a.begin, a.length + b.length)
                e = Node(Node.id, b.begin, b.length + c.length)
                f = Node(Node.id, a.begin, a.length + b.length + c.length)
                f1 = False
                f2 = False
                if a.begin + a.length == b.begin:
                    f1 = True
                if b.begin + b.length == c.begin:
                    f2 = True
                if not f1 and not f2:
                    return False
                elif not f1 and f2:
                    del self.empty[i:i+2]
                    self.empty.insert(i, e)
                elif f1 and not f2:
                    del self.empty[i - 1:i+1]
                    self.empty.insert(i - 1, d)
                else:
                    del self.empty[i - 1:i+2]
                    self.empty.insert(i - 1, f)
                flag = True
                break
        return flag

    def getBegin(self, a: Node) -> int:
        return a.begin
