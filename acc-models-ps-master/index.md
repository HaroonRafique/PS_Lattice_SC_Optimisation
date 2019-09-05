<h1> Proton Synchrotron Optics Repository </h1>

This website contains the official optics models for the CERN Proton Synchrotron. For each scenario listed below 
(and the various configurations belonging to each scenario), MAD-X input scripts, Twiss tables and
optics plots are available and can be browsed. 

The repository will soon be available on EOS and AFS and you can also clone the repository from Gitlab.

!!! note "Clone of the Gitlab repository"
		If you would like to have a local copy of the repository on your computer, you can clone it using the following syntax:

			git clone https://gitlab.cern.ch/acc-models/acc-models-ps.git
 

<h2> Operational optics scenarios</h2>


- [Bare machine](scenarios/bare_machine/index.md) - Combined function magnets only.

- [AD](scenarios/ad/index.md) - Proton beams for the Antiproton Decelerator.

- [EAST](scenarios/east/index.md) - Proton beams for the EAST area.

- [LHC ION](scenarios/lhc_ion/index.md) - Lead ion beams for the LHC physics programme.

- [LHC PROTON](scenarios/lhc_proton/index.md) - Proton beams produced for the LHC physics programme.

- [SFTPRO](scenarios/sftpro/index.md) - Proton beams produced for the SPS fixed target physics programme.

- [TOF](scenarios/tof/index.md) - Proton beams for the n_TOF fixed target physics programme.


<h2> Data structure </h2>

The data for the different operational scenarios quoted above are organized in the following way:

<ul>
<li><b>Optics scenario</b>: each scenario corresponds to a certain operational cycle (i.e. beam and/or user).</li>

<li><b>Configuration</b>: the state of the machine for a specific instant along the cycle (e.g. injection,
flat bottom, ...).</li>

</ul>

For each configuration the values of several parameters (energy, transverse tunes, optical functions at the various BI monitors) 
as well as Twiss tables and plots of the optics functions are provided.
