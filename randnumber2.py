#!/usr/bin/env python

import random
import inquirer

end_value = inquirer.text(message="Input end value for random number")

random_number = random.randint(1, int(end_value))

print("Random number:", random_number)