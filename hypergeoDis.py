import math, pygame, sys
from math import factorial
from pygame import *
pygame.init()
clock = pygame.time.Clock()

#Extra fun
def choose(n,k):
    #nCk = n! / k!(n-k)!
    coff = factorial(float(k)) * factorial(n-k)
    coff = factorial(float(n)) / coff

    return coff

print("For a hypergeometric it is binomial distribution with non replacement")
N = input("Input the total population size(N): ")
K = input("Input the number of success that could happen(K): ")
n = input("Input the the number of draws from the poulation(n): ")
k = input("Input the the number of successful draws, main variable(k): ")

#Working out the values that were successful
kArr = list(k)

#Equation
#N-K is the number of number of fails in the poulation
#n-k is the number of number of draws that could be unsuccessful
#KCk * N-KCn-k / NCn

failPop = float(N)-float(K)
failDraw = float(n)-float(k)

combOfSuc = choose(float(K) , float(k))
combOfFail = choose( failPop , failDraw)
combOfWhole = choose(float(N) , float(n))
ans = combOfSuc * combOfFail / combOfWhole

#Mean, Var & SD
mean = float(K)  * float(n) / float(N)

#Output
print("The mean is: " + str(mean))
print("The probability: " + str(ans))
print("The probability %: " + str(ans*100) + "%")
input("More information: ")
print("The combination of success: " + str(combOfSuc))
print("The combination of fails: " + str(combOfFail))
print("The combination of samples from the population: " + str(combOfWhole))
input("Draw: ")

screen = pygame.display.set_mode((452, 301),0,32)
background = pygame.image.load("graph.png").convert(32)
pygame.display.set_caption("Graphing")

x = []

for i in range(int(k)):
    x.append(i)

rects = []
#248
for i in x:
    failPop = float(N)-float(K)
    failDraw = float(n)-float(i)

    combOfSuc = choose(float(K) , float(i))
    combOfFail = choose( failPop , failDraw)
    combOfWhole = choose(float(N) , float(n))
    ans = combOfSuc * combOfFail / combOfWhole

    rects.append(pygame.Surface((25, 248 * ans)))

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
