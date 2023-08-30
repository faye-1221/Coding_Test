N = int(input())
expression = input()

def diffWaysToCompute(expression):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results

    if expression.isdigit():
        return [int(expression)]

    results = []
    for idx, value in enumerate(expression):
        if value in "-+*":
            left = diffWaysToCompute(expression[:idx])
            right = diffWaysToCompute(expression[idx+1:])
            results.extend(compute(left, right, value)) 
    return results 

print(max(diffWaysToCompute(expression)))