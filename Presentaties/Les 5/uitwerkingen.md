

# Gebruik tuple voor onveranderlijke gegevensstructuur
original_names = ('Alice', 'Bob', 'Charlie')

# Voeg een nieuwe naam toe zonder de originele gegevensstructuur te wijzigen
new_names = original_names + ('David',)
print("Originele namen:", original_names)
print("Nieuwe namen:", new_names)



def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

# Voorbeeld van een bewerking (bijvoorbeeld verdubbeling)
double_operation = lambda x: x * 2

numbers = [1, 2, 3, 4, 5]
result = apply_operation(numbers, double_operation)
print("Originele lijst:", numbers)
print("Bewerkte lijst:", result)


def filter_names(names, filter_function):
    return [name for name in names if filter_function(name)]

# Voorbeeld van een filterfunctie (bijvoorbeeld namen die met een 'A' beginnen)
starts_with_a = lambda name: name[0].lower() == 'a'

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
filtered_names = filter_names(names, starts_with_a)
print("Originele namen:", names)
print("Gefilterde namen:", filtered_names)
