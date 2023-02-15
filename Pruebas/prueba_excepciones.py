while True:
    try:
        a = int(input("Introduce el numero a: "))
        b = float(input("Introduce el numero b: "))

        if a > 5 or b > 5 or not isinstance(b, int):
            raise ValueError("no se puede introducir valores mayores que 5")
        break
    except Exception as e:
        print("Error ", str(e))
