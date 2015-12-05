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
import timing # With the import the time starts counting!
##########
#First Try. Keeping it simple and readable
##########
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
firstTryTime = timing.log("Finished First Try")
