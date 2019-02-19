import math, pygame, sys
from math import e, factorial, sqrt
from pygame import *

pygame.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont("Courier New",20,True,False)

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

print("Input if it is the distribution of trails(T) OR the distribution of fails(F)")
flag = input()
print("Please input the probability of one successs")
p = input()
print("Then the required value(s)(k).")
print("It can be just a number, inequality or a list")
print("Use <,>,≤,≥ for the inequalities")
k = input()

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
q = 1 - float(p)
for i in values:
    if flag.lower() == "t":
        num = float(i)-1
        val = q**num
        val = val * float(p)
        ans.append(val)
    else:
        val = q**float(i)
        val = val * float(p)
        ans.append(val)

#Total Prob
sumP = 0
for i in ans:
    sumP = sumP + i

if moreFlag:
    sumP = 1 - sumP

if flag.lower() == "t":
    mean = 1 / float(p)
else:
    mean = q / float(p)

#Var and SD is the same for both of them
var = q / pow(float(p),2)
SD = sqrt(var)

#Output
print("The mean is: " + str(mean))
print("The varience is: " + str(var))
print("The SD is: " + str(SD))
print("The values of k are: ")
index = 1
for i in values:
    print("k" + str(index) + ": " + str(i) + "The value was: " + str(ans[index-1]))
    index = index + 1
print("Decimal: " + str(sumP))
print("Percentage: " + str(sumP*100) + "%")
input("Draw: ")

screen = pygame.display.set_mode((452, 301),0,32)

if flag.lower() == "t":
    background = pygame.image.load("graphGe.png").convert(32)
else:
    background = pygame.image.load("graph.png").convert(32)
    
pygame.display.set_caption("Graphing")

if flag.lower() == "t":
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
else:
    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

rects = []
#248
for i in x:
    if flag.lower() == "t":
        num = i-1
        val = q**num
        val = val * float(p)
    else:
        print("This2")
        val = q**i
        val = val * float(p)
    
    rects.append(pygame.Surface((25, 248 * val)))

#Making the bars one color
for i in rects:
    i.fill((10,200,10))

#Making a solid color for the value inputted
for i in values:
    if flag.lower() == "t":
        if moreFlag:
            rects[int(n) - int(i)].fill((255,0,0))
        else:
            rects[int(i)-1].fill((255,0,0))
    else:
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
        if flag.lower() == "t":
            #the i-1 in the x has to be done as it is a different image
            screen.blit(rects[i-1], (52 + 25*(i-1), 248 - rects[i-1].get_height()) )
        else:
            screen.blit(rects[i-1], (52 + 25*(i-1), 248 - rects[i-1].get_height()) )
        
    screen.blit(meansur,(320,0))
    screen.blit(varsur,(320,25))
    screen.blit(sdsur,(320,50))
    
    clock.tick()
    pygame.display.update()
