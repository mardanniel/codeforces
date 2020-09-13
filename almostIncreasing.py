# Given a sequence of integers as an array, determine whether it is possible 
# to obtain a strictly increasing sequence by removing no more than one 
# element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
# if a0 < a1 < ... < an. Sequence containing only one element is also 
# considered to be strictly increasing.

def almostIncreasingSequence(sequence):
    count = 0
    for i in range(len(sequence)):
        if count >= 2:
            return False        
        elif sequence[i] > sequence[i-1]:
            count = count + 1
    return True
        

print(almostIncreasingSequence([1,2,3,1]))