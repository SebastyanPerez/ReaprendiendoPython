 
class Producto:
   def __init__(self, nombre, precio, stock):
       if precio<0:
          raise ValueError("El precio no puede ser negativo")
       if stock<0:
            raise ValueError("El stock no puede ser negativo")
       
       self.__nombre=nombre
       self.__precio=precio 
       self.__stock=stock 
  
   def vender(self,cantidad):
        if cantidad <=0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")
        if cantidad > self.__stock:
            raise ValueError(f"No hay suficiente stock para vender {cantidad} unidades de {self.__nombre}. Stock actual: {self.__stock}")
        self.__stock -= cantidad
        print(f"Se han vendido {cantidad} unidades de {self.__nombre}. Stock actual: {self.__stock}")
    
   def reponer(self,cantidad):
        if cantidad <=0:
            raise ValueError("La cantidad a reponer debe ser mayor que cero")
        self.__stock +=cantidad
        print(f"Se han repuesto {cantidad} unidades de {self.__nombre}. Stock actual: {self.__stock}")

   def mostrar_informacion(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Stock: {self.__stock} unidades")


producto = Producto("Laptop", 1000, 10)
producto.mostrar_informacion()
producto.vender(3)
producto.reponer(5)

producto.mostrar_informacion()
print(producto._Producto__stock)