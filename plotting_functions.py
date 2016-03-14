#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# USAGE:
# from fn_plotting.py import *


# PREAMBLE:

import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

# ----------------------------------------
# PLOTTING SUBROUTINES

#time evolution, line plot
def plot_1d(xdata, ydata, color, x_axis, y_axis, system, analysis):
	
	""" Creates a 1D scatter/line plot:

	Usage: time_evol(xdata, ydata, color, x_axis, y_axis, system, analysis)
	
	Arguments:
	xdata, ydata: self-explanatory
	color: color to be used to plot data
	x_axis, y_axis: strings to be used for the axis label
	system: descriptor for the system that produced the data
	analysis: descriptor for the analysis that produced the data
	
	"""

	plt.plot(xdata, ydata, '%s' %(color))	# create the initial plot
#	plt.show()
	plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
#	plt.show()
#	plt.title(r'something here...' %(system), size='14')
	plt.xlabel(r'%s' %(x_axis), size=12)
	plt.ylabel(r'%s' %(y_axis), size=12)
#	plt.show()
#	plt.xlim((0,200))
#	plt.ylim((1.5, 3.0))
	plt.savefig('%s.%s.tevol.png' %(system,analysis))
	plt.close()

#	if average != False:
#		avg = np.sum(ydata)/len(ydata)
#		SD = stdev(ydata)
#		SDOM = SD/sqrt(len(ydata))
#		plt.axhline(avg, xmin=0.0, xmax=1.0, c='r')
#		plt.figtext(0.775, 0.815, '%s, %s\n%6.4f $\\pm$ %6.4f %s \nSD = %4.3f %s' %(system,analysis,avg, SDOM,units,SD,units), bbox=dict(boxstyle='square', ec='r', fc='w'), fontsize=12)


# histogram - 1D, bar
def hist1d(data, x_axis, num_b, system, analysis, norm):
	""" Creates a 1D histogram:

	Usage: hist1d(data, x_axis, num_b, system, analysis, norm)
	
	Arguments:
	data: self-explanatory
	x_axis: string to be used for the axis label
	num_b: number of bins to be used when binning the data
	system: descriptor for the system analyzed
	analysis: descriptor for the analysis performed and plotted
	norm = [False][True]; if False, plotting a frequency of data; if True, plotting a probability density

	"""
	
	events, edges, patches = plt.hist(data, bins=num_b, histtype = 'bar', normed=norm)
	plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
	plt.xlabel(r'%s' %(x_axis), size=12)
#	plt.title(r'something here...' %(system), size='14')

	if norm == True:
		plt.ylabel('Probability Density')
		plt.savefig('%s.%s.prob1d.png' %(system,analysis))
		nf = open('%s.%s.prob1d.dat' %(system,analysis),'w')
	else:
		plt.ylabel('Frequency', size=12)
		plt.savefig('%s.%s.hist1d.png' %(system,analysis))
		nf = open('%s.%s.hist1d.dat' %(system,analysis), 'w')

	for i in range(len(events)):
		nf.write('%10.1f      %10.4f\n' %(events[i], edges[i]))
	
	plt.close()
	nf.close()
	events = []
	edges = []
	patches = []


# Combined plot of a 1D scatter plot and a 1D histogram
def scat_hist(xdata, ydata, color, x_axis, y_axis, system, analysis, num_b):
	""" Creates 1D scatter plot w/ a 1D histogram

	Usage: scat_hist(xdata, ydata, color, x_axis, y_axis, system, analysis, num_b)
	
	Arguments:
	xdata, ydata: self-explanatory
	color: color to be used to plot data
	x_axis, y_axis: strings to be printed on the axi labels
	system: descriptor for the system analyzed
	analysis: descriptor for the analysis performed and plotted
	num_b: number of bins to be used when binning the data
	"""

	left, width = 0.1, 0.65
	bottom, height = 0.1, 0.8
	bottom_h = left_h = left+width+0.01
	rect_scatter = [left, bottom, width, height]
	rect_histy = [left_h, bottom, 0.2, height]
	
	plt.figure(1, figsize=(10,8))
	axScatter =plt.axes(rect_scatter)
	axScatter.plot(xdata, ydata, '%s.' %(color))
	plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
#	plt.xlim((0,500))
	plt.ylabel(r'%s' %(y_axis),size=12)
	plt.xlabel(r'%s' %(x_axis),size=12)

	axHisty = plt.axes(rect_histy)
	axHisty.yaxis.set_major_formatter(nullfmt)
	axHisty.xaxis.set_major_formatter(nullfmt)
	plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
	axHisty.hist(ydata, bins=num_b, orientation='horizontal', color = ['gray'])
	axHisty.set_ylim(axScatter.get_ylim())
	
	plt.savefig('%s.%s.scat_hist.png' %(system, analysis))
	plt.close()


def hist2d(xdata, ydata, x_axis, y_axis, num_b, system, analysis, norm):
	""" Creates a 2D histogram (heat map)
	
	Usage: hist2d(xdata, ydata, x_axis, y_axis, num_b, system, analysis, norm)
	
	Arguments:
	xdata, ydata: self-explanatory
	x_axis, y_axis: strings to be printed on the axi labels
	num_b: number of bins to be used when binning the data
	system: descriptor for the system analyzed
	analysis: descriptor for the analysis performed and plotted
	norm = [False][True]; if False, plotting a frequency of data; if True, plotting a probability density
	"""

	my_cmap = plt.cm.get_cmap('jet')
	my_cmap.set_under('w')
	counts, xedges, yedges, image = plt.hist2d(xdata, ydata, bins=num_b, normed=norm, cmap=my_cmap, vmin=0.001)#, cmap=plt.get_cmap('jet')) # cmap: jet (blue to red), blues (white to blue), ...
	cb1 = plt.colorbar()
	if norm == True:
		cb1.set_label('Prob. Density', size=12)
	else:
		cb1.set_label('Frequency')
#	plt.title('Distribution of Base Pair interactions - %s-%s' %(base_a, base_b))
	plt.xlim((0,8))
	plt.ylim((0,8))
	plt.xlabel(r'%s' %(x_axis), size=12)
	plt.ylabel(r'%s' %(y_axis), size=12)
	plt.savefig('%s.%s.hist2d.png' %(system, analysis))
	plt.close()
	counts = []
	xedges = []
	yedges = []
	image = []

