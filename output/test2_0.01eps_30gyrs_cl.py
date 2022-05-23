import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/pcode/class_decays/output/test2_0.01eps_30gyrs_cl.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test2_0.02eps_30gyrs_cl.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test1_lcdm_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test2_0', 'test2_0', 'test1_lcdm_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT', u'EE', u'BB', u'TE', u'dd', u'dT', u'dE']
tex_names = ['TT', 'EE', 'BB', 'TE', 'dd', 'dT', 'dE']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

index, curve = 1, data[1]
y_axis = [u'TT', u'EE', u'BB', u'TE', u'dd', u'dT', u'dE']
tex_names = ['TT', 'EE', 'BB', 'TE', 'dd', 'dT', 'dE']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

index, curve = 2, data[2]
y_axis = [u'TT', u'EE', u'BB', u'TE', u'dd', u'dT', u'dE']
tex_names = ['TT', 'EE', 'BB', 'TE', 'dd', 'dT', 'dE']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()