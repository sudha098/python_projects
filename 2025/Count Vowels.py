word = "sudhavermaa".lower()
vowels = "aeiou"

count = sum(1 for char in word if char in vowels)
print(count)
