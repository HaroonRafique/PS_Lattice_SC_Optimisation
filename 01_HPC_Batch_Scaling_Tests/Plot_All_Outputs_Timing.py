# Plots all available plottable data from output.mat as individual files
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import scipy.io as sio 
import matplotlib.cm as cm

plt.rcParams['figure.figsize'] = [8.0, 4.0]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.rcParams['font.size'] = 10
plt.rcParams['legend.fontsize'] = 'medium'
plt.rcParams['lines.linewidth'] = 1

'''
add_input_file:
dd: dictionary of particle data dictionaries. key = user defined label
filename: input file name (with relative path from this file)
label: file label e.g. 'case 1', 'case 2', ...
'''
def add_input_file(dd, filename, label):
	f = filename
	p = dict()
	sio.loadmat(f, mdict=p)
	dd[label] = p
	print '\tAdded output data from ', filename, '\t dictionary key: ', label
	return dd

'''
plot_turn_time: Required arguments:
sc:			string: space charge used (for plot titles only)
dd: dictionary of particle data dictionaries. key = user defined label
filename: 			e.g. 'Testing' gives Testing_bunchlength.png.
Plots ptc (hardcoded), PyORBIT, and PyORBIT effective optics functions
beta, alpha, dispersion, in x and y. Also creates two text files
optics.txt : MAD-X TFS like file with all optics functions
optics_2.txt: raw arrays for use elsewhere
'''
def plot_turn_time(sc, dd, filename):

	print 'Plotting turn time'

	fig1 = plt.figure(facecolor='w', edgecolor='k')
	ax1 = fig1.add_subplot(111)

	# ~ colors = cm.rainbow(np.linspace(0, 1, len(dd.keys())))
	# ~ c_it = int(0)
	
	all_nodes = []

	for key, value in sorted(dd.iteritems()):

		# To get the number of nodes we have a naming convention in the dictionary label
		nodes = int(key.split()[0])
		all_nodes.append(nodes)

		print '\n\tCase: ', key, ' <turn duration> = ', np.mean(dd[key]['turn_duration'][0])
		if 'Optimised' in key:
			col = 'r'
		if 'Original' in key:
			col = 'k'
		ax1.scatter(nodes, np.mean(dd[key]['turn_duration'][0]), label=key, color=col);
		# ~ c_it = c_it + 1
		
	final_nodes = np.unique(all_nodes, axis=0)
	
	ax1.set_xticks(final_nodes)

	custom_lines = [Line2D([0], [0], color='k', lw=4), Line2D([0], [0], color='r', lw=4)]
	ax1.legend(custom_lines, ['Original', 'Optimised'], title='Case')

	ax1.set_ylabel('Time [s]');
	ax1.set_xlabel('HPC-Batch Nodes [-] (20 cores per node)');
	ax1.grid(True);
	
	ax1.set_title('PS 2200 turns, no space charge, tracking only')

	figname = filename + '.png'

	fig1.savefig(figname);
	plt.close()
	return;
'''
------------------------------------------------------------------------
						Open files and read data
------------------------------------------------------------------------
'''
	
# Create dd dictionary
dd = dict()
dd = add_input_file(dd, './01_Original_Lattice_Tracking/output/output.mat', '1 Original')
dd = add_input_file(dd, './02_Original_Lattice_Tracking/output/output.mat', '2 Original')
dd = add_input_file(dd, './03_Original_Lattice_Tracking/output/output.mat', '3 Original')
dd = add_input_file(dd, './04_Original_Lattice_Tracking/output/output.mat', '4 Original')
dd = add_input_file(dd, './05_Original_Lattice_Tracking/output/output.mat', '5 Original')
dd = add_input_file(dd, './11_New_Lattice_Tracking/output/output.mat', '1 Optimised')
dd = add_input_file(dd, './12_New_Lattice_Tracking/output/output.mat', '2 Optimised')
dd = add_input_file(dd, './13_New_Lattice_Tracking/output/output.mat', '3 Optimised')
dd = add_input_file(dd, './14_New_Lattice_Tracking/output/output.mat', '4 Optimised')
dd = add_input_file(dd, './15_New_Lattice_Tracking/output/output.mat', '5 Optimised')
print 'Final data dictionary keys: ', dd.keys()
		
sc = 'NoSC'
main_label = 'Timing'
main_label2 = main_label + '_zoom'
scaled_label = main_label + '_scaled'
legend_label = 'Nodes'
turn_tot = None
zoom_turns = 15
turns = [0, 1, 10, 100, 199, 874, 2185]

'''
------------------------------------------------------------------------
								Plot
------------------------------------------------------------------------
'''

plot_turn_time(sc, dd, main_label)
