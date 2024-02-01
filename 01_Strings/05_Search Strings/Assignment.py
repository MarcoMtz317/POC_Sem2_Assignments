text = ("Store Text")

result = text.find("the")

if result == -1:
    print("the word the is not in the string")
else:
    print("the word the is in the string")
    print("the word the apears at", result)
