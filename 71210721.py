class CircularQueue:

    def __init__(self, s):
        self.s = s
        self.queue = [None for i in range(s)]
        self.front = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.s == self.front):
            print(" Antrian penuh")
        elif (self.front == -1):
            self.front = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.s
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.front == -1):
            print("Antrian kosong")
        elif (self.front == self.tail):
            temp = self.queue[self.front]
            self.front = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.s
            return temp

    def display(self):
        if (self.front == -1):
            print("Antrian kosong")
        elif (self.tail > self.front):
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.s):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.tail + 1) % self.s == self.front):
            print("Antrian penuh")

CircularQueue = CircularQueue(5)
CircularQueue.enqueue(14)
CircularQueue.enqueue(22)
CircularQueue.enqueue(13)
CircularQueue.enqueue(-6)
CircularQueue.display()
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
CircularQueue.display()
CircularQueue.enqueue(9)
CircularQueue.enqueue(20)
CircularQueue.enqueue(5)
CircularQueue.display()