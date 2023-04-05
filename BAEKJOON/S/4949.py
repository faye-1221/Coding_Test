while (True):
    stack = []
    strings = str(input())
    if(strings == "."):
        break

    for string in strings:
        if string in "([":
            stack.append(string)
        
        if string == ")":
            if(len(stack) != 0 and stack[len(stack)-1] == "("):
                stack.pop()
            else:
                stack.append(")")
        
        if string == "]":
            if(len(stack) != 0 and stack[len(stack)-1] == "["):
                stack.pop()
            else:
                stack.append(")")

    if(len(stack) == 0):
        print("yes")
    else:
        print("no")