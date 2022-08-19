"""sequences
Contains many of the most famous sequences of the OEIS as Python Functions
each function returns a list containing terms of the sequence"""


import math


def check(n: int) -> int:
    """checks if arg 'n' is a positive int"""

    if not isinstance(n, int):
        raise TypeError ("'n' must be an int")
    if n <= 0:
        raise ValueError ("'n' must be a positive integer")
    return n


def isprime(n: int) -> list[int]:
    """returns True if n is prime"""

    if n in range(2, 4):
        return True

    for i in range(2, int(pow(n, 0.5) + 1)):
        if not (n % i):
            return False
    return True


def whole(n: int) -> list[int]:
    """returns the first n Whole Numbers
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., n-1"""

    return list(range(check(n)))


def natural(n: int) -> list[int]:
    """returns the first n Natural Numbers
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., n"""

    return whole(check(n) + 1)[1:]


def negative(n: int) -> list[int]:
    """returns the first n Negative Numbers
    -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, ..., -n"""

    return [-i for i in natural(n)]


def square(n: int) -> list[int]:
    """returns the first n Perfect Squares
    0, 1, 4, 9, 16, 25, 36, 49, 64, 81, ..., n²"""

    return [pow(i, 2) for i in whole(n)]


def cube(n: int) -> list[int]:
    """returns the first n Perfect Cubes
    0, 1, 8, 27, 64, 125, 216, 343, 512, 729, ..., n³"""

    return [pow(i, 3) for i in whole(n)]


def prime(n: int) -> list[int]:
    """returns the first n Prime Numbers
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..."""

    n, numbers, num = check(n), [2], 3

    while len(numbers) < n:
        if num % 2:
            for i in range(3, int(num**0.5)+1):
                if not (num % i):
                    break
            else:
                numbers.append(num)
        num += 1

    return numbers


def composite(n: int) -> list[int]:
    """returns the first n Composite Numbers
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, ..."""

    n, numbers, num = check(n), [4], 6

    while len(numbers) < n:
        for i in range(2, int(num**0.5)+1):
            if not (num % i):
                numbers.append(num)
                break
        num += 1

    return numbers


def factorial(n: int) -> list[int]:
    """returns the first n Factorial Numbers
    n! = n(n-1)(n-2)...3•2•1"""

    n, numbers = check(n), [1, 1]

    if n in range(1, 3):
        return numbers[:n]

    for i in range(2, n):
        numbers.append(i * numbers[-1])

    return numbers


def palindrome(n: int) -> list[int]:
    """returns the first n Palindrome Numbers
    Palindrome Number:
        a number that remains the same when its digits are reversed"""

    n, numbers, num = check(n), list(), 0

    while len(numbers) < n:
        if str(num) == str(num)[::-1]:
            numbers.append(num)
        num += 1

    return numbers


def triangular(n: int) -> list[int]:
    """returns the first n terms of the Triangular Number Sequence
    Triangular Number:
        the count of circles arranged in an equilateral triangle with n circles
        on a side
        Tₙ = sum(natural(n))"""

    return [sum(natural(i)) for i in natural(n)]


def tetrahedral(n: int) -> list[int]:
    """returns the first n terms of the Tetrahedral Number Sequence
    Tetrahedral Number:
        the count of spheres arranged in a tetrahedron with n spheres on a side
        Tₙ = sum(triangular(n))"""

    return [sum(triangular(i)) for i in natural(n)]


