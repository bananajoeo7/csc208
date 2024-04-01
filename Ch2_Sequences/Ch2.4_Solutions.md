## Solutions to Chapter 2.4:
1. 
Initial Sequence: $3, 5, 11, 21, 43, 85, ...$\
Difference in Sequence pt: $2, 6, 10, 22, 42, ...$\
$2, 2 + 2(2), 6 + 2(2), 10 + 6(2), 22 + 10(2), ...$\
$a_0 = 3$ and $a_1 = 5$

We notice that the sequence is growing in factors of 2 times the previous number.\
Therefore we can assume that the recurrence relation is: $a_n = a_{n - 1} + 2_{n - 2}$
This gives us 171 and 341 as the next terms.

Then we can use Characteristic Root Technique:
$$a_n = a_{n - 1} + 2_{n - 2}$$
Giving the charactersistic polynomial:
$$x^2 - x - 2 = 0$$
Then Factor:
$$(x - 2)(x + 1)$$
Now we know the roots:
$$x = -1, 2$$

I'm stuck after this.

3. 

10. 

12. 
