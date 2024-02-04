def filter_names(names, filter_function):
    return [name for name in names if filter_function(name)]


# Voorbeeld van een filterfunctie (bijvoorbeeld namen die met een 'A' beginnen)
starts_with_a = lambda name: name[0].lower() == 'a'

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
filtered_names = filter_names(names, starts_with_a)
print("Originele namen:", names)
print("Gefilterde namen:", filtered_names)
