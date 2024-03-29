#нумерация списка начинается с единицы, список однонаправленный
class Node: # звено
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkList: # список
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def __str__ (self): 
        if self.first != None:
            current = self.first
            out = 'LinkList [ ' + str(current.value)
            while current.next != None:
                out = out + ', '
                current = current.next
                out = out + str(current.value)
            out = out + ' ]'
            return out
        return 'LinkList []'
    def clear(self): 
            self.__init__()
    def add(self, x, y): #добавление звена на любую позицию, x - значение,y - позиция 
        self.length = self.length + 1
        if self.first == None:
            self.last = self.first = Node (x, None)
            return
        elif y == 1:
            self.first = Node(x, self.first)
            return
        current = self.first
        count = 0
        if 1 < y < self.length:
            while current != None:
                count +=1
                if count + 1 == y:
                    current.next = Node(x, current.next)
                    break
                current = current.next
        elif y == -1: # у = -1 признак того, что звено надо добавлять в конец
            self.last.next = self.last = Node(x, None)
        else : 
            self.last.next = self.last = Node(x, None)
    def dele(self, y): #удаление звена с любой позиции
        if self.first == None:
            return
        self.length = self.length - 1
        current = self.first
        if y == 1:
            self.first = current.next
            return
        elif y <= self.length + 1:
            count = 0
            precur = current
            while current != None:
                count +=1
                if count == y and y != self.length + 1:
                    precur.next = current.next
                elif count == self.length + 1:
                    self.last = precur
                    precur.next = None
                    break
                precur = current
                current = current.next
    def searc (self, x): #поиск первого вхождения 
        if self.first == None:
            return None
        current = self.first
        while current != None:
            if current.value == x:
                return current
            current = current.next

#примеры для проверки функций

#l = LinkList()
#l.add(1,9)
#l.add(2,8)
#l.add(1,2)
#l.add(2,2)
#print(l)
#l.searc(2).value = 0
#l.searc(2).value = 3
##print(l)
#l.dele(4)
#print(l)
#l.add(6,2)
#l.dele(1)
#print(l)
