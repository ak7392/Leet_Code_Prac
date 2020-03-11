from collections import defaultdict


def find_first_repeating_characters(string):

    dic = defaultdict(lambda: 0)
    # Need to figure out later how to use hashing for this code.
    for i in string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # Can we resolved with below piece of code
    for i in range(len(string)):
        if string[i] == string[i+1]:
            return string[i]


string1 = 'geeksforgeeks'
string2 = 'hellogeeks'
print(find_first_repeating_characters(string1))
print(find_first_repeating_characters(string2))