def octahedral(n: int) -> list[int]:
    """returns the first n terms of the Octahedral Number Sequence
    Octahedral Number:
        the count of spheres arranged in an octahedron with n spheres on a side
        Oₙ = n(2n² + 1) / 3"""

    return [i * (2*pow(i, 2) + 1) // 3 for i in natural(n)]


def dodecahedral(n: int) -> list[int]:
    """returns the first n terms of the Dodecahedral Number Sequence
    Dodecahedral Number:
        the count of spheres arranged in a dodecahedron with n spheres on a side
        Dₙ = n(3n - 1)(3n - 2) / 2"""

    return [i * (3*i - 1) * (3*i - 2) // 2 for i in natural(n)]


def icosahedral(n: int) -> list[int]:
    """returns the first n terms of the Icosahedral Number Sequence
    Icosahedral Number:
        the count of spheres arranged in an icosahedron with n spheres on a side
        Iₙ = n(5n² - 5n + 2) / 2"""

    return [i * (5 * pow(i, 2) - 5*i + 2) // 2 for i in natural(n)]


def sq_pyramid(n: int) -> list[int]:
    """returns the first n terms of the Square-Pyramidal Number Sequence
    Square-Pyramidal Number:
        the count of spheres arranged in a square pyramid with n spheres on a
        side of the square base
        Pₙ = sum(square(n + 1))"""

    return [sum(square(i + 1)) for i in natural(n)]


def star(n: int) -> list[int]:
    """returns the first n terms of the Star Number Sequence
    Star Number:
        the count of dots arranged in a 6-pointed star with n dots on a side
        of the central hexagon
        Sₙ = 6n(n - 1) + 1"""

    return [(6 * i * (i-1)) + 1 for i in natural(n)]


def stella_octangula(n: int) -> list[int]:
    """returns the first n terms of the Stella-Octangula Number Sequence
    Stella-Octangula Number:
        the count of spheres arranged in a stella octangula with n spheres on a
        side of the protruding triangles
        Sₙ = n(2n² - 1)"""

    return [i * ((2 * pow(i, 2)) - 1) for i in whole(n)]


def central_polygon(n: int) -> list[int]:
    """returns the first n terms of the Central Polygon Number Sequence
    Central Polygon Number:
        the maximum number of pieces of a circular disc that can be made with
        a given number of straight cuts
        Tₙ = (n² + n + 2) / 2"""

    return [(pow(n, 2) + n+2) // 2 for n in whole(n)]


def magic_constants(n: int) -> list[int]:
    """returns the first n Magic Constants
    Magic Constant:
        Mₙ = n(n²+1) / 2"""

    return [i * (pow(i, 2)+1) // 2 for i in whole(n)]


def woodall(n: int) -> list[int]:
    """returns the first n terms of the Woodall Number Sequence
    Woodall Number:
        number of the form 2ⁿn - 1
        Tₙ = 2ⁿn - 1"""

    return [(i * pow(2, i)) - 1 for i in natural(n)]


def cullen(n: int) -> list[int]:
    """returns the first n terms of the Cullen Number Sequence
    Cullen Number:
        number of the form 2ⁿn + 1
        Tₙ = 2ⁿn + 1"""

    return [(i * pow(2, i)) + 1 for i in whole(n)]


def pronic(n: int) -> list[int]:
    """returns the first n terms of the Pronic Number Sequence
    Pronic Number:
        number that is product of two consecutive whole numbers
        Tₙ = n(n + 1)"""

    return [i * (i+1) for i in whole(n)]


def arithmetic(n: int) -> list[int]:
    """returns the first n terms of the Arithmetic Number Sequence
    Arithmetic Number:
        a number such that the average of its positive divisors is also an
        integer"""

    n, numbers, num = check(n), list(), 1

    def average(x):
        """returns the average of the positive divisors of x"""

        divisors = list()
        for i in range(1, x+1):
            if not (x % i):
                divisors.append(i)
        return float(sum(divisors) / len(divisors))

    while len(numbers) < n:
        if average(num).is_integer():
            numbers.append(num)
        num += 1

    return numbers


def carol(n: int) -> list[int]:
    """returns the first n terms of the Carol Number Sequence
    Carol Number:
        number such that bin(n) is of the form (n-2) 1s + 0 + (n+1) 1s
        Tₙ = (2ⁿ - 1)² - 2"""

    return [pow(4, i) - pow(2, i+1) - 1 for i in natural(n)]


def perfect(n: int) -> list[int]:
    """returns the first n terms of the Perfect Number Sequence
    Perfect Number:
        number that is equal to sum of its positive divisors excluding itself
        example: 6 = 3 + 2 + 1"""

    n, numbers = check(n), list()

    def divisors(x):
        """returns the sum of positive divisors of x"""
        return sum(i for i in range(1, x) if not (x % i))

    num = 1
    while len(numbers) < n:
        if divisors(num) == num:
            numbers.append(num)
        num += 1

    return numbers


def undulating(n: int) -> list[int]:
    """returns the first n terms of the Undulating Number Sequence
    Undulating Number:
        number of the form ABABAB... (A ≠ B)"""

    n, numbers, num = check(n), list(), 100

    while len(numbers) < n:
        a, b  = str(num)[::2], str(num)[1::2]
        types = (a == a[0]*len(a)) and (b == b[0]*len(b))

        if types and (a[0] != b[0]):
            numbers.append(num)
        num += 1

    return numbers


def pascal(n: int) -> list[int]:
    """returns the n-th row of the Pascal's triangle
    n-th row of Pascal's Triangle is given by:
        Pₙ = ⁿCᵣ for r ∈ range(n+1)"""

    return [math.comb(n, r) for r in range(n+1)]


def gould(n: int) -> list[int]:
    """returns the first n terms of the Gould Sequence
    Gould Number:
        the count of odd numbers in the n-th row of pascal's triangle
        Tₙ = count(odd numbers in pascal(n))"""

    n, numbers = check(n), list()

    for i in natural(n):
        count = 0
        for num in pascal(i):
            if num % 2:
                count += 1
        numbers.append(count)

    return numbers


def central_binomial(n: int) -> list[int]:
    """returns the first n Central Binomial Coefficients
    Central Binomial Coefficient:
        the coefficient that shows up exactly in the middle of the even numbered
        rows of Pascal's triangle"""

    return [math.comb(2*i, i) for i in whole(n)]


def catalan(n: int) -> list[int]:
    """returns the first n terms of the Catalan Number Sequence
    Catalan Number:
        number of the form (2n!) / (n!(n+1)!)
        Cₙ = ²ⁿCₙ / (n+1)"""

    return [math.comb(2*i, i) // (i+1) for i in whole(n)]


def van_eck(n: int) -> list[int]:
    """returns first n terms of the Van-Eck Sequence
    Van-Eck Sequence is defined as:
        Tₙ = 0 if n == 0
        Tₙ = 0 if Tₙ₋₁ is a new number
        Tₙ = x if Tₙ occured x steps earlier in the sequence"""

    n, numbers = check(n), [0]

    while len(numbers) < n:
        num, previous = numbers[-1], numbers[:-1]

        if num not in previous:
            numbers.append(0)
            continue

        count = 0
        for index in range(len(numbers)-1, -1, -1):
            if numbers[index] == num:
                count += 1
            if count == 2:
                break

        numbers.append(len(numbers) - 1 - index)

    return numbers


def recaman(n: int) -> list[int]:
    """returns first n terms of the Recamán Sequence
    Recamán Sequence is defined as:
        Tₙ = 0 if n == 0
        Tₙ = Tₙ₋₁ - n if positive and not already in sequence
        Tₙ = Tₙ₋₁ + n otherwise"""

    n, numbers = check(n), [0]

    for i in range(1, n):
        num = numbers[-1] - i
        if num > 0 and num not in numbers:
            numbers.append(numbers[-1] - i)
        else:
            numbers.append(numbers[-1] + i)

    return numbers


def look_say(n: int) -> list[int]:
    """returns first n terms of the Look and Say Sequence
    Look and Say Sequence is defined as:
        Tₙ = 0 if n == 0
        Tₙ = int(word for Tₙ₋₁) otherwise
        example:
            word for: 1 -> 'one 1' -> next term: 11
            word for: 11233 -> 'two 1s one 2 two 3s' -> next term: 211223"""

    n, numbers = check(n), [1]

    while len(numbers) < n:
        num, string = str(numbers[-1]), ""

        for i in range(len(num)):
            string += num[i]
            if i != (len(num) - 1) and num[i] != num[i+1]:
                string += " "

        chars, string = string.split(), ""
        for i in chars:
            string += str(i.count(i[0])) + i[0]

        numbers.append(int(string))

    return numbers


def aronson(n: int) -> list[int]:
    """returns the first n terms of the Aronson Sequence
    Aronson Sequence is defined as:
        the index of English Letter "T" or "t" in the sentence
        "T is the first, fourth, eleventh, ... letter in this sentence"
        ignoring spaces and punctuation marks"""

    sentence = "_tisthefirstfourth"
    n, numbers = check(n), list()

    def name(number):
        """returns the name of an integer"""

        names = {
            0: "zero", 1: "first", 2: "second", 3: "third", 4: "fourth",
            5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth",
            11: "eleventh", 12: "twelfth", 13: "thirteenth", 14: "fourteenth",
            15: "fifteenth", 16: "sixteenth", 17: "seventeenth", 10: "ten",
            18: "eighteenth", 19: "nineteenth", 30: "thirty", 40: "forty",
            20: "twenty",  50: "fifty", 60: "sixty", 70: "seventy",
            80: "eighty", 90: "ninety",
        }
        orders = {
            **dict.fromkeys([3], ("hundred", 10**2)),
            **dict.fromkeys([4, 5, 6], ("thousand", 10**3)),
            **dict.fromkeys([7, 8, 9], ("million", 10**6)),
            **dict.fromkeys([10, 11, 12], ("billion", 10**9)),
            **dict.fromkeys([13, 14, 15], ("trillion", 10**12)),
        }

        order = len(str(number))

        if number in names:
            return names[number]
        if order == 2:
            return f"{name(number // 10*10)}{name(number % 10)}"
        place, div = orders[order]
        slash, percent = number // div, number % div
        if not percent:
            return f"{name(slash)}{place}"
        return f"{name(slash)}{place}{name(percent)}"

    while len(numbers) < n:
        i = sentence.index("t")
        numbers.append(i)
        sentence = sentence.replace("t", "_", 1)
        if i > 4:
            sentence += name(i)
    return numbers


def baum_sweet(n: int) -> list[int]:
    """returns the first n terms of the Baum-Sweet Sequence
    Baum Sweet Sequence is defined as:
        Tₙ = 1 if bin(n) contains no block of consecutive 0s of odd length
        Tₙ = 0 otherwise"""

    n, numbers, num = check(n), [1], 1

    while len(numbers) < n:
        binary, string = bin(num), ""

        for i in range(len(binary)):
            string += binary[i]
            if i != (len(binary) - 1) and binary[i] != binary[i+1]:
                string += " "

        for char in string[3:].split():
            if char[0] == "0" and (len(char) % 2):
                numbers.append(0)
                break
        else:
            numbers.append(1)

        num += 1

    return numbers


def fibonacci(n: int) -> list[int]:
    """returns first n terms of the Fibonacci Sequence
    Fibonacci Sequence is defined as:
        Fₙ = 0 if n == 0
        Fₙ = 1 if n == 1
        Fₙ = Fₙ₋₁ + Fₙ₋₂ otherwise"""

    n, numbers = check(n), [0, 1]

    if n in range(1, 3):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2])

    return numbers


def negafibonacci(n: int) -> list[int]:
    """returns first n terms of the NegaFibonacci Sequence
    NegaFibonacci Sequence is defined as:
        F₋ₙ = (-1)ⁿ⁺¹Fₙ
        where Fₙ is the n-th Fibonacci Number"""

    return [pow(-1, i+1) * fibonacci(n)[i] for i in range(n)]


def tribonacci(n: int) -> list[int]:
    """returns first n terms of the Tribonacci Sequence
    Tribonacci Sequence is defined as:
        Tₙ = 0 if n in (0, 1)
        Tₙ = 1 if n == 2
        Tₙ = Tₙ₋₁ + Tₙ₋₂ + Tₙ₋₃ otherwise"""

    n, numbers = check(n), [0, 0, 1]

    if n in range(1, 4):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(sum(numbers[-3:]))

    return numbers


def negatribonacci(n: int) -> list[int]:
    """returns the first n terms of the NegaTribonacci Sequence
    NegaTribonacci Sequence is defined as:
        T₋ₙ = (-1)ⁿ⁺¹Tₙ
        where Tₙ is the n-th Tribonacci Number"""

    return [pow(-1, i+1) * tribonacci(n)[i] for i in range(n)]


def lucas(n: int) -> list[int]:
    """returns the first n terms of the Lucas Sequence
    Lucas Sequence is defined as:
        Lₙ = 2 if n == 0
        Lₙ = 1 if n == 1
        Lₙ = Lₙ₋₁ + Lₙ₋₂ otherwise"""

    n, numbers = check(n), [2, 1]

    if n in range(1, 3):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2])

    return numbers


def negalucas(n: int) -> list[int]:
    """returns first n terms of the NegaLucas Sequence
    NegaFibonacci Sequence is defined as:
        L₋ₙ = (-1)ⁿLₙ
        where Lₙ is the n-th Lucas Number"""

    return [pow(-1, i) * lucas(n)[i] for i in range(n)]


def supergolden(n: int) -> list[int]:
    """returns the first n terms of the Supergolden Sequence
    Supergolden Sequence is defined as:
        Sₙ = 1 if n in (0, 1, 2)
        Sₙ = Sₙ₋₁ + Sₙ₋₃ otherwise"""

    n, numbers = check(n), [1] * 3

    if n in range(1, 4):
        return [1] * n

    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-3])

    return numbers


