def gcd(a,b):
	rem = a%b
	if rem == 0:
		return b
	else:
		return gcd(b,rem)
a = int(input("Enter a number :: "))
b = int(input("Enter a number :: "))
result = gcd(a,b)
print(result)
