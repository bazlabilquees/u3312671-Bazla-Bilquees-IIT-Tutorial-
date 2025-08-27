#Temperature Conversions — While loop to display a Celsius→Fahrenheit table from 10 to 30 in steps of 5. Use F = (9/5 * C) + 32.
celsius = 10
while celsius <= 30:
 fahrenheit = (9/5 * celsius)+32
 print(f"{celsius:>2} C = {fahrenheit:>5.1f} F")
 celsius += 5


# Vowels Counter Program

phrase = input("There are 5 vowels: ")
vowel_count = 0

for char in phrase:   # loop through each character
    if char.lower() in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)
