class Persona:
    def __init__(self, id, nombre, email):
        self.id_Persona=id
        self.nombre=nombre
        self.email=email
    def login(self):
        print("\n[SESION]:", self.nombre, "ha entrado al sistemaaa")

class Cliente(Persona):
    def __init__(self, id, nom, em, puntos):
        super().__init__(id, nom, em)
        self.puntos_Fidelidad=puntos
        self.historial_Pedidos=[]
    def realizar_Pedido(self, pedido):
        self.historial_Pedidos.append(pedido)
        self.puntos_Fidelidad=self.puntos_Fidelidad+10
    def consultar_Historial(self):
        print("\n---PUNTOS ACUMULADOS---")
        print("Cliente:", self.nombre, "| Total:", self.puntos_Fidelidad)
    def canjear_Puntos(self):
        if self.puntos_Fidelidad>=50:
            self.puntos_Fidelidad=self.puntos_Fidelidad-50
            return True
        return False

class Empleado(Persona):
    def __init__(self, id, nom, em, idE, rol):
        super().__init__(id, nom, em)
        self.id_Empleado=idE
        self.rol=rol 
    
    def actualizar_Inventario(self, inv):
        inv.notificar_Faltante()
        id_llenar=input("\nID del producto q se va a llenar: ")
        unids=int(input("cuantas unidades se agregan?: "))
        
        pos=0
        for p in inv.productos:
            if p.id_Producto==id_llenar:
                agregados=0
                while agregados<unids:
                    inv.cantidades[pos]=inv.cantidades[pos]+1
                    agregados=agregados+1
                print(">> Stock actualizado para", p.nombre)
            pos=pos+1

    def cambiar_EstadoPedido(self, pedido, estado):
        pedido.estado=estado
        print(">>Estado del pedido:", estado)

class ProductoBase:
    def __init__(self, id, nom, precio):
        self.id_Producto=id
        self.nombre=nom
        self.precio_Base=precio

class Bebida(ProductoBase):
    def __init__(self, id, nom, precio, tam, temp):
        super().__init__(id, nom, precio)
        self.tamano=tam
        self.temperatura=temp 
        self.precio_Final=precio
    def agregar_Extra(self,extra, costo):
        self.precio_Final=self.precio_Final+costo
    def calcular_PrecioFinal(self):
        return self.precio_Final

class Postre(ProductoBase):
    def __init__(self, id, nom, precio, vegano, gluten):
        super().__init__(id, nom, precio)
        self.vegano=vegano
        self.sin_Gluten=gluten

class Inventario:
    def __init__(self, lista_prods):
        self.productos=lista_prods
        self.cantidades=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    def reducir_Stock(self, id_prod):
        pos=0
        for p in self.productos:
            if p.id_Producto==id_prod:
                if self.cantidades[pos]>0:
                    self.cantidades[pos]=self.cantidades[pos]-1
                    return True
            pos=pos+1
        return False
    def notificar_Faltante(self):
        print("\n--- STOCK ---")
        pos=0
        for p in self.productos:
            print(p.id_Producto, ":", p.nombre, "| Stock:", self.cantidades[pos])
            pos=pos+1

class Pedido:
    def __init__(self, id_ped):
        self.id_Pedido=id_ped
        self.productos=[]
        self.total=0.0
    def calcular_Total(self):
        suma=0.0
        for p in self.productos:
            if p.id_Producto[0]=="B": 
                suma=suma+p.precio_Final
            else: 
                suma=suma+p.precio_Base
        self.total=suma
        return self.total
    def validar_Stock(self, inv):
        return True