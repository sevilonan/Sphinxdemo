import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(500)
plt.hist(x, 20)
plt.grid()
plt.title(r'First Diagram')
plt.show()