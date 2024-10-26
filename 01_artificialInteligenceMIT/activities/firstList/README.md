# First list

## 1. Running the code

To run the offiline tester, just use `python3 tester.py`

## 2. Warmup activies

1. `cube(n)`, which takes in a number and returns its cube. For example, cube(3) => 27.
2. `factorial(n)`, which takes in a non-negative integer n and returns n!, which is the product of
the integers from 1 to n. (0! = 1 by definition.)
3. `count_pattern(pattern lst)`, which counts the number of times a certain pattern of
symbols appears in a list, including overlaps. So `count_pattern( ('a', 'b'), ('a',
'b', 'c', 'e', 'b', 'a', 'b', 'f'))` should return 2, and
`count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a',
'b', 'a'))` should return 3.

## 3. Actual activities

### 3.1 Expression depth

One way to measure the complexity of a mathematical expression is the depth of the expression
describing it in Python lists. Write a program that finds the depth of an expression.

For example:

- `depth('x') => 0`
- `depth(('expt', 'x', 2)) => 1`
- `depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))) => 2`
- `depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))) => 4`

