# Python Challenges 100 Tasks

## Recursive

### 1:Factorial

> Mathematically, the factorial for a positive number n is defined as the product
(i. e., the multiplication) of all natural numbers from 1 to n, inclusive.

$n! = n ∗ (n − 1) ∗ (n − 2) ∗ ... ∗ 2 ∗ 1$

$
n! = 
\begin{cases} 
1 & \text{if } n = 0 \text{ or } n = 1 \\
n \cdot (n-1)! & \forall n > 1 
\end{cases}
$

### Sum of Numbers Up to `n`

> Mathematically, the *sum* for a number \(n\) is defined as the addition of all natural numbers from 1 ascending up to and including \(n\):

$
\sum_{i=1}^{n} i = n + (n-1) + (n-2) + \dots + 2 + 1
$

> This can be defined recursively as follows:

$
\sum_{i=1}^{n} i =
\begin{cases} 
1 & \text{if } n = 1 \\
n + \sum_{i=1}^{n-1} i & \forall n > 1 
\end{cases}
$


> Optimized calculation of the sum 

$
\sum_{i=1}^{n} i = \frac{(n+1) \cdot n}{2}
$

### Fibonacci

> That’s why you can only pass inputs around 990 here. Larger values will
result in a `RecursionError:` maximum recursion depth exceeded.

$
fib(n) = 
  \begin{cases}
    1, & n=1 \\
    1, & n=2 \\
    fib(n-1)+fib(n-2), & n>2
  \end{cases}
$

### palindrome

> *Algorithm* 
- If the array or list has the length 0 or 1, 
- then it is a palindrome by
definition. 
- If the length is two and greater, 
- you must check the outer left and outer right
elements for a match. 
- After that, a copy of the array or the list is created, 
- shortened by
one position at the front and one at the back. 
- Further checking is then performed on the
remaining part of the array or the list, 


