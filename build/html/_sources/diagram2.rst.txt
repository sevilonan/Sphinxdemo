.. Sphinx documentation master file, created by
   sphinx-quickstart on Sat Jun  5 10:21:07 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

My first sin curve
==================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. plot::

  import matplotlib.pyplot as plt
  import numpy as np

  t = np.arange(0.0, 2.0, 0.01)
  s = 1 + np.sin(2*np.pi*t)
  plt.plot(t, s)

  plt.xlabel('time (s)')
  plt.ylabel('voltage (mV)')
  plt.title('About as simple as it gets, folks')
  plt.grid(True)
  plt.savefig("test.png")
  plt.show()