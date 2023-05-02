import numpy as np
import matplotlib.pyplot as plt

poisson = np.random.poisson(5, 100000) # lambda = 5, 100000 samples
gamma = np.random.gamma(5, 1, 100000) # shape = 5, scale = 1, 100000 samples
binomial = np.random.binomial(10, 0.5, 100000) # n = 10, p = 0.5, 100000 samples
beta = np.random.beta(0.5, 0.5, 100000) # alpha = 0.5, beta = 0.5, 100000 samples
normal = np.random.normal(0, 1, 100000) # mean = 0, standard deviation = 1, 100000 samples

# Define the Histograms
poisson_hist = plt.figure(1)
gamma_hist = plt.figure(2)
binomial_hist = plt.figure(3)
beta_hist = plt.figure(4)
normal_hist = plt.figure(5)

# Name the Histograms
poisson_hist.suptitle('Poisson Distribution')
gamma_hist.suptitle('Gamma Distribution')
binomial_hist.suptitle('Binomial Distribution')
beta_hist.suptitle('Beta Distribution')
normal_hist.suptitle('Normal Distribution')

# Plot the Histograms
poisson_hist.add_subplot(111).hist(poisson, bins = 50, density = True) 
gamma_hist.add_subplot(111).hist(gamma, bins = 50, density = True)
binomial_hist.add_subplot(111).hist(binomial, bins = 50, density = True)
beta_hist.add_subplot(111).hist(beta, bins = 50, density = True)
normal_hist.add_subplot(111).hist(normal, bins = 50, density = True)

plt.show()