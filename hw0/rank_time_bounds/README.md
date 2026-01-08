# Rank Time Bounds
## Problem Description
Rank various time bounds (functions of input size $n$, e.g., $n^2$, $2^n$) in order of their asymptotic growth rates. The functions will be given as LaTeX-like code, e.g.,

```
(0) log n

(1) 2 log n

(2) 1

(3) 2^n
```

You will rank them by uploading a text file with the proper nondecreasing order of asymptotic growth rates. Assume all logarithms are base 2. Some time bounds may have the same asymptotic growth rate, in which case listing them in either relative order would be considered correct. More precisely, a correct ordering $f_1, f_2, \dots$ satisfies $f_i = O(f_{i+1})$ for all $i$. In the above example, since $1 = o(\log n)$, $\log n = \Theta(2 \log n)$, and $\log n = o(2^n)$, there are two correct solutions:

```
2 0 1 3
```

and

```
2 1 0 3
```

## Code Instructions
Pure theory. No code available.