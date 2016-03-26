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

	#plot_1d(time[:], datalist1[:,i], 'k', 'Time', 'RGYR', '%02d.%s.%s' %(i, system, selection), 'RGYR', xunits = 'ns', yunits = '$\AA$')
	
	plot_1d(time[:], datalist1[:,i], 'k', 'Time', 'RGYR', '%02d.%s.%s' %(i, system, selection), 'RGYR', average = True, xunits = 'ns', yunits = '$\AA$')

	hist1d(datalist1[:,i], 'RGYR', 100, '%02d.%s.%s' %(i, system, selection), 'RGYR', xunits = '$\AA$')

	hist1d(datalist1[:,i], 'RGYR', 100, '%02d.%s.%s' %(i, system, selection), 'RGYR', norm = True, average = True, xunits = '$\AA$')

	scat_hist(time[:], datalist1[:,i], 'k', 'Time (ns)', 'RGYR ($\AA$)', '%02d.%s.%s' %(i, system, selection), 'RGYR', 100)

hist2d(datalist1[:,0],datalist1[:,1], 'Column 0 RGYR ($\AA$)', 'Column 1 RGYR ($\AA$)', 100, '%s.%s' %(system, selection), 'RGYR', False)

# OTHER UTILITIES:
#PLOTTING MULTIPLE LINES ON THE SAME FIGURE:
plt.plot(time[:], datalist1[:,0], c='firebrick')
plt.plot(time[:], datalist1[:,1], c='royalblue')
plt.legend(['column 0', 'column 1'], bbox_to_anchor=(-0.05, 1.03, 1.1, .102), fontsize='10', loc=3, ncol=2, mode='expand', borderaxespad=0.)
#plt.show()
plt.savefig('two_lines.png')
plt.close()
