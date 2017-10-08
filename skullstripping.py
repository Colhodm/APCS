import scipy.io as sio
#from __future__ import print_function
from builtins import str
from builtins import range

import os                                    # system functions
from PIL import Image
from nipype import config
# config.enable_provenance()

from nipype.interfaces import spm, fsl

# In order to use this example with SPM's matlab common runtime
# matlab_cmd = ('/Users/satra/Downloads/spm8/run_spm8.sh '
#               '/Applications/MATLAB/MATLAB_Compiler_Runtime/v713/ script')
# spm.SPMCommand.set_mlab_paths(matlab_cmd=matlab_cmd, use_mcr=True)

import nipype.interfaces.io as nio           # Data i/o
import nipype.interfaces.utility as util     # utility
import nipype.pipeline.engine as pe          # pypeline engine
import nipype.algorithms.rapidart as ra      # artifact detection
import nipype.algorithms.modelgen as model   # model specification
import nipype.interfaces.matlab as mlab
from nipype.interfaces import fsl


#a = sio.loadmat('/Users/Colhodm/Desktop/filesfortiff/Desktop1.tif')
#a = sio.loadmat('/Users/Colhodm/Documents/m1.nii')
for i in range(369,370):
	skullstrip = fsl.BET(in_file ="/Users/Colhodm/Documents/" + str(i) + "m.nii",out_file="//Users/Colhodm/Documents/" +str(i) +  "m.nii.layer", mask=True) 
	D = skullstrip.run()
	print(D)

