class Cuenta():

 def __init__(self, titular, cantidad=0):
  self.titular = titular
  self.cantidad = cantidad

  def titular (self):
    print(titular)
  
  def cantidad(self):
    print(cantidad)

  
#métodos
  def mostrar(self):
    print(titular,cantidad)
  
  def ingresar(self):
    if cantidad > 0:
      self.__cantidad = self.__cantidad + cantidad
    
  def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

cuenta1= Cuenta("Luciano",5000)
cuenta1.mostrar()
cuenta1.ingresar(1000)
cuenta1.retirar(7000)
print(cuenta1)