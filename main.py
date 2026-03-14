from models import *
clientes=[
    Cliente("1","Jax","jax@gmail.com",100), 
    Cliente("2","Pomni","pompom@gmail.com",50),
    Cliente("3","Ragatha","ragaa@gmail.com",60), 
    Cliente("4","Zooble","zooble@gmail.com",120),
    Cliente("5","Gangle","loveanime@gmail.com",20), 
    Cliente("6","Kinger","kinger@gmail.com",150),
    Cliente("7","Majo","majitoo@gmail.com",10), 
    Cliente("8","Rafa","rafaelf@gmail.com",70),
    Cliente("9","Osvaldo","osvaldof@gmail.com",0), 
    Cliente("10","Andree","andreelet@gmail.com",0)
]
empleados=[
    Empleado("101","Catnap","cat@c.com","E1","BARISTA"), 
    Empleado("102","Dogday","dog@c.com","E2","MESERO"),
    Empleado("103","Crafty","cra@c.com","E3","BARISTA"), 
    Empleado("104","Bubba","bub@c.com","E4","GERENTE"),
    Empleado("105","Bobby","bob@c.com","E5","MESERO"), 
    Empleado("106","Kickin","kic@c.com","E6","BARISTA"),
    Empleado("107","Picky","pic@c.com","E7","MESERO"), 
    Empleado("108","Hoppie","hop@c.com","E8","BARISTA"),
    Empleado("109","Doey","doe@c.com","E9","MESERO"), 
    Empleado("110","Yarnaby","yar@c.com","E10","BARISTA")
]

menu=[
    Bebida("B1","Espresso",35.0,"Ch","Caliente"), 
    Bebida("B2","Latte",50.0,"Gr","Caliente"),
    Bebida("B3","Frappe",60.0,"Gr","Frio"), 
    Bebida("B4","Te Verde",40.0,"Me","Caliente"),
    Bebida("B5","Americano",45.0,"Gr","Caliente"),
    Postre("P1","Dona",20.0,False,False), 
    Postre("P2","Muffin",40.0,True,False),
    Postre("P3","Galleta",30.0,False,True), 
    Postre("P4","Cheesecake",55.0,False,False),
    Postre("P5","Brownie",35.0,False,False)
]
inv=Inventario(menu)

login=True
while login:
    print("\n"+"=====================")
    print("---Userss registrados---")
    for c in clientes:
        print("ID:",c.id_Persona, "| Nombre:",c.nombre,"| Puntos:",c.puntos_Fidelidad)
    print("-------------------")
    for e in empleados:
        print("ID:", e.id_Persona,"| Nombre:", e.nombre,"| Rol:",e.rol)
    print("=====================")

    tipo=input("\nentrar como cliente(c) o empleado(e)?: ")

    if tipo=="e" or tipo=="E":
        id_emp=input("Ingrese su ID de Empleado: ")
        staff=empleados[0]
        for e in empleados: 
            if e.id_Persona==id_emp: 
                staff=e
        staff.actualizar_Inventario(inv)
    else:
        id_cliente=input("Ingrese su ID de Cliente: ")
        user=clientes[0]
        for c in clientes: 
            if c.id_Persona==id_cliente: 
                user=c
        
        id_emp=input("ID del Empleado que atiende: ")
        staff=empleados[0]
        for e in empleados: 
            if e.id_Persona==id_emp: 
                staff=e
        
        user.login()
        ped=Pedido("Pedido-707")

        compras=True
        while compras:
            print("\n---MENU---")
            for i in [0,1,2,3,4,5,6,7,8,9]:
                p=menu[i]
                print(p.id_Producto, ".", p.nombre, "$", p.precio_Base, "[Stock:", inv.cantidades[i], "]")
            
            opc=input("\nID para elegir el producto o 'p' para pagar: ")
            if opc=="p": 
                compras=False
            else:
                for item in menu:
                    if item.id_Producto==opc:
                        if opc[0]=="B":
                            item.temperatura=input("Fria o Caliente (f/c): ")
                            if input("Leche extra (+$15)?(s/n): ")=="s": 
                                item.agregar_Extra("Leche Extra", 15)
                        else:
                            if input("sin gluten? (s/n): ")=="s" or "S": 
                                item.sin_Gluten=True
                        
                        if inv.reducir_Stock(opc):
                            ped.productos.append(item)
                            print(">> Añadido ")
                        else: 
                            print(">> AGOTADOo")
        subtotal=ped.calcular_Total()
        descuento=0
        print("\nPuntos de", user.nombre, ":", user.puntos_Fidelidad)
        if input("canjear 50 puntos por $15 de descuento?(s/n): ")=="s":
            if user.canjear_Puntos(): 
                descuento=15
                print(">> Canje exitoso C:")
            else:
                print(">> No te alcanzan los puntos :c")

        print("\n"+"**********************")
        print("TICKET DE VENTA")
        print("**********************")
        print("CLIENTE:", user.nombre)
        print("ATENDIO:", staff.nombre)
        print("-------------------")
        for comprita in ped.productos:
            precio_linea=comprita.precio_Base
            if comprita.id_Producto[0]=="B":
                precio_linea=comprita.precio_Final
            print("-", comprita.nombre, ": $", precio_linea)
        
        print("-------------------")
        print("SUBTOTAL:   $", subtotal)
        print("DESCUENTO: -$", descuento) 
        print("TOTAL:      $", subtotal-descuento)
        print("**********************")
        
        user.realizar_Pedido(ped)
        staff.cambiar_EstadoPedido(ped, "ENTREGADO")
        user.consultar_Historial()

    if input("\ndeseas realizar otra operacion? (s/n): ")=="n": 
        login=False

print("\n---GRACIAS POR USAR EL SISTEMA ^^---")