

input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
print(user_list)
not_repeated = []
not_repeated = []
for i in user_list:
    if i not in not_repeated:
        not_repeated.append(i)

print(not_repeated)