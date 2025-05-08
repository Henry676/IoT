from VerifyEmail import validateEmail

if __name__ == "__main__":
    print("Ingrese su correo electronico")
    email = input()
    flag = validateEmail(email)
    if flag:
        print("El correo es valido")
    else:
        print("El correo no es valido")