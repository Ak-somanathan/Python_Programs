class solution:
    # Horizontal scanning
    def commonPrefix1(self, s):
        if not s:
            print("")
        else:
            prefix = s[0]
            for i in s[1:]:
                while not i.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        break

            return prefix

obj = solution()

s = list(map(str, input().split()))

print(obj.commonPrefix1(s))