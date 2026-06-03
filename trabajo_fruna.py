def Fruna():
    lista_cosas = []
    total_mercaderia = 0
    caso_bucle = True
    while caso_bucle == True:
            seguir_lista = input("Si quiere seguir adjuntando productos escriba 'APARTE', si no escriba 'ahinoma'\n")
            match seguir_lista.lower():
                case "ahinoma":
                    print("Se termino el programa\n")
                    print("Los produtos que se han agregado a la lista de compra son : ")
                    print(lista_cosas)
                    print(f"El total a pagar es \n {total_mercaderia}")
                    caso_bucle = False
                case "aparte":
                        try:
                            producto = input("Ingrese el producto a pedir\n")
                            precio = int(input("Ingrese el precio\n"))
                            if precio > 0:
                                total_mercaderia += precio
                                diccionario_local = {producto : precio}
                                lista_cosas.append(diccionario_local)
                                print("Producto ingresado a lista de compra")
                            else:
                                print("Valor del producto no puede ser menor a 0")
                                continue
                        except ValueError:
                            print("Fallo al ingresar un valor")
                case _:
                    print("No se ingreso una opcion valida")

Fruna()