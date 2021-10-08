def compute_gcd(a, b):
    min_num = min(a, b)
    for i in range(1, min_num+1):
        if a % i == 0 and b % i == 0:
            lcm = i
    return lcm


# By recursion

def gcd(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    else:
        return gcd(b, a % b)


print('Lcm of given numbers:', gcd(56, 93))
print('Lcm of given numbers:', compute_gcd(56, 93))
