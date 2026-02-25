#q1
#print("sum of numbers from 1 to 5:",sum(range(1,6)))
#q2a
#1
#0
#   #q2b
# number = int(input("enter the number:"))
# if number % 2 == 0:
#     print(number, "is an even number.")
# else:    print(number, "is an odd number.")
#q3
# n = int(input("enter the number:"))
# print("*"*n)
# print("# "*n)
#q4
# print("david doe")
# print("1600 wilshire blvd #205,los angeles,ca 90017")
#q5 0,1,0,1
#q6
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# if num1 < num2:
#     print(num1, "is smaller than", num2)
# elif num1 > num2:
#     print(num2, "is smaller than", num1)
# else:    print("both numbers are equal.")
#q7
# print("are you an adult?")

# answer = input("enter yes or no:")

# if answer=="yes" :
#     print("are you married?")
#     answer = input("enter yes or no:")
#     if answer=="yes" :
#         print("you are married")
#     elif answer=="no" :
#         print("you are not married")
# elif answer=="no" :
#     print("you are not an adult")

#q8
# for num in range(2, 13):
#     its_prime = True
#     for i in range(2,num):#this checks if num is divisible by any number from 2 to num-1
#         if num%i==0:
#             its_prime = False
#             break
#     if its_prime:
#         print(num, "is a prime number")
#     else:
#         print(num, "composite number")


#q9
#abc = a3+b3+c3# armstrong number
# for num in range(100, 1000):
#   temp = num
#   sum=0
# while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
# if sum == num:
#         print(num, "is an Armstrong number")

#q10
# l1 = ['i like','i love']
# l2 = ['pancake','kiwi juice','espresso']
# for i in l1:
#     for j in l2:
#         print(i, j)
#q11
# person ={'name':'david doe','age':26,'weight': 82,'job':'data scientist'}
# person.update({'father':'john doe'})
# print(person)
#q12
# lst =[5,6,9,2,12,3,8,7]
# max_num = 0
# for i in range(len(lst)):
#     if lst[i] > max_num:
#         max_num = lst[i]
#         lst[i], lst[0] = lst[0], lst[i] 
# print("the largest number is:", ) 
#q13
# a = [[1,2],[3,4],[5,6]]
# new_list = []
# for sublist in a:
#     for item in sublist:
#         new_list.append(item)
#         print(new_list)
#q14

# maria = {
#     'korean': 95,
#     'english': 88,
#     'math': 92,
#     'science': 82
# }

# total = sum(maria.values()) 
# count = len(maria)            
# average = total / count       

# print(average)
#q15
#import copy

# Nested dictionary
# school = {
#     'student1': {
#         'name': 'Maria',
#         'grade': 10
#     },
#     'student2': {
#         'name': 'John',
#         'grade': 9
#     }
# }
# school2 = copy.deepcopy(school)
# print(school is school2)
#q16
# scores = (
#     ('Hyun', 88, 95, 90),
#     ('Maria', 92, 89, 94),
#     ('John', 85, 90, 88),
#     ('Anna', 90, 93, 91)
# )


# names, english, math, science = zip(*scores)


# average_math = sum(math) / len(math)

# print("Math Scores:", math)
# print("Average Math Score:", average_math)
