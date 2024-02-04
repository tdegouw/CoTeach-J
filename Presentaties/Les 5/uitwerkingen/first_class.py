def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]


# Voorbeeld van een bewerking (bijvoorbeeld verdubbeling)
double_operation = lambda x: x * 2

numbers = [1, 2, 3, 4, 5]
result = apply_operation(numbers, double_operation)
print("Originele lijst:", numbers)
print("Bewerkte lijst:", result)
