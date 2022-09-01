'''one person different names-if we call only one function,with that one function we want to get total o/p'''

# def course1(name='core python'):
#     print(f'i have completed my course and course is {name}')
#     course3()
# def course2(name='advanced python'):
#     print(f'i am in middle of course and course is {name}')
#     course1()
# def course3(name='java'):
#     print(f'i want to learn basic of this course is {name}')
# course2()


'''scope of a variable'''
'''local scope - value can be assigned inside the function as it can't be used outside the function'''
# def hii():
#     a=2;b=4;c=6
#     print(a+b)
#     print(a+c)
# hii()

# a=2;b=4;c=6
# def hii():
#     print(a+b)
#     print(a+c)
# hii()



'''global scope - value can be assigned inside as well as outside the function,
                  if the value present in both local nd global scope first it will performance to local'''

# a=2
# def nr():
#     a=4
#     b=5;c=6
#     print(a)
#     print(b)
# print(a)
# nr()
# print(a)



'''local variable as global variable - first we have to declare as global'''
'''if we want to use local variable as global have to declare as global in function,
but first function should be called then only we can use local as global'''

# a=4
# def nv():
#     b=2
#     global a,c
#     a=6;c=8
#     print(b)
#     print(c)
# print(a)
# nv()
# print(a);print(c);print(a)


'''count the length of a string without using built-in function(len())'''

# def hii(name):
#     a=0
#     for i in name:
#         a+=1
#     return a;
# print(hii('niharika'))
    
    

'''function to return sum value'''

# def sum():
#     a=int(input())
#     b=int(input())
#     c=a+b
#     return c       ''' if we need only one single output we can use return c '''
#     return 'the value of {}+{} is {}'.format(a,b,c)   ''' but if we want clear clarification we can use this '''
# print(sum())



'''function definition'''

# def sum(a,b):
#     c=a+b
#     print(c)
# def subm(a,b):
#     d=a-b
#     e=a*b
#     print(d,e)
# a=int(input())
# b=int(input())
# sum(a,b)
# subm(a,b)


'''we can do sum & sub in one part'''

# def sum_sub(a,b):
#     c=x+y
#     d=x-y
#     return c,d
# x=int(input())
# y=int(input())
# c,d=sum_sub(x,y)
# print(c,d)
# print('the sum of a+b is',c,'the sub of a-b is',d)
# print(f'the value of {x}+{y} is {c} and the value of {x}-{y} is {d}')


'''we can do sum,sub,mul,div in one part'''

# def sn(x,y):
#     a=x+y
#     b=x-y
#     c=x*y
#     d=x/y
#     return a,b,c,d
# m=int(input())
# n=int(input())
# nr=sn(m,n)
# print(nr)
# print(*nr)
# for i in nr:print(i)

'''sorting group numbers'''
