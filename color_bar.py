#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl

def make_colormap(seq):
	"""Return a LinearSegmentedColormap
	seq: a sequence of floats and RGB-tuples. The floats should be increasing
	and in the interval (0,1).
	"""
	seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
	cdict = {'red': [], 'green': [], 'blue': []}
	for i, item in enumerate(seq):
		if isinstance(item, float):
			r1, g1, b1 = seq[i - 1]
			r2, g2, b2 = seq[i + 1]
			cdict['red'].append([item, r1, r2])
			cdict['green'].append([item, g1, g2])
			cdict['blue'].append([item, b1, b2])
	return mcolors.LinearSegmentedColormap('CustomMap', cdict)

c = mcolors.ColorConverter().to_rgb
bgr = make_colormap([c('blue'),c('lime'),0.50,c('lime'),c('red'),1.00,c('red')])
bgr.set_over('red')

fig = plt.figure(figsize=(2,8))
ax1 = fig.add_axes([0.10,0.10,0.40,0.75])
#cmap = mpl.cm.cool
#cmap.set_under('0.75')
norm = mpl.colors.Normalize(vmin=0,vmax=8)

cb1 = mpl.colorbar.ColorbarBase(ax1,cmap=bgr,norm=norm,orientation='vertical',extend='max')
cb1.ax.tick_params(labelsize=14,width=2,length=7)
cb1.set_label(r'RMSD ($\AA$)',fontsize=16)

plt.savefig('cbar.png')

