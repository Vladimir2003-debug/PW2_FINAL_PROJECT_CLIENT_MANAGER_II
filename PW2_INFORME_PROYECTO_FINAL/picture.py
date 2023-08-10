from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []                     # Creacion de vertical
    for value in self.img:            
    	vertical.append(value[::-1])    # Cada linea de la imagen es volteada 
    return Picture(vertical)          # Se retorna objeto Picture

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]       # En vez de la linea se voltea los elementos
                                      # de la lista de lineas de la imagen
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []                     # Se crea negative

    for line in self.img:
      newLine = ""                    # Se reemplaza cada punto de la imagen 
      for i in line:                  # Con su negativo en color
        newLine += self._invColor(i)
      negative.append(newLine)        # Se agrega la linea creada al negative
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joinImg = []                      #

    for line in range(len(self.img)): # Concatenamos cada linea de la imagen con cada
      joinImg.append(self.img[line]+p.img[line]) # linea de P

    return Picture(joinImg)

  def up(self, p):
    """Devuelve una nueva figura poniendo la figura p debajo de
       la figura actual """
    upImg = self.img + p.img        # juntamos ambas listas de lineas
    
    return Picture(upImg)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """

    length = len(self.img)

    underImg = []
    
    for line in range(length):        # 
      item = ""
      for i in range(length):
        if p.img[line][i] == " ":     # Cada punto blanco en la imagen p 
          item += self.img[line][i]   # Es reemplazada por la pocicion en
        else:                         # la imagen self.img
          item += p.img[line][i]
      underImg.append(item)      

    return Picture(underImg)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeat = []
    for line in self.img:
      repeat.append(line*n)           # Multiplicamos cada linea de self.img por n
    return Picture(repeat)

  def verticalRepeat(self, n):
    repeat = self.img * n             # Multiplicamos la imagen por n veces
    return Picture(repeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""

    length = len(self.img)            # Extremos el numero de linas
    rotateImg = []

    for i in range(length):
      rotateLine = ""                 # creamos una linea
      for line in self.img:
        rotateLine += line[i]         # cada linea va a ser un string de caracteres de la pocicion 
      rotateImg.append(rotateLine)    # i de cada linea de la imagen

    return Picture(rotateImg)

