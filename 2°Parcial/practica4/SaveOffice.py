def save_office(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def generate_file_name(person):
    first_name = person["nombre"].replace(" ", "_")
    last_name = person.get("apellido1")
    return f"{first_name}_{last_name}.txt"  