from __future__ import unicode_literals

import redis


# fill in the following.
HOST = "redis-19674.c92.us-east-1-3.ec2.cloud.redislabs.com"
PWD = "WYi2cEXgyPf4qFB5sLBw6qjiEmGwekQH"
PORT = "19674" 

# HOST = "redis-11363.c1.asia-northeast1-1.gce.cloud.redislabs.com"
# PWD = "1nOA0St0I7p9pQqu8HkQ18XqDfnoPeoL"
# PORT = "11363" 

redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)


while True:
    msg = input("Please enter your query (type 'quit' or 'exit' to end):").strip()
    if msg == 'quit' or msg == 'exit':
        break
    if msg == '':
        continue
    print("You have entered " + msg, end=' ') 

   
    # Add your code here
    counter = 0
    
    if redis1.get(msg) is not None:
        counter = int(redis1.get(msg))


    value = 1 + counter
    redis1.set(msg, value)
 
    
    print('for ' +str(value)+ ' times')
  
