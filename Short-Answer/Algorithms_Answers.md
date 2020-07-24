#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) It looks to closely resemble Linear TIme O(n). The number of computations will run as many times as n's input size and number of times.

b) I'm going to say Logarythmi O(n^2) . We have two loops and each has to iterate over the entirety of n and then when j is less than n.

c) Linear Time O(n). Looking at it further it's recursive since it's going to decrease bunnies value by -1 for every call until bunnies reaches zero and returns itself when hitting the base case which is 0.

## Exercise II

Knowing how awesome Binary Search is, it's the first thing i'd try to make work with a problem. So i'd start on the building, floor F. IF the egg doesn't break at that height then i can rule out =< floorF. If it did break then i could cut the distance in half and toss an egg on floor C and see where the middle point is from there. If it didn't break on floorF i'd repeat the process until i found a great middle point. I'd then move onto the next half of >floorF and throw another egg.

As i keeping facotring things in, the work is halved giving me the total number of checks and eggs broken a Logarithmic time of O(log(n)). Eggs are going to break regardless, sadly but they should be minimized by cutting the checks in half each time.

<!-- # O(log(n)) or Logarithic time ↓ as we search larger lists, the runtime does not increase significantly. Halving is the giveaway.
def binary_search(arr, target):
    left = 0  # low is the pointer to the first index in the list
    right = len(arr) - 1  # high is the pointer to the last index in the list
    while left <= right:
        # find the midpoint and continue
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # check to see if the element should be on the left or right side
        # of our midpoint
        if arr[mid] < target:
            # toss out the left side of the arr
            # update our `left` index
            left = mid + 1
        # otherwise, arr[mid] > target
        else:
            # toss out the right side of the arr because the element has to be on the left side
            right = mid - 1
    return -1  # not found -->
