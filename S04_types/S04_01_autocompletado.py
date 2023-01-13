def get_full_name(first_name, last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name
#? sin tipado en los parámetros de la fn no hay autocompletado

print(get_full_name('john', 'ortiz'))
# print(get_full_name('john', 0)) #AttributeError