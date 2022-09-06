word_count = 0
char_count = 0

usr_input = input("Enter a string : ")

split_string = usr_input.split()

word_count = len(split_string)

for word in split_string:
    char_count += len(word)
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))
