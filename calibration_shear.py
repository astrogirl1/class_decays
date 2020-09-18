
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from scipy.interpolate import interp1d

import time
start_time = time.time()

#%%
#Gamma_dcdm = 19.6078
Gamma_dcdm = 979.48
tau =1./(Gamma_dcdm*1.02e-3)
tau

kk = np.logspace(-4,np.log10(1),1000) # k in h/Mpc

Pk_0p15_sigNOT = [] # P(k) in (Mpc/h)**3
Pk_0p3_sigNOT  = [] # P(k) in (Mpc/h)**3
Pk_0p45_sigNOT = [] # P(k) in (Mpc/h)**3

Pk_0p15_sigYES = [] # P(k) in (Mpc/h)**3
Pk_0p3_sigYES  = [] # P(k) in (Mpc/h)**3
Pk_0p45_sigYES = [] # P(k) in (Mpc/h)**3


#set general configuration
common_settings = {'output':'tCl,pCl,lCl,mPk',
                   'lensing':'yes',
                   'l_max_scalars':2600,
                   'P_k_max_1/Mpc':1.0,
                   'omega_ini_dcdm2':0.1195,
                   'omega_cdm':0.00001,
                   'Gamma_dcdm':Gamma_dcdm,
                   'n_s':0.9671,
                   'ln10^{10}A_s':3.048,
                   'tau_reio':0.0562,
                   'omega_b':0.02238,
                   'H0':67.65,
                   'N_ncdm':2,
                   'M_dcdm':1,
                   'background_ncdm_distribution': '0, 1',
                   'Quadrature strategy': '0,4',
                   'm_ncdm': '0.06, 0',
                   'N_ur':2.0328,
                   'evolver':0,
                   'l_max_ncdm':17,
                   'Number of momentum bins perturbs': '50, 300',
                   'ncdm_fluid_approximation':2,
                   'ncdm_fluid_trigger_tau_over_tau_k': 25,
                   'massive_daughter_perturbations' : 'yes',
                   'dark_radiation_perturbations': 'yes',
}

#%% read data files

#files1 = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p15_tau50gyrs_nofluid_pk.dat']
files1 = ['/Users/gfranco/cloud/output/dcdm_eps0p15_tau50gyrs_nofluid_pk.dat']

data1 = []
for data_file1 in files1:
    data1.append(np.loadtxt(data_file1))

#files1b = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p15_tau50gyrs_nofluid_cl_lensed.dat']
files1b = ['/Users/gfranco/cloud/output/dcdm_eps0p15_tau50gyrs_nofluid_cl.dat']

data1b = []
for data_file1b in files1b:
    data1b.append(np.loadtxt(data_file1b))


#files4 = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p3_tau50gyrs_nofluid_pk.dat']
files4 = ['/Users/gfranco/cloud/output/dcdm_eps0p3_tau50gyrs_nofluid_pk.dat']

data4 = []
for data_file4 in files4:
    data4.append(np.loadtxt(data_file4))

#files4b = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p3_tau50gyrs_nofluid_cl_lensed.dat']
files4b = ['/Users/gfranco/cloud/output/dcdm_eps0p3_tau50gyrs_nofluid_cl_lensed.dat']

data4b = []
for data_file4b in files4b:
    data4b.append(np.loadtxt(data_file4b))


#files5 = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p45_tau50gyrs_nofluid_pk.dat']
files5 = ['/Users/gfranco/cloud/output/dcdm_eps0p45_tau1gyrs_nofluid_pk.dat']

data5 = []
for data_file5 in files5:
    data5.append(np.loadtxt(data_file5))

#files5b = ['/home/guillermo/class_MAJORON/output/dcdm_eps0p45_tau50gyrs_nofluid_cl_lensed.dat']
files5b = ['/Users/gfranco/cloud/output/dcdm_eps0p45_tau1gyrs_nofluid_cl.dat']

data5b = []
for data_file5b in files5b:
    data5b.append(np.loadtxt(data_file5b))



pk_ref_0p15  = data1[0]
f_pk_ref_0p15 = interp1d(pk_ref_0p15[:,0], pk_ref_0p15[:,1])
cl_ref_0p15  = data1b[0]
f_clTT_ref_0p15 = interp1d(cl_ref_0p15[:,0], cl_ref_0p15[:,1])
f_clEE_ref_0p15 = interp1d(cl_ref_0p15[:,0], cl_ref_0p15[:,2])

