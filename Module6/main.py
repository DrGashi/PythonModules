from Module5.functionsAL import printoje
from Module6.my_math import katrori, shuma, ndryshimi, prodhimi, heresi, moduli, rrenja
from math import sqrt as sq
import importlib
import Module6

importlib.reload(Module6.my_math)

printoje(katrori(5))
printoje(shuma(5, 2))
printoje(ndryshimi(10, 3))
printoje(prodhimi(4, 7))
printoje(int(heresi(16, 4)))
printoje(moduli(8, 2))
printoje(int(rrenja(225)))
printoje(int(sq(396)))
