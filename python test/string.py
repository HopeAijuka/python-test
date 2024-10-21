def is_same_string(input_string, test_string):
    if input_string == test_string:
        return True
    else:
        return False


string1 = "Hello"
string2 = "Hope"
result = is_same_string(string1, string2)
print("Are the strings the same?", result)