def padovan(n: int) -> list[int]:
    """returns first n terms of the Padovan Sequence
    Padovan Sequence is defined as:
        Pₙ = 1 if n in (0, 1, 2)
        Pₙ = Pₙ₋₂ + Pₙ₋₃ otherwise"""

    n, numbers = check(n), [1] * 3

    if n in range(1, 4):
        return [1] * n

    while len(numbers) < n:
        numbers.append(numbers[-2] + numbers[-3])

    return numbers


def perrin(n: int) -> list[int]:
    """returns first n terms of the Perrin Sequence
    Perrin Sequence is defined as:
        Pₙ = 3 if n == 0
        Pₙ = 0 if n == 1
        Pₙ = 2 if n == 2
        Pₙ = Pₙ₋₂ + Pₙ₋₃ otherwise"""

    n, numbers = check(n), [3, 0, 2]

    if n in range(1, 4):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(numbers[-2] + numbers[-3])

    return numbers


def pell(n: int) -> list[int]:
    """returns the first n terms of the Pell Sequence
    Pell Sequence is defined as:
        Pₙ = 0 if n == 0
        Pₙ = 1 if n == 1
        Pₙ = 2Pₙ₋₁ + Pₙ₋₂ otherwise"""

    n, numbers = check(n), [0, 1]

    if n in range(1, 3):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(2*numbers[-1] + numbers[-2])

    return numbers


