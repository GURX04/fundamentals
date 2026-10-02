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

# list1 = [1,2.,3]


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

# neslist = [
#     ["aniket","chembur",418],
#     ["vedant","cotton green",533],
#     ["ruchi","borivali",710],
#     ["krrish","andheri",684],
# ]

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

# data = [12, 45, 23, 67, 34, 89, 15, 56]

# new = []
# for i in data:
#     if i >= 40:
#         new.append(i)

# print(new)        


# mew = [value for value in data if value >=40]
# print(mew)

# if new== mew:
#     print("lessfkinggoo")


#day 4 
#start with dictionary - key value pair

# student = {
#     "name" : "aniket",
#      "age" : 19,
#      "age" : 24
# }

# print(type(student))
# print(student)


# student["city"] = "mumbai"
# print(student)

# student["city"]= "vashi"
# student.pop("city")
# print(student)

# del student["age"]
# print(student)

# student["age"]= 19
# student["city"] = "Mumbai"
# print(student)


# if "name" in student:
#     print(student["name"])

# print(student.keys())
# for key in student:
#     print(key)


# print(len(student.keys()))

# student.keys()
# student.values()
# print(student.items())


#------nested dict-------

# ITgang = {
#     "aniket": {
#         "gen": "male",
#         "age": 19
#     },

#     "vedant": {
#         "gen": "male",
#         "age": 20
#     },
    
#     "krrish": {
#         "gen": "male",
#         "age": 20
#     },

#     "ruchi": {
#         "gen": "female",
#         "age": 19
#     }
# }

# print(ITgang["aniket"]["gen"])
# print(ITgang["ruchi"]["age"])


# gng = [
#     {
#         "name" : "aniket",- 
#         "age" : 19
#     },

#     {
#         "name":"vedant",
#         "age":20
#     }
# ]

# print(gng[0]["age"])

# for i in range(len(gng)):
#     print(gng[i]["age"])

#---------------practice  ------------
# student = {
#     "name": "Aniket",
#     "age": 20,
#     "cgpa": 7.1
# }

# print(student["cgpa"])

# student["age"] = 21
# student["cgpa"] = 7.8

# student["city"] = "mumbai"
# student["branch"] = "it"

# print(student)

# student.pop("city")
# del student["branch"]

# print(student)


# if "cgpa" in student:
#     print("cgpa exists")

# students = {
#     "name": "Aniket",
#     "age": 20,
#     "cgpa": 7.1
# }    


# for key,value in students.items():
#     print(key, " : ",value )

# students = [
#     {"name": "Aniket", "marks": 85},
#     {"name": "Rahul", "marks": 72},
#     {"name": "Soham", "marks": 91},
#     {"name": "Vedant", "marks": 68}
# ]

# for i in range(len(students)):
#     if students[i]["marks"] > 80:
#         print(students[i]["name"]) 

#average
# sum = 0
# for student in students:
#     sum = sum + student["marks"]

# print(sum/len(students))


# get highest marks

# high = []
# for student in students:
#     high.append(student["marks"])

# print(max(high))



# data = [
#     {"age": 20, "salary": 25000},
#     {"age": 22, "salary": 32000},
#     {"age": 19, "salary": 18000},
#     {"age": 25, "salary": 45000},
#     {"age": 21, "salary": 28000}
# ]

# for value in data:
#     if value["salary"] > 25000:
#         print(value["salary"])

# total = []
# for value in data:
#     total.append(value["salary"])

# print(sum(total))
# print(sum(total)/(len(data)))
# print(max(total))
# print(min(total))




# students = [
#     {"name": "Aniket", "marks": 85},
#     {"name": "Rahul", "marks": 72},
#     {"name": "Soham", "marks": 91},
#     {"name": "Vedant", "marks": 68},
#     {"name": "Adarsh", "marks": 78}
# ]

# nlist = []
# for value in students:
#     nlist.append(value["marks"])

