class MyCircularDeque:  

    def __init__(self, k: int):  
        self.capacity = k  
        self.deque = [0] * k  
        self.front = -1  
        self.rear = -1  

    def insertFront(self, value: int) -> bool:  
        if self.isFull():  
            return False  
        if self.isEmpty():  
            self.front = self.rear = 0  
        else:  
            self.front = (self.front - 1) % self.capacity  
        self.deque[self.front] = value  
        return True  

    def insertLast(self, value: int) -> bool:  
        if self.isFull():  
            return False  
        if self.isEmpty():  
            self.front = self.rear = 0  
        else:  
            self.rear = (self.rear + 1) % self.capacity  
        self.deque[self.rear] = value  
        return True  

    def deleteFront(self) -> bool:  
        if self.isEmpty():  
            return False  
        if self.front == self.rear:  
            self.front = self.rear = -1 
        else:  
            self.front = (self.front + 1) % self.capacity  
        return True  

    def deleteLast(self) -> bool:  
        if self.isEmpty():  
            return False  
        if self.front == self.rear:  
            self.front = self.rear = -1  
        else:  
            self.rear = (self.rear - 1) % self.capacity  
        return True  

    def getFront(self) -> int:  
        if self.isEmpty():  
            return -1  
        return self.deque[self.front]  

    def getRear(self) -> int:  
        if self.isEmpty():  
            return -1  
        return self.deque[self.rear]  

    def isEmpty(self) -> bool:  
        return self.front == -1  

    def isFull(self) -> bool:  
        return (self.rear + 1) % self.capacity == self.front  

# Example usage:  
# obj = MyCircularDeque(k)  
# param_1 = obj.insertFront(value)  
# param_2 = obj.insertLast(value)  
# param_3 = obj.deleteFront()  
# param_4 = obj.deleteLast()  
# param_5 = obj.getFront()  
# param_6 = obj.getRear()  
# param_7 = obj.isEmpty()  
# param_8 = obj.isFull()