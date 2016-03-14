#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# USAGE:
# ./rgyr_plotting.py data_file system_qualifier

# PREAMBLE:

from plotting_functions import *

dat1 = sys.argv[1]  
system = sys.argv[2]

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
	selection = sel[i][0]

	plot_1d(time[:], datalist1[:,i], 'k', 'Time (ns)', 'RGYR ($\AA$)', '%02d.%s.%s' %(i, system, selection), 'RGYR')

	hist1d(datalist1[:,i], 'RGYR ($\AA$)', 100, '%02d.%s.%s' %(i, system, selection), 'RGYR', False)

	hist1d(datalist1[:,i], 'RGYR ($\AA$)', 100, '%02d.%s.%s' %(i, system, selection), 'RGYR', True)

	scat_hist(time[:], datalist1[:,i], 'k', 'Time (ns)', 'RGYR ($\AA$)', '%02d.%s.%s' %(i, system, selection), 'RGYR', 100)

hist2d(datalist1[:,0],datalist1[:,1], 'Column 1 RGYR ($\AA$)', 'Column 2 RGYR ($\AA$)', 100, '%s.%s' %(system, selection), 'RGYR', False)

