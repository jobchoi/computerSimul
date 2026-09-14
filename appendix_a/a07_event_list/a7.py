import queue
from queue import Queue

# A.7.1 Priority Queue
# Implementing the event list using the queue module.

Event_List = queue.PriorityQueue()

for item in ((10, "Arrival"), (5,"Departure"),(2,"Fully_Charged")):
    Event_List.put(item)

print("=== Priority Queue ===")
while not Event_List.empty():
    print(Event_List.get())



# A.7.2 Heap Queue
# Implementing the event list using the heapq module.
import heapq
from heapq import *

Event_List = []

heappush(Event_List, (10, "Arrival"))
heappush(Event_List, (5, "Departure"))
heappush(Event_List, (2, "Fully_Charged"))  

# Print the first item in the heap
print("=== Heap Queue ===")
print(heappop(Event_List))