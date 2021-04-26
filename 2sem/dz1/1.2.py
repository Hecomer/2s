def bracket_check(test_string):
    count = 0
    for i in range(len(test_string)):
        if test_string[i] == '(':
            count += 1
        elif test_string[i] == ')':
            count -= 1
        if test_string[0] == ')' or test_string[-1] == '(' or count < 0:
            count = 1
            break
    if count == 0:
        print("YES")
    else:
        print("NO")
bracket_check('')