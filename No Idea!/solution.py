#getting inputs
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

#initial happiness
happiness = 0

#basic problem logic
for i in array:
    if i in A:
        happiness = happiness + 1
    if i in B:
        happiness = happiness - 1

#output
print(happiness)