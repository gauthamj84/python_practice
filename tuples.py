# tuples.py 
# tuples usage example program
# A tuple consists of a number of values separated by commas
# tuples can be nested as well

t = 12345, 54321, 'hello!'
print t[0]
# 12345
print t
#(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))