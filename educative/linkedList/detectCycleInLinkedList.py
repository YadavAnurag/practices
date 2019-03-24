#Access HeadNode => list.getHead()
#Check if list is empty => list.isEmpty()
#Node class  { int data ; Node nextElement;}

def detectLoop(list):
  # Keep two iterators
  onestep = list.getHead()
  twostep = list.getHead()
  while(onestep and twostep and twostep.nextElement): 
    onestep = onestep.nextElement # Moves one node at a time
    twostep = twostep.nextElement.nextElement # Moves two nodes at a time
    if onestep == twostep: # Loop exists
      return True
  return False

#----------------------

list = LinkedList()

list.insertAtHead(21)
list.insertAtHead(14)
list.insertAtHead(7)

head = list.getHead()
node = list.getHead()

# Adding a loop
for i in range(4):
  if(node.nextElement == None):
    node.nextElement = head.nextElement
    break
  node = node.nextElement

print(detectLoop(list))

