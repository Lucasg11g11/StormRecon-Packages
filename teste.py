def run(args):
    print("Comando personalizado 'ola' executado!")
    if args:
        print("Argumentos passados:")
        for i, arg in enumerate(args, 1):
            print(f"  {i}. {arg}")
    else:
        print("Nenhum argumento foi passado.")
