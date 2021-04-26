import os
import random

data_base_dir = '/home/qb/NewHome/yoloV5t/src/yolov5/data/image'
file_list = [] # Pic list
list1 = [] # file name
list1 = os.listdir(data_base_dir)

file_name = '/home/qb/NewHome/yoloV5t/src/yolov5/data/'
file_list_name1 = file_name + 'train.txt'
file_list_name2 = file_name + 'val.txt'
file_list_name3 = file_name + 'test.txt'

for file1 in list1:
    if file1.endswith(".jpg"):
        file_list.append(file1)

random.shuffle(file_list) # randomize
number_of_lines = len(file_list)
print(number_of_lines)

f1 = open(file_list_name1,'w') #train 1200
for i in range(0,1200): #0-1199
    f1.write(data_base_dir + '/' + file_list[i] + '\n')
f1.close()

f2 = open(file_list_name2,'w') #val 407
for i in range(1200,1607): #1200-1606
    f2.write(data_base_dir + '/' + file_list[i] + '\n')
f2.close()

f3 = open(file_list_name3,'w') #test 100
for i in range(1607,1707): #1607-1706
    f3.write(data_base_dir + '/' + file_list[i] + '\n')
f3.close()