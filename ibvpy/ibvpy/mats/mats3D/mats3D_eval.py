'''
Created on Sep 3, 2009

@author: jakub
'''

from etsproxy.traits.api import Callable, Constant

from ibvpy.mats.mats_eval import MATSEval

# @todo parameterize - should be specialized in the dimensional subclasses
from ibvpy.mats.mats3D.mats3D_tensor import \
    map3d_eps_eng_to_mtx, map3d_sig_eng_to_mtx, map3d_eps_mtx_to_eng, map3d_sig_mtx_to_eng, \
    map3d_ijkl2mn, map3d_tns2_to_tns4, map3d_tns4_to_tns2, compliance_mapping3d

class MATS3DEval( MATSEval ):

    # number of spatial dimensions of an integration cell for the material model
    #
    n_dims = Constant( 3 )

    # dimension dependent tensor mappings
    #
    map_tns4_to_tns2 = Callable( map3d_tns4_to_tns2, transient = True )
    map_eps_eng_to_mtx = Callable( map3d_eps_eng_to_mtx, transient = True )
    map_sig_eng_to_mtx = Callable( map3d_sig_eng_to_mtx, transient = True )
    compliance_mapping = Callable( compliance_mapping3d, transient = True )
    map_sig_mtx_to_eng = Callable( map3d_sig_mtx_to_eng, transient = True )
    map_eps_mtx_to_eng = Callable( map3d_eps_mtx_to_eng, transient = True )
