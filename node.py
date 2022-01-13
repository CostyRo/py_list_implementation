class Node:

  """A simple class to generates nodes"""

  def __init__(self,value):
    self.value=value
    self.next=None

  def __str__(self):
    return f"{self.value}"