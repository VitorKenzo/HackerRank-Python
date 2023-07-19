#input
n = int(input())

# aux variables
words = {}
diff_words = 0

# working with the words
for i in range(n):
    word = input()
    if word in words.keys():
        words[word] = words[word] + 1
    else:
        diff_words = diff_words + 1
        words[word] = 1
   
#output
print(diff_words)
#formatting the second output line
ans = ''
for value in words.values():
    ans = ans + str(f'{value} ')
print(ans)