
from multiprocessing import Process
from matcher.multiparallel import tasks
import time



# # sequntial
# start1 = time.perf_counter()
# tasks.task1()
# tasks.task2()
# tasks.task3()
# tasks.task4()
# end1 = time.perf_counter()
# print(end1-start1)



if __name__ == "__main__": 
#     #multiparallel

    start2 = time.perf_counter()
    p1 = Process(target=tasks.task1())
    p2 = Process(target=tasks.task2()) 
    p3 = Process(target=tasks.task3()) 
    p4 = Process(target=tasks.task4()) 
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end2 = time.perf_counter()
    print(end2-start2)


