from node import Node

class MyList:

  """A \"alternative\" to default list"""

  def __init__(self,*head_value):
    self.length=len(head_value)
    if len(head_value):
      self.head=Node(head_value[0])

      current=self.head
    
      for item in head_value[1:]:
        current.next=Node(item)
        current=current.next
    else:
      self.head=None

  def __iter__(self):
    while (current:=current if "current" in locals() else self.head) is not None:
      yield current
      current=current.next

  def __len__(self):
    return self.length

  def __str__(self):
    return "["+" -> ".join(map(str,self))+"]"

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

  def clear(self):
    self.head=None

  def copy(self):
    return MyList(*self)

  def insert(self,index,element):
    if index>self.length or index<0:
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

    return self

  def map(self,function):
    return MyList(*(function(node.value) for node in self))

  def pop(self,index=None):
    if index is None:
      index=self.length-1

    if index>self.length or index<0:
      raise IndexError

    counter=0
    current=self.head

    while counter<index-1:
      current=current.next
      counter+=1

    if self.length==1:
      self.head=None
    elif index==0:
      self.head=self.head.next
    else:
      current.next=current.next.next
    self.length-=1

    return self

  def remove(self,value):
    counter=0

    while (current:=current if "current" in locals() else self.head) is not None:
      if current.value==value:
        self.pop(counter)
        return self
      current=current.next
      counter+=1

    raise ValueError