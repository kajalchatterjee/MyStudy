class node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self) -> None:
    pass

  def append(self, data):
    newnode = node(data)
    if self.head == None:
      self.head = newnode
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode

  def display(self):
    temp = self.head
    while temp != None:
      print(temp.data, "->", end=" ")
      temp = temp.next
    print()

  def insert_at_beginning(self, data):
    newnode = node(data)
    newnode.next = self.head
    self.head = newnode

  def insert_at_end(self, data):
    newnode = node(data)
    if self.head == None:
      self.head = newnode
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode

  def insert_at_position(self, pos, data):
    newnode = node(data)
    if self.head == None:
      self.head = newnode
    else:
      temp = self.head
      for i in range(pos - 1):
        temp = temp.next
      newnode.next = temp.next
      temp.next = newnode

  def delete_at_beginning(self):
    if self.head == None:
      print("list is empty")
    else:
      temp = self.head
      self.head = self.head.next
      temp.next = None

  def delete_at_end(self):
    if self.head == None:
      print("list is empty")
    else:
      temp = self.head
      while temp.next.next != None:
        temp = temp.next
      temp.next = None

  def delete_at_position(self, pos):
    if self.head == None:
      print("list is empty")
    else:
      temp = self.head
      for i in range(pos - 1):
        temp = temp.next
      temp.next = temp.next.next

  def search(self, data):
    if self.head == None:
      print("list is empty")
    else:
      temp = self.head
      while temp != None:
        if temp.data == data:
          return True
        temp = temp.next
      return False

  def count(self):
    if self.head == None:
      return 0
    else:
      temp = self.head
      count = 0
      while temp != None:
        count += 1
        temp = temp.next
      return count

  def reverse(self):
    prev = None
    current = self.head
    while current != None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def insert_node_at_middle(head, data):
    newnode = node(data)
    if head == None:
      head = newnode
    else:
      temp = head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode
    return head

  def insert_node_at_middle_recursive(head, data):
    newnode = node(data)
    if head == None:
      head = newnode
    else:
      head.next = insert_node_at_middle_recursive(head.next, data)
    return head

  def insert_node_at_middle_iterative(head, data):
    newnode = node(data)
    if head == None:
      head = newnode
    else:
      temp = head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode
    return head

  def insert_node_at_middle_recursive_iterative(head, data):
    newnode = node(data)
    if head == None:
      head = newnode
    else:
      temp = head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode
    return head

  def insert_node_at_middle_recursive_iterative_2(head, data):
    newnode = node(data)
    if head == None:
      head = newnode
    else:
      temp = head
      while temp.next != None:
        temp = temp.next
      temp.next = newnode
    return head

  def insert_node_in_sorted_list(self, data):
    newnode = node(data)
    if self.head is None or self.head.data >= data:
      newnode.next = self.head
      self.head = newnode
    else:
      current = self.head
      while current.next is not None and current.next.data < data:
        current = current.next
      newnode.next = current.next
      current.next = newnode


if __name__ == "__main__":
  llist = LinkedList()
  llist.append(1)
  llist.append(2)
  llist.append(3)
  llist.append(4)
  llist.append(5)
  llist.display()
  llist.insert_at_beginning(0)
  llist.display()
  llist.insert_at_end(6)
  llist.display()
  llist.insert_at_position(3, 3.5)
  llist.display()
  llist.delete_at_beginning()
  llist.display()
  llist.delete_at_end()
  llist.display()
  llist.delete_at_position(2)
  llist.display()
  print(llist.search(3))
  print(llist.count())
  llist.reverse()
  llist.display()
