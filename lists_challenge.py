class Node:

  """A simple class to generates nodes"""

  def __init__(self,value):
    self.value=value
    self.next=None

  def __str__(self):
    return f"{self.value}"

class MyList:

  """A \"alternative\" to default list"""

  def __init__(self,*head_value):
    self.length=len(head_value)
    self.head=Node(head_value[0])
    current=self.head
    
    for item in head_value[1:]:
      current.next=Node(item)
      current=current.next

  def __iter__(self):
    while (current:=current if "current" in locals() else self.head) is not None:
      yield current
      current=current.next

  def __len__(self):
    return self.length

  def __str__(self):
    return " -> ".join(map(str,self))

  def __reversed__(self):
    return MyList(*reversed([node.value for node in self]))

  def append(self,*value):

    while (current:=current if "current" in locals() else self.head).next is not None:
      current=current.next

    current.next=Node(value[0])
    current=current.next

    for item in value[1:]:
      current.next=Node(item)
      current=current.next

    self.length+=len(value)

    return self

  def insert(self,index,element):
    if index>self.length:
      raise IndexError

    counter=0
    current=self.head

    while counter<index-1:
      current=current.next
      counter+=1

    temp=Node(element)
    temp.next=current.next
    current.next=temp

    self.length+=1

  def map(self,function):
    return MyList(*(function(node.value) for node in self))

my_list=MyList(1,2,3,4)
print(my_list)

my_list.append(5,6)
print(my_list)

my_list.insert(2,2.5)
print(my_list)

print(len(my_list))

for i in my_list:
  print(f"Node: {i}, value: {i.value}, next: {i.next}")

print(reversed(my_list))

print(my_list.map(lambda x: x+1))