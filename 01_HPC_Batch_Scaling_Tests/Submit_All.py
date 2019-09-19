import os

sbs = True

master_dir = os.getcwd()

sbs_locations = []

sbs_locations.append('/01_Original_Lattice_Tracking')
sbs_locations.append('/02_Original_Lattice_Tracking')
sbs_locations.append('/03_Original_Lattice_Tracking')
sbs_locations.append('/04_Original_Lattice_Tracking')
sbs_locations.append('/05_Original_Lattice_Tracking')
sbs_locations.append('/11_New_Lattice_Tracking')
sbs_locations.append('/12_New_Lattice_Tracking')
sbs_locations.append('/13_New_Lattice_Tracking')
sbs_locations.append('/14_New_Lattice_Tracking')
sbs_locations.append('/15_New_Lattice_Tracking')

if sbs:
	for loc in sbs_locations:
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'		
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)		
		os.system(submit_command)
