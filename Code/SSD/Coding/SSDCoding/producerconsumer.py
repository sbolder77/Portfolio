'''code source: https://techmonger.github.io/55/producer-consumer-python/ - 
Module provising producer consumer printing function'''

from threading import Thread
from queue import Queue

q = Queue()
final_results = []

'''Function to calcualte the producer consumer threads'''
def producer():
    for P in range(100):
        q.put(P)        

def consumer():
    while True:
        number = q.get()
        result = (number, number**2)
        final_results.append(result)
        q.task_done()

for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()

producer()
q.join()
print (final_results)