import functools
import turtle
def factorial(n):
    return functools.reduce(lambda n_1, n: n_1 * n, range(1, n + 1))

def sum_of(n):
    return  functools.reduce(lambda n_1, n: n_1 + n, range(1, n + 1))

def optimized_sum_of(n):
    return (n * (n + 1)) // 2

def optimized_sum(n):
    return functools.reduce(lambda x, y: x + y, range(1, n + 1))

def factorial_default(n):
    if n < 0:
        raise ValueError("n must be >=0")
    # recursive termination
    if n == 0 or n == 1:
        return 1
    # recursive descent
    return n * factorial_default(n-1)

def sum_of_default(n):
    if n <= 0:
        raise ValueError("n must be >= 1")
    # recursive termination
    if n == 1:
        return 1
    # recursive descent
    return n + sum_of_default(n - 1)

def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def palindrome_simple(values):
    # recursive termination
    if len(values) <= 1:
        return True
    left = 0
    right = len(values) - 1
    if values[left] == values[right]:
        # attention: end is exclusive
        remainder = values[left + 1 : right]
        # recursive descent
        return palindrome_simple(remainder)
    return False

def palindrome_optimized(values):
    return palindrome_in_range(values, 0, len(values) - 1)

# include two position markers left and right
# initially span entire
def palindrome_in_range(values, left, right):
    # recursive termination
    if left >= right:
        return True
    # if the left and right values referenced by these positions match
    if values[left] == values[right]:
        # recursive descent
        # markers are moved inward by one
        return palindrome_in_range(values, left + 1, right - 1)
    return False

def palindrome_iterative(values):
    left = 0
    right = len(values) - 1
    same_value = True
    while left < right and same_value:
        same_value = values[left] == values[right]
        left += 1
        right -= 1
    return same_value

# any recursive algorithm can be converted into an iterative one
#
def palindrome_iterative_compact(values):
    # use two position pointers instead of the recursive descent
    left = 0
    right = len(values) - 1
    while left < right and values[left] == values[right]:
        left += 1
        right -= 1
    # left >= right or values[left] != values[right]
    return left >= right

# an inverse variant of the original list is generated
# memory required twice
def palindrome_short(values):
    return values == values[::-1] #built-in functionality [::-1]

def fractal_generator(n):
    if n < 1:
        return
    if n == 1:
        print("-")
    else:
        fractal_generator(n-1)
        print("=" * n)
        fractal_generator(n-1)


def multiply_all_digits(value):
    remainder = value // 10
    digit_value = value % 10
    print("multiply_all_digits: %-10d | remainder: %d, digit: %d" %
        (value, remainder, digit_value))
    if remainder > 0:
        result = multiply_all_digits(remainder)
        print("-> %d * %d = %d" % (digit_value, result, digit_value * result))
        return digit_value * result
    else:
        print("-> " + str(value))
        return value



if __name__ == '__main__':

    multiply_all_digits(346)

    #fractal_generator(8)
    # print(f'palindrome_short: {palindrome_short("ABBA")}')

    # print(f'factorial: {factorial(5)}')
    # print(f'sum_of: {sum_of(15)}')
    # print(f'optimized_sum_of: {optimized_sum_of(15)}')
    # print(f'optimized_sum: {optimized_sum(120)}')
    # print(f'fib: {fib(30)}')

