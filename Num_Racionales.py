
class Numero_Racional():
   
   def __init__(self, racional_str):
      self.__numerador, self.__denominador, self.reprecentacion = self.recolector_datos(racional_str)
   

   def recolector_datos(self, rac_str):
      entero = True
      for simbol in rac_str:
         if simbol == '/':
            entero = False
      if entero:
         return (int(rac_str), 1, rac_str)
      else:
         recolector_str = ''
         for i in range(len(rac_str)):
            if rac_str[i] == '/':
               numerador = int(recolector_str)
               denominador = int(rac_str[i+1:])
            else:
               recolector_str = recolector_str + rac_str[i]
      
         new_numerador, new_denominador, reprecentacion = self.simplificador(numerador, denominador)
         return (new_numerador, new_denominador, reprecentacion)


   def simplificador(self, numerador, denominador):
      if numerador == 0 or denominador == 1:
         return (numerador, 1, str(numerador))
      elif numerador == 1:
         return (1, denominador, f'1/{denominador}')
      else:
         if numerador < 0:
            num_factores = self.descomponer_factores_primos(abs(numerador))
            new_numerador = -1
         else:
            num_factores = self.descomponer_factores_primos(numerador)
            new_numerador = 1

         den_factores = self.descomponer_factores_primos(denominador)
         new_denominador = 1
         i = 0
         j = 0
         while i<len(num_factores) and j<len(den_factores):
            if num_factores[i] == den_factores[j]:
               i += 1
               j += 1
            elif num_factores[i] < den_factores[j]:
               new_numerador *= num_factores[i]
               i += 1
            else:
               new_denominador *= den_factores[j]
               j += 1
         while i<len(num_factores):
            new_numerador *= num_factores[i]
            i += 1
         while j<len(den_factores):
            new_denominador *= den_factores[j]
            j += 1
         if new_denominador == 1:
            return (new_numerador, new_denominador, str(new_numerador))
         else:
            return (new_numerador, new_denominador, f'{new_numerador}/{new_denominador}')


   def descomponer_factores_primos(self, numero):
      factores_primos = []
      primo = 2
      while numero != 1:
         divisores = 0
         for contador in range (1, primo+1):
            if primo % contador == 0:
               divisores += 1
         if divisores == 2:
            while numero % primo == 0 and numero != 1:
               factores_primos.append(primo)
               numero = numero/primo
         primo += 1
      return factores_primos
   

   def multiplicar_dividir(self, reprec_str):
      numerador, denominador, repre = self.recolector_datos(reprec_str)
      new_numerador, new_denominador, new_reprecentacion = self.simplificador(self.__numerador * numerador, self.__denominador * denominador)
      return new_reprecentacion


   def sumar_restar(self, reprec_str):
      numerador, denominador, repre = self.recolector_datos(reprec_str)
      if self.__denominador == denominador:
         new_numerador, new_denominador, new_reprecentacion = self.simplificador(self.__numerador + numerador, denominador)
         return new_reprecentacion
      else:
         new_numerador = (self.__numerador * denominador) + (numerador * self.__denominador)
         new_denominador = self.__denominador * denominador
         new_numerador, new_denominador, new_reprecentacion = self.simplificador(new_numerador, new_denominador)
         return new_reprecentacion


   def invertirso(self):
      if self.__numerador == 0:
         return '0'
      elif self.__numerador < 0:
         num, den, rep = self.simplificador(self.__denominador * (-1), self.__numerador * (-1))
         return rep
      else:
         num, den, rep = self.simplificador(self.__denominador, self.__numerador)
         return rep