#Import the time class to allow timers
import time as time

#Specify the class
class CircularPrinterQueue:
    #Constant
    CAPACITY:int = 10

    #Constructor
    def __init__(self):
        self.data = [[None,None,None,None]] * self.CAPACITY
        self.front = 0
        self.size = 0
        self.jobId= 0

    #Method for empty check
    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

    #Method to check what is on top
    def top(self):
        return self.data[self.front]

    #Method to check if full
    def is_full(self):
        if self.size == self.CAPACITY:
            return True
        else:
            return False

     #Method to add to queue
    """"When taking data in, insert a list of[user_id,job_id,priority,waiting_time]:
                -  Only User_Id needed
                -  Job_Id will be dynamic 
                -  Priority will be default 1
                -  Waiting time will be obtained from the value on time.perf_counter()
                        * time.perf_counter()[Python] is similar to System.nanoTime[Java]"""
    def enqueue(self,user_id):
        if self.is_full():
            print("The queue is full, wait a short while")
            return
        avail = (self.size + self.front) % self.CAPACITY
        self.jobId +=1
        job_id = self.jobId
        priority = 1
        waiting_time = time.perf_counter_ns()
        self.data[avail]= [user_id,job_id,priority,waiting_time]
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, can't print anything")
            return
        output = self.data[self.front]
        self.data[self.front]= [None,None,None,None]
        self.front = (self.front + 1)% self.CAPACITY
        return output

    def show_status(self):
        count:int = 0
        i:int = 0
        while i <= self.CAPACITY-1:
            if self.data[i][2] is not None:
                count+=1
            i+=1
        if count==0:
            print("There are no jobs in the queue")
            return
        else:
            print(f"There are {count} job(s) in the queue")
            return

if __name__=="__main__":
    cpq = CircularPrinterQueue()
    cpq.show_status()
    cpq.enqueue("caleb")
    cpq.show_status()
    cpq.enqueue("kimanzi")
    cpq.show_status()
    cpq.enqueue("mutiso")
    cpq.enqueue("169890")
    cpq.show_status()
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    cpq.dequeue()
    cpq.dequeue()
