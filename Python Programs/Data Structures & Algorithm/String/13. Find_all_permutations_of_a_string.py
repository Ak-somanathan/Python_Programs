s = input()

res = []

def backtrack(curr, rem):

    if len(rem) == 0:
        res.append(curr)

    for i in range(len(rem)):
        new_curr = curr + rem[i]
        new_rem = rem[:i] + rem[i+1:]
        backtrack(new_curr, new_rem)

    return res

backtrack("", s)
print(", ".join(res))
