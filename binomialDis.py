import math, sys
from math import factorial, sqrt

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

print("Input the number of trials that happen: ")
n = input()
print("Input the number of trials that were successful: ")
k = input()
print("Input the probabilty of one trial being successful: ")
p = input()

values = []

#This is if you have a more than probality given so you can do 1-p()
moreFlag = False

#Working out the values that were successful
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

#Equation
#nCk = n! / k!(n-k)!
#nCk * p^k * (1-p)^n-k
q = 1 - float(p)

ans = []
ansCo = []
ansSuc = []
ansFai = []

#Looping the values
for i in values:
    numFails = float(n)-float(i)

    #Part of the formula and what it is
    coff = factorial(float(i)) * factorial(numFails)
    coff = factorial(float(n)) / coff

    suc = pow(float(p),float(i))

    fails = pow(q,numFails)

    ansCo.append(coff)
    ansSuc.append(suc)
    ansFai.append(fails)

    #Bin
    binomial = coff * suc * fails

    ans.append(binomial)

#Mean, Var & SD
mean = float(n)*float(p)
var = mean * q #np(1-p)
SD = sqrt(var)

#Total Prob
sumP = 0
for i in ans:
    sumP = sumP + i

if moreFlag:
    sumP = 1 - sumP

#Mean Var
print("The average number of successes would be: " + str(mean))
print("The Variance is: " + str(var))
print("The SD is: " + str(SD))
print("The binomial probability: " + str(sumP))
print("The binomial probability %: " + str(sumP * 100) + "%")
#Add extra Info
input("Would you like extra information: ")
index = 0
for i in values:
    print("Binomial coefficent when k is " + str(i) + ": " + str(ansCo[index]))
    print("Probability of successes when k is " + str(i) + ": " + str(ansSuc[index]))
    print("Probability of failure when k is " + str(i) + ": " + str(ansFai[index]))
    print("")
    index = index + 1
input("Draw: ")

import pygame
from pygame import *
pygame.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont("Courier New",20,True,False)

screen = pygame.display.set_mode((452, 301),0,32)
background = pygame.image.load("graph.png").convert(32)
pygame.display.set_caption("Graphing")

x = []

for i in range(int(n)+1):
    x.append(i)

rects = []
#248
for i in x:
    #n-k
    numFails = float(n)-float(i)

    #Part of the formula and what it is
    coff = factorial(float(i)) * factorial(numFails)
    coff = factorial(float(n)) / coff

    suc = pow(float(p),float(i))

    fails = pow(q,numFails)

    #Bin
    binomial = coff * suc * fails

    rects.append(pygame.Surface((25, 248 * binomial)))

#Making a solid color
for i in values:
    if moreFlag:
        rects[int(n) - int(i)].fill((255,0,0))
    else:
        rects[int(i)].fill((255,0,0))

meansur = Font.render("Mean = " + str(mean),True,(100,140,235))
varsur = Font.render("Var = " + str(var),True,(90,235,140))
sdsur = Font.render("SD = " + str(SD),True,(235,50,235))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    for i in x:
        screen.blit(rects[i], (52 + 25*i, 248 - rects[i].get_height()) )

    screen.blit(meansur,(320,0))
    screen.blit(varsur,(320,25))
    screen.blit(sdsur,(320,50))
    
    clock.tick()
    pygame.display.update()
