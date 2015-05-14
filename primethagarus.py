'''Locate all of the Pythagorean triples with a,b,c < n for which a,b,c share no common factors'''

def e_sieve(number):
    primes = []
    sieve = [True] * (number+1)
    for p in range(2, number+1):
        if sieve[p]:   # default test is against the argument being True.
            primes.append(p)
            for i in range(p*p, number+1, p):
                sieve[i] = False
    return primes

def factorise(number, divisors):
    original = int(number)
    factors = []
    for n in range(0, len(divisors)):
        while number % divisors[n] == 0:
            factors.append(divisors[n])
            number /= divisors[n]
    if number != 0:
        factors.append(int(number))
    if 1 in factors:
        factors.remove(1)
    return factors

def primethagoras():
    print('This program will locate all of the Pythagorean triples with a,b,c < n for which a,b,c share no common factors.')
    n = int(input('Please specify an upper bound for a,b and c:\n'))
    p_triples = [(a,b,c) for a in range(1,n) for b in range(1,n) for c in range(1,n) if a<b<c and(a**2 + b**2)==c**2]
    primetrips=[]
    for trip in p_triples:
        primes = e_sieve(int(trip[2]))
        pfactors = factorise(int(trip[2]), primes)
        for x in pfactors:
            if int(trip[0]) % x == 0 and int(trip[1]) % x == 0:
                    break
            else:
                if x==pfactors[-1]:
                    primetrips.append(trip)
    print(primetrips)

if __name__ == "__main__":
    primethagoras()
