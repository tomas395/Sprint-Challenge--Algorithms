'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0  # declare the counter

    def count_doubles(word, counter):
        if len(word) < 2:  # iterate through and if it's less than 2, don't bother
            return counter
        # use the startswith method and find "th" and once it does then add +1 to the count
        elif word.startswith("th"):
            return count_doubles(word[2:], counter + 1)  # make a slice so that we iterate on the index after the "th"
        else:
            return count_doubles(word[1:], counter)  # if not then slice[1:] to hit index[2] to make sure we don't miss the next []
    return count_doubles(word, counter) 

    # no loops ehh...?
    # i'm obviously going to need to iterate over the length of each string.. NO LOOPS THO
    # i'll need to find == "th" and the .startswith() will help with that
    # i'll need to filter out everything else including just one instance of "t" or "h"
    # I'll also need to keep a count or store of all occurences of "th" somewhere in the return.
    # i can't alter the original count_th so i'll have to add another function on top of it
    # i'll want to use recursion so that if the iterations hit anything less than two characters, then stop and return to get the base case going.

