'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):


    token = "th"

   # so want to count how often "th" occurs in a word, using recursion
    if len(word) == 0:
        return 0
   # want to iterate through the word, from front to back, taking away 1 letter at a time from the front, 
   # until you reach 1 letter, at which point, terminate function, returns total count 
   #      
    if len(word) > 1 and word[0:2] == token:
        return 1 + count_th(word[1:])

    else:
        return count_th(word[1:])    


'''
def count_th(word):

    if len(word) == 0:
        return 0
    
           
    #else:
    #    word = word[:-1]
    #    count_th(word)
    
    counter = 0
    
   
    for i in range(len(word)-1, 0, -1):
    
        if  word[i] == "h"  and word[i-1] == "t":
            counter +=1
        
    return counter         
    # TBC
'''