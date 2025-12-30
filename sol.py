n = 358
l = 1
t = 200

digits = []
temp = n
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

nums = []

for a in digits:
    nums.append(a)

for a in digits:
    for b in digits:
        if a != b:
            nums.append(a * 10 + b)

for a in digits:
    for b in digits:
        for c in digits:
            if a != b and b != c and a != c:
                nums.append(a * 100 + b * 10 + c)

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

finalAns = []
for x in nums:
    if l < x < t and isPrime(x):
        finalAns.append(x)

print(sorted(set(finalAns)))
