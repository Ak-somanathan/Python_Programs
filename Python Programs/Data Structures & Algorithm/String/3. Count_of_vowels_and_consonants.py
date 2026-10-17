class Solution:
    # for loop + if..else
    def countVowelsAndConsonants1(self, s):
        vowel = 0
        consonant = 0

        for i in s:
            if i in "aeiouAEIOU":
                vowel += 1

            elif i.isalpha():
                consonant += 1

        return f'Vowels: {vowel}, Consonants: {consonant}'

    # for loop + set
    def countVowelsAndConsonants2(self, s):
        vowel = 0
        consonant = 0
        vowel_set = set("aeiouAEIOU")

        for i in s:
            if i in vowel_set:
                vowel += 1

            elif i.isalpha():
                consonant += 1

        return f'Vowels: {vowel}, Consonants: {consonant}'

obj = Solution()

s = input()

print(obj.countVowelsAndConsonants1(s))
print(obj.countVowelsAndConsonants2(s))