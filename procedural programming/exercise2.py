string = "012345678901234567890123456789"

list_string = [string[0:10] for i in range(string.count("9"))]
print(".".join(list_string))
