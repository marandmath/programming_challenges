input_string = open('input.txt').read()
if input_string[-1] == '\n':
    input_string = input_string[:-1]

def is_nice(s):
    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
        if vowels >= 3:
            break
    if vowels < 3:
        return False
    repeat = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = True
            break
    if not repeat:
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

count1 = 0
count2 = 0
for s in input_string.split('\n'):
    if is_nice(s):
        count1 += 1
    if is_really_nice(s):
        count2 += 1
print(count1)
print(count2)
    


