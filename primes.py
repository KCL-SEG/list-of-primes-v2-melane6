"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import sqrt

def _prime(primes, newNumber):
    for prime in primes:
        if sqrt(newNumber) < prime :
            return True
        elif newNumber % prime == 0:
            return False
    return True	

def primes(number_of_primes):
    primes = [2]
    newNumber = 3
    
    if number_of_primes <= 0:
        raise ValueError
       
        
    while len(primes) != number_of_primes:
        if _prime(primes, newNumber):
            primes.append(newNumber)
        newNumber+= 1
    return primes
   
    
   
    

