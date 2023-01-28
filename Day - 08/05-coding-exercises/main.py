# Coding Exercise 1

# Note: This is a very challenging exercise. Do not worry if you can't get it right. 
# Just try to code until you get bored. The sole experience of trying to code helps your learning a ton.

# A client wants to buy a coin-flip probability program from you.
# The programs should work like this:
# 1. The user runs the program. The program asks the user to enter "head" or "tail".  
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". 
# The user does the same over and over again. 

# Throw the coin and enter head or tail here: ? tail
# Heads: 0.0%
# Throw the coin and enter head or tail here: ? head
# Heads: 50.0%
# Throw the coin and enter head or tail here: ? head
# Heads: 66.66666666%
# Throw the coin and enter head or tail here: ? tail
# Heads: 50.0%
# Throw the coin and enter head or tail here: ? 

# In each cycle, the program should return the current percentage of heads in the program, 
# similar to what you see in the screenshot above. Also, you should write each user entry 
# (i.e., head or tail) in a text file using a with-context manager, one entry per line.