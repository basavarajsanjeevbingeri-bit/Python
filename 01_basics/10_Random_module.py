import random

# number = random.randint(10,20)
# print(number)

# number = random.randrange(10,20)
# print(number)


# number = random.uniform(10,20)
# print(number)

# number = random.random()
# print(number)


l = [2 ,91 , -8 , 7 , 6 ,0]
# picker = random.choices(l)
# print(picker)

random.shuffle(l)
print(l)

# Python random Module — Full Methods List

# 🔹 1. Basic Random Numbers
# random.random()        # Float [0.0, 1.0)
# random.uniform(a, b)   # Float [a, b]
# random.randint(a, b)   # Int [a, b]
# random.randrange(start, stop, step)
# 🔹 2. Sequence Operations
# random.choice(seq)              # Single element
# random.choices(seq, k=n)        # With replacement
# random.sample(seq, k=n)         # Without replacement
# random.shuffle(seq)             # In-place shuffle
# 🔹 3. Weighted Random
# random.choices(population, weights=None, cum_weights=None, k=1)
# 🔹 4. Distributions (Important for Interviews)
# Normal / Gaussian
# random.gauss(mu, sigma)
# random.normalvariate(mu, sigma)
# Uniform
# random.uniform(a, b)
# Exponential
# random.expovariate(lambd)
# Gamma
# random.gammavariate(alpha, beta)
# Beta
# random.betavariate(alpha, beta)
# Log Normal
# random.lognormvariate(mu, sigma)
# Triangular
# random.triangular(low, high, mode)
# Von Mises (circular data)
# random.vonmisesvariate(mu, kappa)
# Pareto
# random.paretovariate(alpha)
# Weibull
# random.weibullvariate(alpha, beta)
# 🔹 5. Bytes & Bits
# random.getrandbits(k)     # k random bits (int)
# random.randbytes(n)       # n random bytes (Python 3.9+)
# 🔹 6. Seed & State (Very Important)
# random.seed(a=None)       # Initialize generator
# random.getstate()         # Get internal state
# random.setstate(state)    # Restore state
# 🔹 7. System-Level Random (Secure)
# import random
# secure = random.SystemRandom()

# secure.random()
# secure.randint(a, b)
# secure.choice(seq)

# 👉 Uses OS entropy (more secure than normal random)

# 🔹 8. Quick Utility Patterns
# Random Boolean
# random.choice([True, False])
# Random String
# import string
# ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# Random Color
# "#%06x" % random.randint(0, 0xFFFFFF)
# 🔹 9. Important Notes
# randint(a, b) → includes both ends ✅
# randrange() → behaves like range()
# shuffle() → modifies original list ⚠️
# sample() → no duplicates
# choices() → allows duplicates