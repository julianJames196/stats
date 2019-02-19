import math, sys, pygame
from math import e, factorial, sqrt
from pygame import *
pygame.init()
clock = pygame.time.Clock()
#Extra fun
def containF(string,char):
    index = 0
    contains = False
    numAtArray = []
    for i in list(string):
        if i == char:
            contains = True
            numAtArray.append(index)
        elif contains == True and i != char:  #This is so it will remain true
            contains = True
        else:
            contains = False
        index = index + 1

    return [contains,numAtArray]


print("Please input the Mean(m)/Variance(v)/SD(s) default is mean/variance")
mean = input()
print("Then the required value(s)(k). It can be just a number, inequality or a list")
print("Use <,>,≤,≥ for the inequalities")
k = input()

#Mean, Var, SD
stringVal = list(mean)
lamS = ""
lam = 0
if stringVal[len(stringVal)-1].lower() == "s":
    del stringVal[len(stringVal)-1]
    for i in stringVal:
        lamS = lamS + i
    lam = float(lamS)**2 #This is for an input of the standard deviation
else:
    if stringVal[len(stringVal)-1].lower() == "m" or stringVal[len(stringVal)-1].lower() == "v":
        del stringVal[len(stringVal)-1]
    for i in stringVal:
        lamS = lamS + i
    lam = float(lamS)
#K values
values = []

#This is if you have a more than probality given so you can do 1-p()
moreFlag = False

kArr = list(k)

try:
    values.append(int(k))
except:
    if containF(k,",")[0] == True:
        string = ""
        for i in k:
            if i == ",":
                values.append(string)
                string = ""
            else:
                string = string + i
        values.append(string)
    else:
        #This is for inequlaities
        #Format
        index = 0
        for i in kArr:
            if i == "<":
                kArr[index] = "≤"
                kArr[index+1] = str(int(kArr[index+1]) - 1)
            if i == ">":
                kArr[index] = "≤"
                kArr[index+1] = str(int(kArr[index+1])) #-1 is not needed as, being great than a value must be the inverse as would include that value
                moreFlag = True
            if i == "≥":
                kArr[index] = "≤"
                kArr[index+1] = str(int(kArr[index+1]) - 1) #Is needed for the opposite reason as above
                moreFlag = True

            index = index + 1
                
        #Find values
        stringF = False
        num = ""
        for i in kArr:
            if stringF == True:
                num = num + i
                
            if i == "≤":
                stringF = True

        index = 0
        while index <= int(num):
            values.append(index)

            index = index + 1


#e^-m * m^k  / k!
#i is k
ans = []
for i in values:
    val = e**-float(lam)
    val = float(lam)**float(i) * val
    val = val / factorial(int(i))
    ans.append(val)

#Total Prob
sumP = 0
for i in ans:
    sumP = sumP + i

if moreFlag:
    sumP = 1 - sumP

#Output
print("The mean is: " + str(lam))
print("The values of k are: ")
index = 1
for i in values:
    print("k" + str(index) + ": " + str(i) + ", The poisson value was: " + str(ans[index-1]))
    index = index + 1
print("Decimal: " + str(sumP))
print("Percentage: " + str(sumP*100) + "%")
input("Draw: ")

screen = pygame.display.set_mode((452, 301),0,32)
background = pygame.image.load("graph.png").convert(32)
pygame.display.set_caption("Poisson")
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

rects = []
#248
for i in x:
    val = e**-float(lam)
    val = float(lam)**float(i) * val
    val = val / factorial(int(i))

    print(val)
    rects.append(pygame.Surface((25, 248 * val)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    for i in x:
        screen.blit(rects[i], (52 + 25*i, 248 - rects[i].get_height()) )

    clock.tick()
    pygame.display.update()
