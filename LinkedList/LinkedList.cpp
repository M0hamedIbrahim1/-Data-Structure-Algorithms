class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node 
    def print_values(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
my_list = LinkedList()
my_list.append("Mohamed")
my_list.append("Ibrahim")
my_list.append("20")
my_list.append("Years")
my_list.print_values()

------------------------------
//Mohamed
//Ibrahim
//20
//Years