def jacobstathal(n: int) -> list[int]:
    """returns the first n terms of the Jacobstathal Sequence
    Jacobstathal Sequence is defined as:
        Jₙ = 0 if n == 0
        Jₙ = 1 if n == 1
        Jₙ = Jₙ₋₁ + 2Jₙ₋₂ otherwise"""

    n, numbers = check(n), [0, 1]

    if n in range(1, 3):
        return numbers[:n]

    while len(numbers) < n:
        numbers.append(numbers[-1] + 2*numbers[-2])

    return numbers


def sylvester(n: int) -> list[int]:
    """returns the first n terms of the Sylvester Sequence
    Sylvester Sequence is defined as:
        Sₙ = 2 if n == 0
        Sₙ = product(sylvester(n-1)) + 1 otherwise"""

    n, numbers = check(n), list()

    while len(numbers) < n:
        num = 1
        for i in numbers:
            num *= i
        numbers.append(num + 1)

    return numbers


def euclid_mullin(n: int) -> list[int]:
    """returns the first n terms of the Euclid-Mullin Sequence
    Euclid-Mullin Sequence is defined as:
        Tₙ = 2 if n == 1
        Tₙ = smallest prime factor of product(euclid_mullin(n-1))+1 otherwise"""

    n, numbers = check(n), [2]

    def smallest_factor(x):
        """returns the smallest prime factor of x"""

        if isprime(x):
            return x

        for i in range(2, x+1):
            if isprime(i) and (not x % i):
                return i

    while len(numbers) < n:
        num = 1
        for i in numbers:
            num *= i
        numbers.append(smallest_factor(num + 1))

    return numbers


