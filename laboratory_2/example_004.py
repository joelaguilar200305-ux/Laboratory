
#practica resuelto de menu de comida--
#se muestra el menu en la pantalla al cliente--

print (" ==== Menu de comida===" )
print ("1. Pizza")
print ("2. Hamburguezas")
print ("3. Tacos")
print ("4. Arroz con pollo")
print ("5. Arepa")
print ("6. Bistec picado")
print ("7. Salir")

#en esta parte le pedimos al usuario que eleija una de esta opción--

option = int(input("\n Elige una de tu comida favorita: "))


match option:
    case 1: 
        print("buena elección! tu Pizza esta en camino ")  
    case 2:
        print("ya se estara entregando el pedido")
    case 3:
        print("en hora buena! en unos minutos se entregando su tacos")
    case 4:
        print("Ya se estara entregando su rico Arroz con pollo")
    case 5:
        print("En unos minutos se le estara entregando su rico Arepa")
    case 6:
        print("Menu agotado ")
    case 7:
        print("Gracias por la visita, lo esparamo pronto de nuevo")
        
    case _:
        print("Opcion invalida")
        
        
    
    




    
    

