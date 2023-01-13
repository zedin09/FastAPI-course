def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('john', 'ortiz'))
# print(get_full_name('jphn', 0)) #AttributeError