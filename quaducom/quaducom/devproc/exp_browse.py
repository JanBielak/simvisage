'''
Created on Mar 15, 2012

@author: rch
'''

import os.path

from matresdev.db.simdb import \
    SimDB

simdb = SimDB()

from matresdev.db.exdb.ex_run_view import ExRunView

ex_path = os.path.join(simdb.exdata_dir, 'tensile_tests', 'dog_bone', '2012-03-20_TT-12c-4cm-0-TU_SH3',
                        'TT-12c-4cm-TU-0-SH3-V2.DAT')

#ex_path = os.path.join(simdb.exdata_dir, 'bending_tests', 'four_point', '2012-04-03_BT-4PT-12c-6cm-0-TU',
#                                        'BT-4PT-12c-6cm-SH4', 'BT-4PT-12c-6cm-SH4-V1.DAT')
#ex_path = os.path.join(simdb.exdata_dir, 'bending_tests', 'four_point', '2012-04-03_BT-4PT-12c-6cm-0-TU',
#                                       'BT-4PT-12c-6cm-SH4', 'BT-4PT-12c-6cm-SH4-V1.DAT')



print os.path.exists(ex_path)

doe_reader = ExRunView(data_file = ex_path)

#print 'model', doe_reader.model.ex_type.Kraft
#print 'model', doe_reader.model.ex_type.WA_VL 
#print 'model', doe_reader.model.ex_type.WA_VR
#print 'model', doe_reader.model.ex_type.WA_HL
#print 'model', doe_reader.model.ex_type.WA_HR

doe_reader.configure_traits()
