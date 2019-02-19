import math, pygame, sys
from math import factorial, sqrt
from pygame import *

pygame.init()
clock = pygame.time.Clock()
Font = pygame.font.SysFont("Courier New",20,True,False)

#Extra fun
def choose(n,k):
    #nCk = n! / k!(n-k)!
    coff = factorial(float(k)) * factorial(n-k)
    coff = factorial(float(n)) / coff

    return coff

print("For a negative it is binomial distribution with a fix number of successes")
r = input("Input the number of success(r): ")
p = input("Input the probabilty of one trial being successful(p): ")
x = input("Input the number of trials: ")

#Equation
q = 1 - float(p)

#Part of the formula and what it is

numFails = float(x)-float(r)

coff = choose(float(x)-1,float(r)-1)

suc = pow(float(p),float(r))

fails = pow(q,numFails)

ans = coff * suc * fails

#Mean, Var & SD
mean = float(r) / float(p)
var = float(r) * q
var = var / pow(float(p),2)
SD = sqrt(var)

#Output
print("The mean is: " + str(mean))
print("The variance is: " + str(mean))
print("The SD is: " + str(mean))
print("The probability: " + str(ans))
print("The probability %: " + str(ans*100) + "%")
input("More information: ")
print("The combination of draws: " + str(coff))
print("The number of sucess: " + str(suc))
print("The number of failures: " + str(fails))
input("Draw: ")

screen = pygame.display.set_mode((452, 301),0,32)
background = pygame.image.load("graph.png").convert(32)
pygame.display.set_caption("Graphing")

x = []

index = int(r)
while index != 16:
    x.append(index)
    index += 1

for i in x:
    print(i)

rects = []
#248
for i in x:
    numFails = float(i)-float(r)
    coff = choose(float(i)-1,float(r)-1)
    suc = pow(float(p),float(r))
    fails = pow(q,numFails)
    ans = coff * suc * fails
    rects.append(pygame.Surface((25, 248 * ans)))

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
        screen.blit(rects[i-int(r)], (52 + 25*i, 248 - rects[i-int(r)].get_height()) )

    screen.blit(meansur,(320,0))
    screen.blit(varsur,(320,25))
    screen.blit(sdsur,(320,50))

    clock.tick()
    pygame.display.update()
