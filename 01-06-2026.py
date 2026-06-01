'''
Data Types:
Premitive:
1 Integer
2 Float
3 String
4 Boolean

Non-Premitive:
1 List
2 Tuple
3 Dictionary
4 Set
'''

a = 10

'''
Operator:
1 Arithmetic Operator: + - * / % // **
2 Assignment Operator: = += -= *= /= %= //= **=
3 Comparison Operator: == != > >= < <=
4 Logical Operator: not or and
5 Bitwise Operator: & | ^ ~ << >> 
6 Membership Operator: in, not in
7 Identity Operator: is, is not
'''



# lt = [10,20,30]
# lt1 = [10,20,30]

# print(40 not in lt)

# t = (10,20,30)
# t1 = (10,20,30)

# print(id(lt), id(lt1))
# print(id(t), id(t1))

# print(lt is lt1)
# print(t is t1)


'''
Conditional Statement:
1 if
2 elif
3 if else
4 nested if
'''

# wt = int(input("Enter the weight: "))
# if 0 < wt and  wt <= 2000:
#     print ("15 min")
# else :
#     print ("1st if failed")
# if 2000 < wt and  wt <= 4000:
#     print ("25 min")
# else :
#     print ("2nd if failed")
# if 4000 < wt and  wt <= 7500:
#     print ("35 min")
# else:
#     print ("OVERWEIGHT")

'''
Loopings
for : 1. with index 2. with item
while
'''
# t = (10,20,30)
# for i in range(3):  #0 1 2 
#     print(t[i])

# for j in t:
#     print(j)

# range(start,stop,step)  

start_default = 0
step_default = 1

# range(2,10,2)  =>  2 4 6 8 
# range(3,30,5)  =>  3 8 13 18 23 28 
# range(-10,-50,-5) =>  -10 -15 -20 -25 -30 -35 -40 -45
# range (50:5:-5)
# limit = 10
# i = 0
# while i < limit:
#     print(i)
#     i += 1


# print all the prime number within the range of 10 to 50

n = 7
for j in range(11,50):
    flag = True
    for i in range(2,j):
        if j%i == 0:
            flag = False
            break 

    if flag:
        print("prime",j)
    else:
        print("composite",j)
        