def sophie_germain(n: int) -> list[int]:
    """returns the first n terms of the Sophie-Germain Prime Number Sequence
    Sophie Germain Prime Number:
        prime number x such that 2x + 1 is also prime"""

    n, numbers, num = check(n), list(), 2

    while len(numbers) < n:
        if isprime(num) and isprime(2*num + 1):
            numbers.append(num)
        num += 1

    return numbers


def circular_prime(n: int) -> list[int]:
    """returns the first n terms of the Circular-Prime Number Sequence
    Circular Prime Number:
        number such that all of its cyclic permutations are prime"""

    n, numbers, num = check(n), list(), 2

    def perm(x):
        """returns all cyclic permutations of x"""

        x, all_x = str(x), [x]
        for i in range(len(x)):
            x = x[-1] + x[:-1]
            all_x.append(int(x))
        return all_x

    def is_circ_prime(x):
        """returns True if all cylic permutations of x are prime"""

        if x in (2, 3, 5, 7):
            return True

        for p in perm(x):
            for i in range(2, int(pow(p, 0.5) + 1)):
                if not (p % i):
                    return False
        return True

    while len(numbers) < n:
        if is_circ_prime(num):
            for z in perm(num):
                if z in numbers:
                    break
            else:
                numbers.append(num)
        num += 1

    return numbers


