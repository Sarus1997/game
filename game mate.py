import random
number = [1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.]
operator = ['+','-','*','/']
correct = True
score = 0
while correct:
    num1 = random.sample(number,1)
    num2 = random.sample(number,1)
    op = random.sample(operator,1)
    print(num1[0], op[0], num2[0])
    ans = input("Enter answer :")
    if op[0] == '+':
        result = num1[0] + num2[0]
    elif op[0] == '-':
        result = num1[0] - num2[0]
    elif op[0] == '*':
        result = num1[0] * num2[0]
    elif op[0] == '/':
        result = num1[0] / num2[0]
    if result == ans:
        correct = True
        score +=1
        print("Correct..good job")
    else:
        correct = False
        print("Incorrect ..")
        print ("Game over")
        print("Your scores :",score)