# avg = sum(nlist) / len(nlist)
# highest = max(nlist)
# lowest = min(nlist)

# for value in students:
#     if value["marks"] > 70:
#         print(value["name"])

#     if value["marks"] > avg:
#         print(value["name"])




 #--------------------tuple-------------------

# tup = ('aniket',19,"aplha-male",True,7.146)
# print(tup)


# tt = tuple("aniket")
# print(tt)

# name, age ,gender,gay,gpa = tup
# print(name)
# print(gender)


#-----practice tuple ---------

# data = (10,20,30,40,50)
# print(data[2])

# data = (10, 20, 30, 20, 40, 20)
# print(data.count(20))

# data = (5, 10, 15, 20, 25)
# for value in data:
#     print(value)


# student = ("Aniket", 20, 7.1)    

# name, age ,cgpa = student

# print(name)
# print(age)
# print(cgpa)



# coordinates = (
#     (10, 20),
#     (30, 40),
#     (50, 60)
# )


# for value in coordinates:
#     print(value[0],value[1])


# students = (
#     ("Aniket", 85),
#     ("Rahul", 72),
#     ("Soham", 91),
#     ("Vedant", 68)
# )


# for i in students:
#     if i[1] > 80:
#         print(i[0])


#------------------------ day 6 ------------------

# sets 

# set1 = {"aniket", 19}

# print (set1)

# data = {10, 20, 30, 20, 10, 40}
# print(data)

# set2 = {10,20,30}
# set2.add(40)
# print(set2)


# set2.remove(20)
# print(set2)




# data = [1, 2, 2, 3, 4, 4, 5, 5]

# data = set(data)
# # print(data)


# numbers = {10, 20, 30, 40}

# if 50 in numbers:
#     print("yes")

# else:
#     print("not present")


# a = {1, 2, 3}
# b = {3, 4, 5}

# c = a.union(b)
# c = a | b
# print(c)

# d = a.intersection(b)
# d = a & b
# print(d)

# students_a = {"Aniket", "Rahul", "Soham", "Adarsh"}
# students_b = {"Soham", "Vedant", "Aniket", "Rohit"}


# a = students_a | students_b
# b = students_a & students_b
# print(b)



# data = [10, 20, 20, 30, 40, 40, 50, 50, 50]

# data = set(data)

# print(len(data))



# functions
# def aniket():
#     print("aniket says hi")

# aniket()

# def greet(name):
#     print("hi hello welcome", name )

# greet("ani")
# greet("sunny")



#---- practice-functiions ----


# def hello():
#     print("hello python")


# def add(a,b):
#     return a + b 
    
# result = add(15, 25)
# print(result)

# def square(number):
#     return number*2

# print(square(5))

# def isoddiseven(n):
#     if n %2 ==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")

# isoddiseven(77)
# isoddiseven(40)        



# marks = [80, 70, 90, 60, 100]

# def calavg(data):
#     print(sum(data)/len(data))

# calavg(marks)



# marks = [35, 70, 45, 20, 90, 33, 80]

# def getpassedstudents(data):
#     passed = []

#     for number in marks:
#         if number>= 40:
#             passed.append(number)

#     print(passed)       

# getpassedstudents(marks)    

# student = {
#     "name": "Aniket",
#     "marks": 85
# }

# def checkstudent(data):
#     if student["marks"] >= 40:
#         print(student["name"],"passed")


# checkstudent(student)



# data = [10, 20, 30, 40, 50]

# def anal(data):
#     total = sum(data)
#     high = max(data)
#     low = min(data)
#     avg = total/len(data)

#     print(f"total: {total},highest: {high},lowest: {low},avg: {avg} ")


# anal(data)


# def normalze(data):
#     normal = []
#     for number in data:
#         ss = (number - min(data)) / (max(data) - min(data))
#         normal.append(ss)

#     print(normal) 

# normalze(data)