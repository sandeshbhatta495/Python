<<<<<<< HEAD
import numpy as np
# Without vectorization (slow)
data = np.arange(1e6)
squared = [x**2 for x in data]

# With vectorization (fast)
squared_vec = data**2
=======
import numpy as np
# Without vectorization (slow)
data = np.arange(1e6)
squared = [x**2 for x in data]

# With vectorization (fast)
squared_vec = data**2
>>>>>>> ad12eb181427590f30d26fd51061b42124f2f380
