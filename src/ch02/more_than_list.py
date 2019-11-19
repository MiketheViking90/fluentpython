from array import array
from random import random
floats = array('d', (random() for i in range(10**3)))
print(floats)

import numpy as np
nums = np.arange(12)
print(nums)
