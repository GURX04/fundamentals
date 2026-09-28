# print("hello world")

# name = "aniket"
# age = 19 
# skill = "python"
# student = True



# print(type(name))
# print(type(age))
# print(type(skill))
# print(type(student))



# change = 100 

# change = "aniket"
# print(change)


# name = input("enter your name:")
# age = int(input("age?  "))
# gender = input("gender?   ")

# print("hi " + name +" of "+ str(age) + " and gender "+ gender)

# print(type(name))
# print(type(age))
# print(type(gender))

# print(f"hi {name} of age: {age} and gender {gender}")




# -----------------practice qn day1 ------------------------


# name = str(input("enter your name: "))
# age = int(input("enter your age: "))
# course = str(input("enter your course: "))
# clg = str(input("enter your clg: "))
# cgpa = float(input("enter your cgpa: "))

# print(f"Name: {name}")
# print(f"age: {age}")
# print(f"course: {course}")
# print(f"clg: {clg}")
# print(f"cpga: {cgpa}")





# --------------------------------------------

# a = int(input("enter a no: "))
# b = int(input("enter another no: "))

# print(f"addition:; {a+b}")
# print(f"subtraction: {a-b}")
# print(f"mulplication: {a*b}")
# print(f"division: {a/b}")
# print(f"remainder: {a%b}")

# mylist = [1,2,3,4,5,6] # =datatype - list: holds many value
#                        # is mutable , postion on elements start from 0 

# print(mylist[-1])  # accessing the list 
# print(mylist[4])

# mylist[5] = 2
# print(mylist[5])   #changing valuea in the list 

# mylist.append(7)  #appending the list
# print(mylist)


# mylist.insert(0,99)   #insertiing in the list ,syntax:list.insert(index, value)
# print(mylist)


# mylist.remove(2)      #removes the values from the list

# mylist.remove(2)
# print(mylist)

# mylist.pop(1)  #removes index values from the list
# mylist.pop ()   #removes the last value from the list

# print(mylist)


# data = [10,20,30,40,50,60,70,80,90,100]

# print(len(data))    #prints the no of elements in the list 

#     #useful functions

# print(sum(data))
# print(max(data))
# print(min(data))

#     #avetage function

# print(sum(data)/len(data))
# print(max(data) - min(data))


#----------------EXERCISE-------------------

# data = [12, 15, 18, 20, 25, 30]

# print("Dataset:", data)
# print("Number of values:", len(data))
# print("Total:", sum(data))
# print("Minimum:", min(data))
# print("Maximum:", max(data))

# average = sum(data) / len(data)

# print("Average:", average)

list1 = [1,2.,3]


#------------------ Day 3 --------------------

#for loop syntax - for value in data:
#                       print(value)


# loop = [10,20,30,40,50,]

# for value in loop:
#     if value>25:
#      print(value)
#     elif value == 30 :
#      print("skipped")
#     else:  
#      print(value*2)


# average = sum(loop)/len(loop)

# for value in loop:
#     if value >= average:
#         print(value)
#     else :
#         print("not above average :", value)


# data = [15, 20, 25, 30, 35]

# print(len(data))
# print(sum(data))
# print(max(data))
# print(min(data))
# print(sum(data)/len(data))

# for value in data:
#     if value >= 25:
#         print(value)




# marks = [45, 67, 82, 39, 91, 55, 73]

# for value in marks:
#     if value >= 50:
#         print(value)


#add 5 number to a empppty list by taking user input
# mylist = []


# for i in range(5):
#     add = int(input("enter a number:"))
#     mylist.append(add)

# print(mylist)    



#calculate the average and prrint 

# data = [10, 20, 30, 40, 50]

# avg = sum(data)/len(data)

# for value in data:
#     if value >= avg:
#         print(value)

#list slicing

# data = [10, 20, 30, 40, 50]


# print(data[2:5])

# print(data[::2])


# data = [10, 20, 30, 40, 50]

# num = int(input("enter a number to see that it exist inn t[he list]"))
# if num in data:
#     print("yes")
# else:
#     print("no")

# data = [50, 10, 40, 20, 30]

# data.sort()

# print(data)

# marks = [45, 67, 82, 39, 91, 55, 73]

# marks.sort()
# print(marks)

# marks.sort(reverse=True)
# print(marks)


#------------nested list-------

neslist = [
    ["aniket","chembur",418],
    ["vedant","cotton green",533],
    ["ruchi","borivali",710],
    ["krrish","andheri",684],
]

# print(neslist)
# print(neslist[1][2])

# for i in range(4):
#     print(neslist[i][1])

# print(len(neslist))

# ss =  ["aniket","chembur",418]
# print(neslist.count(ss))

#--------------------day 4-----------------------------

# for i in range(21):
#     print(i)

# for i in range(0,21,2):
#     print(i)

# ls = []
# l = len(ls)
# for l in range(0,5):
#     data = int(input("enter an integer: "))
#     ls.append(data)

# print("orginal list:",ls)

# ls.sort()
# print("sorted list: ",ls)

# ls.sort(reverse = True)
# print("reverse sorted list: ",ls)


# data = [10, 20, 30, 40, 50, 60, 70]

# print(data[0:3])

# l = len(data)
# s = l - 3
# print(data[s:l])

# print(data[0:(len(data)+1):2])

# print(data[2:6])


# students = [
#     ["Aniket", 80],
#     ["Rahul", 75],
#     ["Soham", 90],
#     ["Vedant", 85]
# ]



# for i in range(len(students)):
#     j = 0
#     print(f"name : {students[i][0]} marks: {students[i][1]}")
#     j += 1
#     avg = 0
#     avg =  avg + students[i][1]

# print("average:",avg)    



# data = [10, 20, 30, 40, 50]

# new = [value *2 for value in data]
# print(new)

data = [12, 45, 23, 67, 34, 89, 15, 56]

new = []
for i in data:
    if i >= 40:
        new.append(i)

print(new)        


mew = [value for value in data if value >=40]
print(mew)

if new== mew:
    print("lessfkinggoo")