# Mohamed Mahmoud
# Pythagorean Triples Program

# - Start of the Program -

import math
n=int(input("Enter integer n: "))
for a in range(0,n):
    for b in range(0,n):
        for c in range(0,n):
            if 1<a<b<c<n and ((a**2)+(b**2)==(c**2)) and math.gcd(math.gcd(a,b),c)==1:
                print(a,b,c)

# - End of the Program -