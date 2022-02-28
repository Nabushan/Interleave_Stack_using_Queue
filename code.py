"""

This problem was asked by Google.
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
Hint: Try working backwords from the end state.

"""

class Stack:
    #Stack method is implemented using list() method internally.
    arr = list()
    size = 0
    def __init__(self):
        self.arr = list()
        self.size = 0

    def push(self,num):
        self.arr.append(num)
        self.size+=1

    def pop(self):
        self.temp = self.arr[-1]
        del self.arr[-1]
        self.size-=1
        return self.temp

    def get_size(self):
        return self.size

    def print_stack(self):
        print("Stack items : {}, Stack Size : {}".format(self.arr,self.get_size()))

class Queue:
    #Queue method is implemented using list() method internally.
    arr = list()
    size = 0
    def __inti__(self):
        self.arr = list()
        self.size = 0

    def enqueue(self,num):
        self.arr.append(num)
        self.size+=1

    def dequeue(self):
        self.temp = self.arr[0]
        del self.arr[0]
        self.size-=1
        return self.temp

    def get_size(self):
        return self.size

    def print_queue(self):
        print("Queue items : {}, Queue Size : {}".format(self.arr,self.get_size()))
    

def helper_load_initial_stack(s,arr):
    for i in arr:
        s.push(i)

def helper_load_stack(s,q,times):
    while (times > 0):
        s.push(q.dequeue())

        times-=1

def helper_load_queue(s,q,times):
    while(times > 0):
        q.enqueue(s.pop())
        
        times-=1

def interleave(s,q,arr):
    length = len(arr)
    helper_load_initial_stack(s,arr)
    while(length > 0):
        helper_load_queue(s,q,length - 1)
        helper_load_stack(s,q,length - 1)
        length-=1

def helper(arr):
    s = Stack()
    q = Queue()
    interleave(s,q,arr)
    s.print_stack()
    q.print_queue()

#Driver Code 1
arr = [1, 2, 3, 4, 5]
helper(arr)

#Driver Code 2
arr= [1, 2, 3, 4]
helper(arr)
