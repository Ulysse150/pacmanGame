# Créé par leonardr, le 08/03/2022 en Python 3.7
from game import *
import traceback
g = Game()


try:

    while g.en_cours:
        g.main()

except:

    print(traceback.format_exc())

