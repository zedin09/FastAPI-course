def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name
#? con tipado en los parámetros de la fn hay autocompletado

print(get_full_name('john', 'ortiz'))