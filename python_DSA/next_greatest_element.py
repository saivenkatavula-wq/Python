# navie method - o(n^2)
def greater_element(n):
    final_output = []
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] > n[i]:
                final_output.append(n[j])
                break
        else:
            final_output.append(-1)

    return final_output


n = [4, 5, 2, 25]

print(greater_element(n))

# using stack - o(n)

def greater_element_using_stack(n):
    stack = []
    output = [-1] * len(n)
    for i in range(len(n)):
        while len(stack) != 0 and n[i] > n[stack[-1]]:
            top_index = stack.pop()
            output[top_index] = n[i]
        stack.append(i)
    return output
n = [4, 5, 2, 25]
print(greater_element_using_stack(n))



