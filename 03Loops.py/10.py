# # 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time 

attempt = 0
max_retries = 5
wait_time=1

while attempt < max_retries:
    print("attempt", attempt+1 ,",", "retry left", max_retries-attempt-1 , "and time taken", wait_time )
    time.sleep(wait_time)
    attempt += 1
    wait_time *= 2    
    
