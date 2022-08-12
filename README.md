# sequences

## About sequences
sequences is a simple Mathematical Module providing access to the most famous of sequences from the On-Line Encyclopedia of International Sequences (OEIS) as callables. Help text is included for each function so that the user gets an idea of what to expect as the output to each function.

## Examples of functions provided

- whole(n)
    > [0, 1, 2, 3, ..., n]
- prime(n)
    > [2, 3, 5, 7, 11, ...]
- fibonacci(n)
    > [0, 1, 1, 2, 3, ..., sum(F(n-1), F(n-2))]
- tribonacci(n)
    > [0, 1, 1, 2, 4, ..., sum(T(n-1), T(n-2), T(n-3))]
- recaman(n)
    > [0, 1, 3, 6, 2, ...] \
    > T(n) = 0 if n == 0 \
    > T(n) = T(n-1) - n if positive and not already in sequence \
    > T(n) = T(n-1) + n otherwise
- van_eck(n)
    > [0, 0, 1, 0, 2, ...] \
    > T(n) = 0 if n == 0 \
    > T(n) = 0 if T(n-1) is a new number \
    > T(n) = x if T(n) occured x steps earlier in the sequence

And many more... To access the names of all the functions, run:

```
dir(sequences)
```

To access the help-text for any function to know more about it, run:

```
help(function_name)
```

## Update History

### Updates (0.0.5)

Minor bug fixes

### Updates (0.0.6)

Added the following (non-exhaustive) list of new sequences:
- catalan(n)
    > [1, 1, 2, 5, 14, ..., comb(2n, n) / (n+1)]
- cantral_polygon(n)
    > [1, 2, 4, 7, 11, ..., (pow(n, 2) + n+2) / 2]

### Updates (0.0.7)

Added the following (non-exhaustive) list of new sequences:
- lucas(n)
    > [2, 1, 3, 4, 7, ..., sum(L(n-1), L(n-2))]
- negalucas(n)
    > [2, -1, 3, -4, 7, ..., pow(-1, n) * L(n)]
- euclid_mullin(n)
    > [2, 3, 7, 43, 13, ...] \
    > T(n) = 2 if n == 1 \
    > T(n) = smallest prime factor of product(euclid_mullin(n)) + 1 otherwise
- central_binomial(n)
    > [1, 2, 6, 20, 70, ..., comb(2n, n)]

### Updates (0.0.8)
Minor bug fixes

## Footnotes

The function `check(n)` is not meant for use.