pk_ref_0p3   = data4[0]
f_pk_ref_0p3 = interp1d(pk_ref_0p3[:,0], pk_ref_0p3[:,1])
cl_ref_0p3  = data4b[0]
f_clTT_ref_0p3 = interp1d(cl_ref_0p3[:,0], cl_ref_0p3[:,1])
f_clEE_ref_0p3 = interp1d(cl_ref_0p3[:,0], cl_ref_0p3[:,2])

pk_ref_0p45  = data5[0]
f_pk_ref_0p45 = interp1d(pk_ref_0p45[:,0], pk_ref_0p45[:,1])
cl_ref_0p45  = data5b[0]
f_clTT_ref_0p45 = interp1d(cl_ref_0p45[:,0], cl_ref_0p45[:,1])
f_clEE_ref_0p45 = interp1d(cl_ref_0p45[:,0], cl_ref_0p45[:,2])



M = Class()
#%% EPSILON=0.15 CASE ########################################################

'''
M.set(common_settings)
M.set({'epsilon_dcdm': 0.15})

M.compute()

h = M.h()
for k in kk:
    Pk_0p15_sigNOT.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)


clM_0p15 = M.lensed_cl(2600)
ll = clM_0p15['ell'][2:]
clTT_0p15 = clM_0p15['tt'][2:]
clEE_0p15 = clM_0p15['ee'][2:]

M.struct_cleanup()
M.empty()

f_Pk_0p15_sigNOT=interp1d(kk,Pk_0p15_sigNOT)
f_clTT_0p15 = interp1d(ll,ll*(ll+1.0)*clTT_0p15/(2.0*np.pi))
f_clEE_0p15 = interp1d(ll,ll*(ll+1.0)*clEE_0p15/(2.0*np.pi))
'''

#%% EPSILON=0.3 CASE ########################################################

# NON-ZERO SHEAR EQUATION
'''
M.set(common_settings)
M.set({'epsilon_dcdm': 0.3, 'switch_off_shear_wdm': 'no'})

M.compute()

h = M.h()
for k in kk:
    Pk_0p3_sigYES.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)

clM_0p3_sigYES = M.lensed_cl(2600)
ll = clM_0p3_sigYES['ell'][2:]
clTT_0p3_sigYES = clM_0p3_sigYES['tt'][2:]
clEE_0p3_sigYES = clM_0p3_sigYES['ee'][2:]


M.struct_cleanup()
M.empty()

f_Pk_0p3_sigYES = interp1d(kk,Pk_0p3_sigYES)
f_clTT_0p3_sigYES = interp1d(ll,ll*(ll+1.0)*clTT_0p3_sigYES/(2.0*np.pi))
f_clEE_0p3_sigYES = interp1d(ll,ll*(ll+1.0)*clEE_0p3_sigYES/(2.0*np.pi))

###############################################################################
# ZERO SHEAR EQUATION

M.set(common_settings)
M.set({'epsilon_dcdm': 0.3, 'switch_off_shear_wdm': 'yes'})

M.compute()

h = M.h()
for k in kk:
    Pk_0p3_sigNOT.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)

clM_0p3_sigNOT = M.lensed_cl(2600)
ll = clM_0p3_sigNOT['ell'][2:]
clTT_0p3_sigNOT = clM_0p3_sigNOT['tt'][2:]
clEE_0p3_sigNOT = clM_0p3_sigNOT['ee'][2:]


M.struct_cleanup()
M.empty()

f_Pk_0p3_sigNOT = interp1d(kk,Pk_0p3_sigNOT)
f_clTT_0p3_sigNOT = interp1d(ll,ll*(ll+1.0)*clTT_0p3_sigNOT/(2.0*np.pi))
f_clEE_0p3_sigNOT = interp1d(ll,ll*(ll+1.0)*clEE_0p3_sigNOT/(2.0*np.pi))
'''

#%% EPSILON =0.45 CASE ########################################################


# NON-ZERO SHEAR EQUATION

M.set(common_settings)
M.set({'epsilon_dcdm': 0.45, 'switch_off_shear_wdm': 'no'})

M.compute()

h = M.h()
for k in kk:
    Pk_0p45_sigYES.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)

clM_0p45_sigYES = M.lensed_cl(2600)
ll = clM_0p45_sigYES['ell'][2:]
clTT_0p45_sigYES = clM_0p45_sigYES['tt'][2:]
clEE_0p45_sigYES = clM_0p45_sigYES['ee'][2:]


M.struct_cleanup()
M.empty()

