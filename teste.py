from gato import Gato
from cachorro import Cachorro

gato1 = Gato("Felix", 5, 0)
cachorro1 = Cachorro("cachorrinho", 8, 0)

gato1.miar()
cachorro1.latir()

gato1.moverse()
gato1.moverse()
gato1.moverse()
gato1.moverse()

cachorro1.moverse()
cachorro1.moverse()

print("Posição do gato: ", gato1.posicao)
print("Posição do cachorro: ", cachorro1.posicao)