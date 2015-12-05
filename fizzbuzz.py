# -*- coding: utf-8 -*-
__author__ = 'Paschaleris Triantafyllos'

'''
FizzBuzz Challenge Description:
    Based on a traditional English children's game
    Print the numbers 1..100
    For multiples of 3, print "Fizz" instead of the number
    For multiples of 5, print "Buzz" instead of the number
    For multiples of 3 and 5, print "FizzBuzz" instead of the number
    Extra: Print a new line after each case
'''

##########
#First Try. Keeping it simple and readable
##########
def firstTry():
    for i in range(1, 101):
        if i%15 == 0:
            print("FizzBuzz\n")
            continue
        if i%3 == 0:
            print("Fizz\n")
            continue
        if i%5 == 0:
            print("Buzz\n")
            continue
        print(str(i) + '\n')
##########
#Second Try. The Error way! (more like 'The WTF Way'!)
##########
def secondTry():
    arrayy = [1-15, 2-15, 'Fizz', 4-15, 'Buzz', 'Fizz', 7-15, 8-15, 'Fizz', 'Buzz', 11-15, 'Fizz', 13-15, 14-15, 'FizzBuzz'] # It' the list with the first 15 elements to be printed, just subtracting 15 from each number, because of the first iteration below
    for j in range(7):
        for i in range(len(arrayy)):
            if j*15+i>99 : return
            try:
                arrayy[i] += 15
                print(arrayy[i])
            except TypeError: # String + Number throws this error
                print(arrayy[i])
            finally:
                print()


#########################
#  RUNNING
#########################
import timing # With the import the time starts counting!
firstTry()
firstTryTime = timing.log("Finished First Try")
secondTry()
secondTryTime = timing.log("Finished Second Try", firstTryTime)


#########################
# RESULTS
#########################
print("Difference between First and Second Try")
diff_1_2 = secondTryTime-firstTryTime
print('Exact time: ', secondTryTime-firstTryTime)
print('Rounded time: ', timing.secondsToStr(secondTryTime-firstTryTime))