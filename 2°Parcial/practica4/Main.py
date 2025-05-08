from ReadingData import read_json_file
from ReadingTemplate import read_Template
from PersonalizeOffice import create_office
from SaveOffice import save_office, generate_file_name
from CalculateAge import calculate_age


def main():
    jsonData = "/home/hertz676/Documentos/Ingenieria desarrollo de software/7mo/IoT (Python)/2°Parcial/practica4/personas.json"    
    data = read_json_file(jsonData)
    template = read_Template("Correspondencia.docx")

    for person in data['personas']:
        person['edad calculada'] = calculate_age(person['fechaNacimiento'])
        text = create_office(template, person)
        file_name = generate_file_name(person)
        save_office(file_name, text)
        print("Archivo guardado:", file_name)
if __name__ == "__main__":
    main()