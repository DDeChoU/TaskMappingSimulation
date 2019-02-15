from Generation import Generation
from Scheduler import Scheduler
from Model import Model
from Task import Task
from Partition import Partition
import copy

#test document
'''total_density = 0.5
total_af = 2
g=Generation()
task_list = g.generate_tasks(total_density, False)
partition_list = g.generate_partitions(total_af)'''

partition_list = {}
partition_list[0] = Partition(0, 0.5481)
partition_list[1] = Partition(1, 0.708)
partition_list[2] = Partition(2, 0.677)
partition_list[3] = Partition(3, 0.068)

task1 = Task(0, 1, 31, 100,100, 1, False)
task2 = Task(1, 5, 19, 100, 100, 1, False)
task_list = []
task_list.append(task1)
task_list.append(task2)
s = Scheduler('almost_worst_fit')
model = Model(s, task_list, partition_list)
model.run_model()
print model.is_schedulable()