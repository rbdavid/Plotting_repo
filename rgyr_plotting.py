#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# USAGE:
# ./rgyr_plotting.py data_file system_qualifier

# PREAMBLE:

from fn_plotting import *

dat1 = sys.argv[1]  
system1 = sys.argv[2]

sel = []
sel.append(['protein','firebrick'])
sel.append(['protein-12','royalblue'])

# ----------------------------------------
# MAIN PROGRAM:

datalist1 = np.loadtxt(dat1)
nSteps = len(datalist1[:,0])

time = np.zeros(nSteps)
for i in range(nSteps):
	time[i] = i*0.002	# units of time in ns; each frame is separated by 0.002 ns 

for i in range(len(sel)):
	system = sel[i][0]
	num = i

	plot_1d(time[:], datalist1[:,i], 'k', 'Time (ns)', 'RGYR ($\AA$)', '%02d.%s.%s' %(num, system1, system), 'RGYR')

	hist1d(datalist1[:,i], 'RGYR ($\AA$)', 100, '%02d.%s.%s' %(num, system1, system), 'RGYR', False)

	hist1d(datalist1[:,i], 'RGYR ($\AA$)', 100, '%02d.%s.%s' %(num, system1, system), 'RGYR', True)

	scat_hist(time[:], datalist1[:,i], 'k', 'Time (ns)', 'RGYR ($\AA$)', '%02d.%s.%s' %(num, system1, system), 'RGYR', 100)

