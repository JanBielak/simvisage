'''
Created on Jun 16, 2010

@author: alexander
'''
from etsproxy.traits.api import \
    HasTraits, Float, Array, implements, Property, cached_property, Instance, Enum, \
    Dict, Bool, Int, List

import numpy as np

from numpy import c_

import scipy as sp

from os.path import join

from math import pi


class GeoSUPPRT(HasTraits):
    '''Geometry definition of the tappered support.
    Linear reduction of the stiffness of the support.
    '''

    #-----------------------------------------------------------------
    # geometric parameters of the support
    #-----------------------------------------------------------------
    # NOTE: coordinate system is placed at the edge of the slab test/support

    #-----------------
    # geometry:
    #-----------------

    # x and y-direction 
    #
    width_supprt = Float(0.10, input = True)

    # z-direction
    #
    thickness_supprt = Float(0.02, input = True)

    def __call__(self, pts):
        print '*** geo_slab_test called ***' 
        
        L = self.width_supprt
        t = self.thickness_supprt
        
        x_, y_, z_ = pts.T

        dz_red_ = (x_ + y_ - x_ * y_ )

        x = x_ * L
        y = y_ * L
        z = z_ * t
        idx_z_ = np.where( z_ == 0.0 )[0]
        z[ idx_z_ ] = ( z_[ idx_z_ ] + dz_red_[ idx_z_ ] ) * t
        
        pts = c_[x, y, z]

        # rotate coordinates in order to have the load introduction plate at the 
        # top left corner of the grid
        #
#        pts = np.c_[L-x, L-y, z]
#        pts = np.c_[x, y, z]

#        # switch order of the points in order to start in the opposite corner of the slab
#        # instead of the center of the load introduction plate. The opposite center of the 
#        # slab corresponds to the origin of the slab in the model 'sim_st' (as generated by
#        # the FEGrid mesh; 
#        # 
#        pts = pts[::-1]
#        # switch back the order of the z-axis in order to maintain starting from 0
#        #
#        pts[:,-1] = pts[:,-1][::-1]
        
        return pts




if __name__ == '__main__':

    from etsproxy.mayavi import mlab

    geo_supprt = GeoSUPPRT()

    # discretization of total slab in x- and y-direction
    #
    shape_xy = 4

    # discretization in z-direction 
    # (thickness direction):
    #
    shape_z = 1

    grid = np.mgrid[0:1:complex(0, shape_xy + 1),
                    0:1:complex(0, shape_xy + 1),
                    0:1:complex(0, shape_z + 1)]

    X, Y, Z = grid

    gpoints = np.c_[ X.flatten(), Y.flatten(), Z.flatten() ]
    
    mlab.figure(bgcolor=(1.,1.,1.,))
    fp1 = geo_supprt(gpoints)
    mlab.points3d(fp1[:, 0], fp1[:, 1], fp1[:, 2],
                   scale_factor = 0.003 ,
                   resolution = 8)
    mlab.axes()
    mlab.show()