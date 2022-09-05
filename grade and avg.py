def calculate_average(total):
    return total / 5


# Grading scale
def find_score(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'


# Enter marks of 5 subjects
scores = []
for i in range(1, 6):
    score = int(input('Enter score {0}: '.format(i)))
    print('That\'s a(n): ' + find_score(score))
    scores.append(score)

# sum of all subject marks
total = sum(scores)
avg_marks = calculate_average(total)
final_grade = find_score(avg_marks)

print('Average grade is: ' + str(avg_marks))
print("That's a(n): " + str(final_grade))
