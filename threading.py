import threading
import queue

BUF_SIZE = 1000
q = queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super().__init__(ProducerThread,self)
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                #item = frame
                q.put(item)
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super().__init__(ConsumerThread,self)
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                #send(item)
        return

if __name__ == '__main__':
    
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    c.start()