import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/a1705053/Desktop/pcode/class_decays/output/test1_lcdm_z1_pk.dat','/home/a1705053/Desktop/pcode/class_decays/output/test1_0.01eps_56gyrs_z1_pk.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test2_0.01eps_30gyrs_z1_pk.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test3_0.01eps_9.8gyrs_z1_pk.dat']
#files = ['/home/a1705053/Desktop/pcode/class_decays/output/test1_lcdm_z1_pk.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test1_0.01eps_z1_pk.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test1_0.02eps_z1_pk.dat', '/home/a1705053/Desktop/pcode/class_decays/output/test1_0.04eps_z1_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test1_lcdm_z1_pk', 'test1_0', 'test1_0', 'test1_0']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 1, data[1]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 2, data[2]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 3, data[3]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()