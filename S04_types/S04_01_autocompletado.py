def get_full_name(first_name, last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('john', 'ortiz'))
#? sin tipado en los parámetros de la fn no hay autocompletado

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('john', 'ortiz'))
#? con tipado en los parámetros de la fn hay autocompletado