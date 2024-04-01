## Solutions to Chapter 2.3:
1. Sequence: $0, 2, 6, 12, 20, ...$\
Difference 1: $2, 4, 6, 8, ...$\
Difference 2: $2, 2, 2, ...$\
The second differnce is a constant number therefore the sequence is a $\Delta^2$-constant.\
So we know the polynomial is to the second degree, and now we can solve for the a, b, and c terms:
$$
a_n = an^2 + bn + c\\
a_0 = 0 = a*0^2 + b*0 + c
0 = c
$$

Now we know that $c = 0$, now we need to find a and b.\
First we solve using $n = 1$ and $n = 2$.
$$
a_1 = 2 = a*1^2 + b*1 + 0\\
2 = a + b\\
\\
a_2 = 6 = a*2^2 + b*2 + 0
6 = 4a + 2b
$$

Now you can solve for a and b:
$$
b = 2 - a\\
=>  
6 = 4a + 2(2 - a)\\
6 = 4a + 4 - 2a\\
2 = 2a\\
a = 1\\
=>  
2 = 1 + b\\
b = 1\\
$$

Now that we know the values for a, b, and c we can write the equation in terms of n, which is the following:
$$ 
a_n = 1*n^2 + 1*b + 0\\
a_n = n^2 + n
$$

6. We can tell the equation is quadratic by the difference between the numbers being increasing by two each time.\\
My Guess for the answer is going to be $a_n = a^2 - n + 1$

Note: 6-9 are stupid, it tells you to guess the answer when you have a perfecttly good way to solve it. It tells you to basically not show your work.

10. No. You can't do this because after looking at the differences you will notice that you will never end up with a constant.

11. No. The sequence is not a polynomial but geometric instead.
