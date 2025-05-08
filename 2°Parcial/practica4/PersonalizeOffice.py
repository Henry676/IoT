def create_office(template, person):
    personalized_text = template
    for key, value in person.items():
        label = f"{{{{{key}}}}}"
        personalized_text = personalized_text.replace(label, str(value))
    return personalized_text
