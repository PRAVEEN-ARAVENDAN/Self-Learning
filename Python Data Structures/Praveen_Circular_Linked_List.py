'''
CIRCULAR LINKED LIST

l :- Linked list
a,b,c :- Nodes
n :- Node that needs to be inserted or deleted

traversal(l) :- Also displays the Linked List along with traversal
insert_after(n, a)
insert_at_last(l, n)
delete(l, n) :- n will be deleted

Note :-

A Circular Linked List is just a simple linked list with the next pointer of the last node of a linked list connected to the first node.

'''

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self, key):
    z = Node(key)
    z.next = z
    self.last = z

def insert_after(n, a):
  n.next = a.next
  a.next = n

def insert_at_last(l, n):
  n.next = l.last.next
  l.last.next = n
  l.last = n

def delete(l, n):
  temp = l.last
  while temp.next != n:
    temp = temp.next

  if n == l.last: #last node
    if n.next == n: #only one node
      l.last = None
    else: #more than one node and last node
      temp.next = n.next
      l.last = temp #updating last pointer
  else: #not last node
    temp.next = n.next
  del n

def traversal(l):
  temp = l.last
  a = str(temp.data)+"\t"
  temp = temp.next

  while temp != l.last:
    a = a + str(temp.data) + "\t"
    temp = temp.next
  print(a)

if __name__ == '__main__':
  l = CircularLinkedList(10)

  a = Node(20)
  b = Node(30)
  c = Node(40)

  l.last.next = a
  a.next = b
  b.next = c
  c.next = l.last

  traversal(l)

  z = Node(50)
  insert_after(z, c)
  z = Node(25)
  insert_after(z, a)
  z = Node(100)
  insert_at_last(l, z)

  traversal(l)

  delete(l, l.last);
  delete(l, b);

  traversal(l);