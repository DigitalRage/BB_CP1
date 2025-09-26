# BB 1st Debugging Notes 

# Syntax Error - grammar error
# print"Vienna"
# => Read error message, go to that line of code, fix the syntax

# Logic Errors - We gave the wrong steps
numone = "2"
numtwo = "5"

print(numone+numtwo)

# Have a well thought out plan, Step by step go through our logic 

# Run-time Error - it ends with num/0
import random
import time

while True:
    time.sleep(0.05)
    denominator = random.randint(1,5)

    print(10/denominator)