def prime_powers(n: int) -> list[int]:
    """returns the first n Prime Power Numbers
    Prime Power Number:
        number of the form xⁿ where x is prime and n is any positive integer"""

    n, numbers, num = check(n), [2], 3

    def is_prime_power(x):
        """returns True if x is a Prime Power Number"""

        copy = x
        for i in prime(x):
            while copy != 1:
                if copy % i:
                    break
                copy //= i
            else:
                return True
            copy = x
        return False

    while len(numbers) < n:
        if is_prime_power(num):
            numbers.append(num)
        num += 1

    return numbers


def semiprime(n: int) -> list[int]:
    """returns the first n Semi-Prime Numbers
    Semi-Prime Number:
        the product of two prime numbers, not necessarily distinct"""

    n, numbers, num = check(n), list(), 4

    def factors(x):
        """returns the number of prime factors of x (not unique)"""

        total, i = 0, 2
        while x != 1:
            if not isprime(i):
                i += 1
            if not (x % i):
                x //= i
                total += 1
            else:
                i += 1
        return total

    while len(numbers) < n:
        if factors(num) == 2:
            numbers.append(num)
        num += 1

    return numbers


def sphenic(n: int) -> list[int]:
    """returns the first n terms of the Sphenic Number Sequence
    Sphenic Number:
        number that is the product of three distinct primes"""

    n, numbers, num = check(n), list(), 30

    def factors(x):
        """returns the number of unique prime factors of x"""

        divs, i = list(), 2
        while x != 1:
            if not isprime(i):
                i += 1
            if not (x % i):
                x //= i
                divs.append(i)
            else:
                i += 1
        return divs

    while len(numbers) < n:
        if len(f := factors(num)) == len(set(f)) == 3:
            numbers.append(num)
        num += 1

    return numbers
