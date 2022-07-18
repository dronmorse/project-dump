#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy
import copy

def randomwalk(a,b,c,x,m):
        
    movement =  10000

    probability = 0.57

    perpendicular = 5 
    parallel = 5

    perpendicular2 = 15
    parallel2 = 15
    
    perpy = []
    parax = []

    perpy2 = []
    parax2 = []
   
    perpy3 = []
    parax3 = []

    generated = []
    generated2 = []
    generated3 = []

    arraylen = 1
    arraylen2 = 1
    arraylen3 = 1
    
    count = 0

    switch = 0

    matrix = numpy.zeros((20,20))
    matrix2 = numpy.zeros((20,20))
    matrix3 = numpy.zeros((20,20))

    while count < movement and switch != 1:
        f = a*x%m
        generated.append(f)
        if f/(m*probability) > 1:
            print ('no king movement')
        elif f/(m*0.67) < 1:
            f1 = f*x%m
            if f1/(m*0.25) < 1:
                print ('king moves up')
                perpendicular += 1
                if perpendicular > 20:
                    perpendicular = 0
            if f1/(m*0.25) < 2 and f1/(m*0.25) > 1:
                print ('king moves down')
                perpendicular -= 1
                if perpendicular < 0:
                    perpendicular = 20
            if f1/(m*0.25) < 3 and f1/(m*0.25) > 2:
                print ('king moves left')
                parallel -= 1
                if parallel < 0:
                    parallel = 20
            if f1/(m*0.25) < 4 and f1/(m*0.25) > 3:
                print ('king moves right')
                parallel += 1
                if parallel > 20:
                    parallel = 0
            print ("position: ", perpendicular, parallel)
        elif f/(m*0.67) > 1:
            f1 = f*x%m
            if f1/(m*0.25) < 1 :
                print ('king moves diagonally rightup')
                perpendicular += 1
                parallel += 1
                if perpendicular > 20:
                    perpendicular = 0
                if parallel > 20:
                    parallel = 0
            if f1/(m*0.25) < 2 and f1/(m*0.25) > 1:
                print ('king moves diagonally leftup ')
                perpendicular += 1
                parallel -= 1
                if perpendicular > 20:
                    perpendicular = 0
                if parallel < 0:
                    parallel = 20
            if f1/(m*0.25) < 3 and f1/(m*0.25) > 2:
                print ('king moves diagonally rightdown')
                perpendicular -= 1
                parallel += 1
                if perpendicular < 0:
                    perpendicular = 20
                if parallel > 20:
                    parallel = 0
            if f1/(m*0.25) < 4 and f1/(m*0.25) > 3:
                print ('king moves diagonally leftdown')
                perpendicular -= 1
                parallel -= 1
                if perpendicular < 0:
                    perpendicular = 20
                if parallel < 0:
                    parallel = 20
            print ("position: ", perpendicular, parallel)
        
        a = f
        parax.append(parallel)
        perpy.append(perpendicular)
        matrix[perpendicular-1][parallel-1] += 1
        
        f2 = b*x%m
        generated2.append(f2)
        if f2/(m*probability) > 1:
            print ('no queen movement')
        elif f2/(m*0.67) < 1:
            f3 = f2*x%m
            if f3/(m*0.25) < 1:
                print ('queen moves up')
                perpendicular2 += 1
                if perpendicular2 > 20:
                    perpendicular2 = 0
            if f3/(m*0.25) < 2 and f3/(m*0.25) > 1:
                print ('queen moves down')
                perpendicular2 -= 1
                if perpendicular2 < 0:
                    perpendicular2 = 20
            if f3/(m*0.25) < 3 and f3/(m*0.25) > 2:
                print ('queen moves left')
                parallel2 -= 1
                if parallel2 < 0:
                    parallel2 = 20
            if f3/(m*0.25) < 4 and f3/(m*0.25) > 3:
                print ('queen moves right')
                parallel2 += 1
                if parallel2 > 20:
                    parallel2 = 0
            print ("position: ", perpendicular2, parallel2)
        elif f2/(m*0.67) > 1:
            f3 = f2*x%m
            if f3/(m*0.25) < 1:
                print ('queen moves diagonally rightup')
                perpendicular2 += 1
                parallel2 += 1
                if perpendicular2 > 20:
                    perpendicular2 = 0
                if parallel2 > 20:
                    parallel2 = 0
            if f3/(m*0.25) < 2 and f3/(m*0.25) > 1:
                print ('queen moves diagonally leftup ')
                perpendicular2 += 1
                parallel2 -= 1
                if perpendicular2 > 20:
                    perpendicular2 = 0
                if parallel2 < 0:
                    parallel2 = 20
            if f3/(m*0.25) < 3 and f3/(m*0.25) > 2:
                print ('queen moves diagonally rightdown')
                perpendicular2 -= 1
                parallel2 += 1
                if perpendicular2 < 0:
                    perpendicular2 = 20
                if parallel2 > 20:
                     parallel2 = 0
            if f3/(m*0.25) < 4 and f3/(m*0.25) > 3:
                print ('queen moves diagonally leftdown')
                perpendicular2 -= 1
                parallel2 -= 1
                if perpendicular2 < 0: 
                    perpendicular2 = 20
                if parallel2 < 0:
                    parallel2 = 20
            print ("position: ", perpendicular2, parallel2)
        
        b = f2
        count += 1

        if parallel == parallel2 and perpendicular == perpendicular2:
            switch += 1
            print ("particles met!", "step: ", count)
        
        parax2.append(parallel2)
        perpy2.append(perpendicular2)
        matrix2[perpendicular2-1][parallel2-1] += 1
    
    meeting = copy.deepcopy(count)
    parallel3 = parallel2
    perpendicular3 = perpendicular2

    for i in range (0,movement-count):
        f4 = c*x%m
        generated3.append(f4)
        if f4/(m*probability) > 1:
            print ('no simultaneous movement')
        elif f4/(m*0.67) < 1:
            f5 = f4*x%m
            if f5/(m*0.25) < 1:
                print ('together moves up')
                perpendicular3 += 1
                if perpendicular3 > 20:
                    perpendicular3 = 0
            if f5/(m*0.25) < 2 and f5/(m*0.25) > 1:
                print ('together moves down')
                perpendicular3 -= 1
                if perpendicular3 < 0:
                    perpendicular3 = 20
            if f5/(m*0.25) < 3 and f5/(m*0.25) > 2:
                print ('together moves left')
                parallel3 -= 1
                if parallel3 < 0:
                    parallel3 = 20
            if f5/(m*0.25) < 4 and f5/(m*0.25) > 3:
                print ('together moves right')
                parallel3 += 1
                if parallel3 > 20:
                    parallel3 = 0
            print ("position: ", perpendicular3, parallel3)

        elif f4/(m*0.67) > 1:
            f5 = f4*x%m
            if f5/(m*0.25) < 1 :
                print ('together moves diagonally rightup')
                perpendicular3 += 1
                parallel3 += 1
                if perpendicular3 > 20:
                    perpendicular3 = 0
                if parallel3 > 20:
                    parallel3 = 0
            if f5/(m*0.25) < 2 and f5/(m*0.25) > 1:
                print ('together moves diagonally leftup ')
                perpendicular3 += 1
                parallel3 -= 1
                if perpendicular3 > 20:
                    perpendicular3 = 0
                if parallel3 < 0:
                    parallel3 = 20
            if f5/(m*0.25) < 3 and f5/(m*0.25) > 2:
                print ('together moves diagonally rightdown')
                perpendicular3 -= 1
                parallel3 += 1
                if perpendicular3 < 0:
                    perpendicular3 = 20
                if parallel3 > 20:
                    parallel3 = 0
            if f5/(m*0.25) < 4 and f5/(m*0.25) > 3:
                print ('together moves diagonally leftdown')
                perpendicular3 -= 1
                parallel3 -= 1
                if perpendicular3 < 0:
                    perpendicular3 = 20
                if parallel3 < 0:
                    parallel3 = 20
            print ("position: ", perpendicular3, parallel3)
        
        c = f4
        parax3.append(parallel3)
        perpy3.append(perpendicular3)
        matrix3[perpendicular3-1][parallel3-1] += 1
    

    print ('array particle1')        
    for i in matrix:
        print (i)

    print ('array particle2')
    for i in matrix2:
        print (i)
    
    print ('array simultanous')
    for i in matrix3:
        print (i)

    for i in generated[1:]:
        root = generated[0]
        if i == root:
            break
        else:
            arraylen += 1

    for i in generated2[1:]:
        root = generated2[0]
        if i == root:
            break
        else:
            arraylen2 += 1

    for i in generated3[1:]:
        root = generated3[0]
        if i == root:
            break
        else:
            arraylen3 += 1

    

    if arraylen3 == 1:
        arraylen3 = 0
    
    file = open('matrices.txt', 'w')

    file.write('array of particle1 movement')
    file.write('\n')
    for i in matrix:
        file.write(str(i))
        file.write('\n')
    file.write('array of particle2 movement')
    file.write('\n')
    for i in matrix2:
        file.write(str(i))
        file.write('\n')
    file.write('array of simultanous movement')
    file.write('\n')
    for i in matrix3:
        file.write(str(i))
        file.write('\n')
    file.write('random for particle1')
    file.write('\n')
    file.write(str(generated))
    file.write('\n')
    file.write('single array particle1 length: ')
    file.write(str(arraylen))
    file.write('\n')
    file.write('random for particle2')
    file.write('\n')
    file.write(str(generated2))
    file.write('\n')
    file.write('single array particle2 length: ')
    file.write(str(arraylen2))
    file.write('\n')
    file.write('random for simultanous')
    file.write('\n')
    file.write(str(generated3))
    file.write('\n')
    file.write('single array together length: ')
    file.write(str(arraylen3))

    file.close()

    if meeting == movement:
        print ('particles didnt meet')
    else:
        print ("particles met at: ", meeting)
    print ("number of steps: ", movement)

    plt.scatter(parax,perpy, c='b', marker='o')
    plt.scatter(parax2,perpy2, c='r', marker = 'x')
    plt.scatter(parax3,perpy3, c='g', marker = '.')
    plt.show()
    
randomwalk(16807,16808,16809,12369123,2147483647)
