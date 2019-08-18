
import numpy as np
import matplotlib.pyplot as plt
import probfit
import iminuit


np.random.seed(0)
data = np.random.randn(10000) * 4 + 1
plt.hist(data, bins=100, histtype='step');

def gauss_pdf(x, mu, sigma):
    return 1 / np.sqrt(2 * np.pi) / sigma * np.exp(-(x - mu) **2 / 2. / sigma ** 2)

extended_gauss_pdf = probfit.Extended(gauss_pdf)
iminuit.describe(extended_gauss_pdf)
chi2 = probfit.BinnedChi2(extended_gauss_pdf, data, bins=100, bound=(-7,10))

minuit = iminuit.Minuit(chi2, sigma=1, pedantic=False, print_level=0)
minuit.migrad();

fig = plt.figure()
ax = fig.add_subplot(111)

chi2.draw(minuit,ax=ax);
fig.savefig('run1.png')
