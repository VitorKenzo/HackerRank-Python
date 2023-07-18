# user input
S = input()

# sorting everything and making it iterable using list
S = sorted(list(S))

#to separate the classes of alpha numerics
lowercase, uppercase, even_digits, odd_digits = [], [], [], []

for s in S:
    if s.islower():
        lowercase.append(s)
    elif s.isupper():
        uppercase.append(s)
    elif s.isdigit():
        if int(s) % 2 == 0:
            even_digits.append(s)
        else:
            odd_digits.append(s)

#printing the result in the right order
print(''.join(lowercase + uppercase + odd_digits + even_digits))
