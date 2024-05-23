import time as T
import random
T1=T.time_ns()
for item in range(0,200000):
    ran=random.randint(0,100)
    print(ran)
T2=T.time_ns()
td=T2-T1
print(td)
