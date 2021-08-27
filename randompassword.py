#Classic random password maker

import string
from random import *

characters = (string.ascii_letters + string.punctuation  + string.digits)

password =  "".join(choice(characters) for x in range(randint(10, 30)))

print(password)
