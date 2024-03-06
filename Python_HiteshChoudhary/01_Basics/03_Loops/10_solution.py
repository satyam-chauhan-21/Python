#-------------------------------------------------------------------------------#
#                          10. Exponential Backoff
#-------------------------------------------------------------------------------#
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

'''
exponential backoff strategy : ye ek program hai jo APIs or dusre work ko wait karane me use hota hai.
'''
import time

wait_time = 1 # here wait_time is value in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attemps", attempts + 1, "-wait time",wait_time)
    time.sleep(wait_time)
    wait_time = wait_time * 2 # this line increace wait_time exponentially
    attempts = attempts + 1

# here time.sleep(time_in_seconds) : used for stop program exetion for given seconds
'''
loop execution : in this loop attempts is used as iterator
    first iteration : 
        attempts = 0, wait_time = 1
        loop condition attempts(0) < max_retries(5) => becomes true
        program stoped for 1 second
    second iteration :
        attempts = 1, wait_time = 2
        loop condition attempts(1) < max_retries(5) => becomes true
        program stoped for 2 second
    third iteration :
        attempts = 2, wait_time = 4
        loop condition attempts(2) < max_retries(5) => becomes true
        program stoped for 4 second
    fourth iteration :
        attempts = 3, wait_time = 8
        loop condition attempts(3) < max_retries(5) => becomes true
        program stoped for 8 second
    fifth iteration :
        attempts = 4, wait_time = 16
        loop condition attempts(4) < max_retries(5) => becomes true
        program stoped for 16 second
    sixth iteration :
        attempts = 5, wait_time = 16
        loop condition attempts(5) < max_retries(5) => becomes False
        
        loop ends & program ends.

'''