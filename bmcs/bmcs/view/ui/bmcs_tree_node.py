'''
Created on 14. 4. 2014

@author: Vancikv
'''

from traits.api import \
    HasStrictTraits, Str, List, WeakRef, \
    Property, cached_property

from traitsui.api import \
    View
from traits.api import Range  

class BMCSLeafNode(HasStrictTraits):
    '''Base class of all model classes that can appear in a tree view.
    '''
    node_name = Str('<unnamed>')

    def draw(self, fig):
        return


class BMCSTreeNode(HasStrictTraits):
    '''Base class of all model classes that can appear in a tree view.
    '''
    node_name = Str('<unnamed>')

    tree_node_list = List([])

    tree_view = View()
    
    def append_node(self, node):
        '''Add a new subnode to the current node.
        Inform the tree view to select the new node within the view.
        '''
        self.tree_node_list.append(node)

    def plot(self, fig):
        '''Plot the content of the current node.
        '''
        return


class ReinfLayoutTreeNode(BMCSTreeNode):
    '''Class accommodating the list of all reinforcement components.
    '''
    node_name = Str('Reinforcement layout')

    cs_state = WeakRef(HasStrictTraits)

    def __getstate__(self):
        '''Overriding __getstate__ because of WeakRef usage
        '''
        state = super(HasStrictTraits, self).__getstate__()

        for key in ['cs_state', 'cs_state_']:
            if state.has_key(key):
                del state[key]

        return state

    def plot(self, fig):
        ax = fig.add_subplot(1, 1, 1)
        self.cs_state.plot_geometry(ax)

    tree_node_list = Property(
        depends_on='cs_state.reinf_components_with_state')

    @cached_property
    def _get_tree_node_list(self):
        self.cs_state.changed = True
        return self.cs_state.reinf_components_with_state
