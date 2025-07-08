String reversal method 1


text = "Original String"
reversed_text = text[::-1]
print(reversed_text)


Using Reversed and Join method inbuilt in Python


text = "Hello, World!"
reversed_text = ''.join(reversed(text))
print(reversed_text)


Method 3- Loops

text = "Hello, World!"
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)