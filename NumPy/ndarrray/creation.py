#>>>>>>>>>>>>>>>>>>>>>> numpy.empty >>>>>>>>>>>>>>>>>>>
# numpy.empty(shape, dtype = float, order = 'C')

import numpy as np
a = np.empty([3,2], dtype = int) 
print (a)

#result:
#[[481036337261 519691042932]
# [390842023976 188978561075]
# [399431958578 137438953516]]


#>>>>>>>>>>>>>>>>>>>>>>> numpy.zeros >>>>>>>>>>>>>>>>>>>

# numpy.zeros(shape, dtype = float, order = 'C')

import numpy as np 
b = np.zeros((2,2), dtype = np.int)  
print (b)

# result 
#[[0 0]
# [0 0]]        

#>>>>>>>>>>>>>>> numpy.ones >>>>>>>>>>>>>>>>>>>>>>>>>>>

import numpy as np
c = np.ones((2,2), dtype=np.int)

print(c)

#result : 
#[[1 1]
# [1 1]]


#>>>>>>>>>>>>>>>>>>>>>>>>>> numpy.random.randn >>>>>>>>>>>>>>>
#Return a sample (or samples) from the “standard normal” distribution.
# numpy.random.randn(d0, d1, ..., dn)

import numpy as np
d = np.random.randn(2,2)

print(d)

#resulr:
#[[-2.77180935  0.99742099]
# [-0.76309103 -0.33031291]]


## Tutorials point den devam et