def get_prime(n): # We define a recursive function to get prime numbers
    state = False # We use state to see if any other numbers can be devided into n
    for i in range(2, n): # Loop between 2 (inclusive) and n (exclusive)
        if n % i == 0: # Check if i can be devided into n
            state = True # Update state to true so we know it is not a prime
            break # Break out of the loop since we dont have to check any more numbers

    if not state: # If its not a prime
        return True # Tell the user it is a prime

    return False # Otherwise dont

    # get_prime(n + 1) # Call the function again


get_prime2 = lambda n: True if len([i for i in range(2,n) if n % i == 0]) == 0 else False
# Just having fun at this point

indx = 2
while True:
    if get_prime2(indx):
        print(indx)
    indx += 1