f_Pk_0p45_sigYES = interp1d(kk,Pk_0p45_sigYES)
f_clTT_0p45_sigYES = interp1d(ll,ll*(ll+1.0)*clTT_0p45_sigYES/(2.0*np.pi))
f_clEE_0p45_sigYES = interp1d(ll,ll*(ll+1.0)*clEE_0p45_sigYES/(2.0*np.pi))

###############################################################################
# ZERO SHEAR EQUATION

M.set(common_settings)
M.set({'epsilon_dcdm': 0.45, 'switch_off_shear_wdm': 'yes'})

M.compute()

h = M.h()
for k in kk:
    Pk_0p45_sigNOT.append(M.pk(k*h,0.)*h**3) # function .pk(k,z)

clM_0p45_sigNOT = M.lensed_cl(2600)
ll = clM_0p45_sigNOT['ell'][2:]
clTT_0p45_sigNOT = clM_0p45_sigNOT['tt'][2:]
clEE_0p45_sigNOT = clM_0p45_sigNOT['ee'][2:]


M.struct_cleanup()
M.empty()

f_Pk_0p45_sigNOT = interp1d(kk,Pk_0p45_sigNOT)
f_clTT_0p45_sigNOT = interp1d(ll,ll*(ll+1.0)*clTT_0p45_sigNOT/(2.0*np.pi))
f_clEE_0p45_sigNOT = interp1d(ll,ll*(ll+1.0)*clEE_0p45_sigNOT/(2.0*np.pi))

 

#%% START TO PLOT
plt.figure(1)
plt.xscale('log')
#plt.yscale('log')
plt.xlim(kk[0],kk[-1])


plt.xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$', fontsize=15)
plt.ylabel(r'$P(k)_{\mathrm{approx}}/P(k)_{\mathrm{full}}-1$', fontsize=20)
plt.title(r'$\varepsilon = 0.45, \, \, \, \, \Gamma^{-1} = %.0f \, \mathrm{Gyrs}$'%tau, fontsize = 20)

plt.plot(kk,f_Pk_0p45_sigYES(kk)/f_pk_ref_0p45(kk)-1.0,'b',label=r'$\dot{\sigma}_{\mathrm{wdm}} \neq 0$')
plt.plot(kk,f_Pk_0p45_sigNOT(kk)/f_pk_ref_0p45(kk)-1.0,'r',label=r'$\dot{\sigma}_{\mathrm{wdm}} = 0$')


#plt.ylabel(r'$P(k) \, [(\mathrm{Mpc}/h)^3]$', fontsize=20)
#plt.plot(pk_ref_0p25[:,0],pk_ref_0p25[:,1],'b',label=r'Full hierarchy')
#plt.plot(kk,Pk_0p25_sigNOT,'g',label=r'Fluid wdm with shear=0')

plt.legend(loc='best', fontsize=13)

plt.show()
plt.clf()

#%%

#ax_1 = plt.subplot(211)
#ax_2 = plt.subplot(212, sharex = ax_1)
#plt.subplots_adjust(hspace=0)

#ax_1.set_ylim([-0.04,0.04])
#ax_2.set_ylim([-0.17,0.17])
#ax_1.set_xlim([2,2500])
#ax_2.set_xlim([2,2500])

#ax_2.tick_params(axis='both', which='minor', labelsize=12)

#ax_1.semilogx(ll,f_clTT_0p3_sigNOT(ll)/f_clTT_ref_0p3(ll)-1.0,'r',label=r'$\varepsilon = 0.3, \, \, \, \, \Gamma^{-1} = 50 \, \mathrm{Gyrs}$')
#ax_2.semilogx(ll,f_clEE_0p3_sigNOT(ll)/f_clEE_ref_0p3(ll)-1.0,'r',label=r'$\varepsilon = 0.3, \, \, \, \, \Gamma^{-1} = 50 \, \mathrm{Gyrs}$')

#ax_2.set_xlabel(r'$\mathrm{multipole} \, \ell$',fontsize=15)
#ax_1.set_ylabel(r'$\frac{C_\ell^\mathrm{TT}(\mathrm{approx} )}{C_\ell^\mathrm{TT}(\mathrm{full} )} -1$',fontsize=20)
#ax_2.set_ylabel(r'$\frac{C_\ell^\mathrm{EE}(\mathrm{approx} )}{C_\ell^\mathrm{EE}(\mathrm{full} )} -1$',fontsize=20)


#ax_2.tick_params(axis="x", labelsize=18)
#ax_2.tick_params(axis="y", labelsize=18)
#ax_1.tick_params(axis="y", labelsize=18)

#ax_1.legend(frameon=False,fontsize =15,loc='upper left',borderaxespad=0.)
#plt.show()

#plt.clf()
