class queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
    def enqueue(self,val):
        self.queue.append(val)
        if(self.front == -1):
            self.front+=1
            self.rear+=1
            return
        self.rear+=1
        
    def dequeue(self):
        T = self.queue.pop(self.rear)
        self.rear-=1
        if self.empty() is True:
            self.rear = -1
            self.front = -1
            
    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def Front(self):
        if self.empty() is True:
            print("Queue Is Empty")
        else:
            return self.front
    def Rear(self):
        if self.empty() is True:
            print("Queue Is Empty")
        else:
            return self.rear
    def display(self):
        if self.empty() is True:
            print("Queue Is Empty")
            return
        print("-- Queue --")
        i = self.front
        while i <= self.rear:
            print(self.queue[i])
            i+=1

a = queue()
a.enqueue("faculty")
a.enqueue("of")
a.enqueue("computer")
a.enqueue("and")
a.enqueue("information")
a.display()
#Print front of queue
print(a.Front())
a.dequeue()
#after deleting last element 
a.display()
------------------------------
// -- Queue --
// faculty
// of
// computer
// and
// information
// 0
// -- Queue --
// faculty
// of
// computer
// and
