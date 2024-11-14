import numpy as np

def count_vowels(s1):
    vowel_count = 0
    for i in s1:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowel_count += 1
    return vowel_count

string_array = np.array(["hello", "soham", "strings", "vowels", "count"])


max_count = 0
max_string = ""
for i in string_array:
    curr_count = count_vowels(i)
    if curr_count > max_count:
        max_count = curr_count
        max_string = i
    if curr_count == max_count:
        if i < max_string:
            max_string = i
print(f"String with the max count is {max_string}")
print(f"Max count of vowels in string is {max_count}")

    