import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10.0, 6.0]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.rcParams['font.size'] = 6
plt.rcParams['legend.fontsize'] = 'small'
plt.rcParams['figure.titlesize'] = 'medium'

plt.rcParams['lines.linewidth'] = 0.5

# Open Files

original_file='original_ptc_twiss'
optimised_file='optimised_ptc_twiss'

s18 = []
betx18 = []
bety18 = []
dx18 = []
dxp18 = []
mux18 = []
muy18 = []

s = []
betx = []
bety = []
dx = []
dxp = []
mux = []
muy = []

plot_betax = 1
plot_betay = 1
plot_dx = 1

beta = 0.15448

# Read Data

fin1=open(optimised_file,'r').readlines()[90:]

for l in fin1:
    s18.append(float(l.split()[0]))
    betx18.append(float(l.split()[2]))
    bety18.append(float(l.split()[4]))
    dx18.append(float(l.split()[8]))

fin2=open(original_file,'r').readlines()[90:]

for f in fin2:
    s.append(float(f.split()[0]))
    betx.append(float(f.split()[2]))
    bety.append(float(f.split()[4]))
    dx.append(float(f.split()[8]))

############
#   Betas  #
############

if(plot_betax):
    fig, ax1 = plt.subplots();

    plt.title(r"PS Lattice Optimisation $\beta_x$");
    ax1.plot(s18, betx18, 'k-', label='Original Beta_x', linewidth=1.5);
    ax1.plot(s, betx, 'r-', label='Optimised Beta_x', linewidth=1.5);

    ax1.set_xlabel("s [m]");
    ax1.set_ylabel(r'$\beta_x$ [m]', color='k');
    # ~ ax1.plot(s18, bety18, 'g-', label='Original Beta_y', linewidth=1.5);
    # ~ ax1.plot(s, bety, 'b:', label='Optimised Beta_y', linewidth=1.5);
    # Make the y-axis label, ticks and tick labels match the line color.
    # ~ ax1.tick_params('y', colors='b');
    # ~ ax1.set_yscale('log')

    # ~ plt.xlim(100,300);
    #~ ax1.set_xlim(0,220);
    # ~ ax1.set_ylim(1.8E4, 2.8E4);
    ax1.xaxis.grid(color='k', linestyle=':', linewidth=0.5)
    ax1.yaxis.grid(color='k', linestyle=':', linewidth=0.5)

    # ~ ax2 = ax1.twinx();
    # ~ ax2.set_ylabel("Beta [m]", color='r');
    # ~ ax2.tick_params('y', colors='r');
    #~ ax2.set_yscale('log')

    # ~ ax2.set_ylim(50,300);


    ax1.legend(loc = 2);
    # ~ ax2.legend(loc = 1);

    fig.tight_layout();
    #~ plt.show();
    plt.savefig('Beta_x.png', dpi = 800);
    
if(plot_betay):
    fig, ax1 = plt.subplots();

    plt.title(r"PS Lattice Optimisation $\beta_y$");
    # ~ ax1.plot(s18, betx18, 'k-', label='Original Beta_x', linewidth=1.5);
    # ~ ax1.plot(s, betx, 'r:', label='Optimised Beta_x', linewidth=1.5);

    ax1.set_xlabel("s [m]");
    ax1.set_ylabel(r"$\beta_y$ [m]", color='k');
    ax1.plot(s18, bety18, 'k-', label='Original Beta_y', linewidth=1.5);
    ax1.plot(s, bety, 'r-', label='Optimised Beta_y', linewidth=1.5);
    # Make the y-axis label, ticks and tick labels match the line color.
    # ~ ax1.tick_params('y', colors='b');
    # ~ ax1.set_yscale('log')

    ax1.xaxis.grid(color='k', linestyle=':', linewidth=0.5)
    ax1.yaxis.grid(color='k', linestyle=':', linewidth=0.5)

    # ~ ax2 = ax1.twinx();
    # ~ ax2.set_ylabel("Beta [m]", color='r');
    # ~ ax2.tick_params('y', colors='r');
    #~ ax2.set_yscale('log')

    # ~ ax2.set_ylim(50,300);


    ax1.legend(loc = 2);
    # ~ ax2.legend(loc = 1);

    fig.tight_layout();
    #~ plt.show();
    plt.savefig('Beta_y.png', dpi = 800);

#################
#   Dispersion  #
#################

if(plot_betax):
    fig, ax1 = plt.subplots();

    plt.title("SIS18 D_x");
    ax1.plot(s18, dx18, 'k-', label=r'Original D$_x$', linewidth=1.5);
    ax1.plot(s, dx, 'r-', label=r'Optimised D$_x$', linewidth=1.5);
    ax1.set_xlabel("s [m]");
    ax1.set_ylabel("D [m]", color='k');
    
    # ~ ax1.tick_params('y', colors='b');
    # ~ ax1.set_yscale('log')

    # ~ ax1.set_ylim(1.8E4, 2.8E4);
    ax1.xaxis.grid(color='k', linestyle=':', linewidth=0.5)
    ax1.yaxis.grid(color='k', linestyle=':', linewidth=0.5)

    # ~ ax2 = ax1.twinx();
    # ~ ax1.plot(s18, dx18, 'k-', label='SIS18 Beta_x', linewidth=1.5);   
    # ~ ax2.plot(s, dx, 'r:', label='PTC Dx', linewidth=1.5);
    # ~ ax2.set_ylabel("D [m]", color='r');
    # ~ ax2.tick_params('y', colors='r');
    #~ ax2.set_yscale('log')

    # ~ ax2.set_ylim(50,300);


    ax1.legend(loc = 2);
    # ~ ax2.legend(loc = 1);

    fig.tight_layout();
    #~ plt.show();
    plt.savefig('Dx.png', dpi = 800);
