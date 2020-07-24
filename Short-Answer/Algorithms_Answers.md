#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Looks like this is 0(n). This will run an amount of times equal to the value of n


b)this looks like O(nlogn). The first loop, for i in n is O(n) runtime complexity, and as long as n is >4, the while loop with j will always terminate before i is finished running. So for the most part, the 2nd loop is O(logn) runtime. Worse case, if n is <2, then the runtime is O(n^2) because then it is both iterating and running the while loop simultaneously. 


c) This is exponential time, O(2^n), recursive function holding variables and storing them

## Exercise II

I believe this is a log(n) runtime solution. You basically cut the distance from the top floor to the bottom floor in half, and drop the egg from the middle floor. So basically you start at floor N/2. If the egg breaks, you know it will break at all floors above F(N/2), and so you cut this in half again. So say you start at floor 100, you jump to 50, test the egg. If it breaks, you drop to floor 25. If it doesnt break, you jump halfway back up to floor 37. If it breaks at 37, you go to floor (37+25)/2 or 31 and test there. You continually cut the distance in half between the floor you are on and the previous cutoff point where the egg did or did not break, until you find the floor it broke on. 


