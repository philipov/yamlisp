
"""
manipulate onetick configuration files
"""

from termcolor import colored
from termcolor import cprint

import colorama
colorama.init( )

import colored_traceback
colored_traceback.add_hook( )

import logging
log = logging.getLogger( name="yamlisp.config" )
log.debug = lambda *a, **b : None
# log.debug = print

################################

import re

from collections import OrderedDict
from copy import deepcopy

from pathlib import Path
from .path import stack_of_files
from .path import try_resolve

from .yaml import read as read_yaml
from .yaml import rprint
from .eval import eval_yamlisp
from .functions import PathList, PathList2
from .functions import DelayedPath


#----------------------------------------------------------------------#

expression_regex = re.compile(
r"""    \${                             # ${
        ((?P<namespace>[^{}]+?)::)?     #   namespace::         [optional]
        ((?P<section>[^:{}]+?):)?       #   section:            [optional]
        (?P<key>[^:{}]+?)               #   key                 -required-
        }                               #  }
""", re.VERBOSE)

####################





#----------------------------------------------------------------------#


class ConfigTree:

    #----------------------------------------------------------------#
    #----------------------------------------------------------------#

    ####################
    def __init__( self, root_file: Path = None ) :

        self.nodes = list()



    #----------------------------------------------------------------#
    #----------------------------------------------------------------#



#----------------------------------------------------------------------#


class Config:
    pattern_keyvalue    = re.compile( r"""^(?P<key>[^#=]+)""" + r"""[\s]*=[\s]*""" + r"""(?P<value>[^#='"]*)""" )
    pattern_comment     = re.compile( r"""#.*$""" )

    section_names       = ['pkg', 'path', 'shell', 'keyval']
    envvar_sections     = ['pkg', 'path', 'shell']
    sections_to_write   = ['shell', 'keyval']

    #----------------------------------------------------------------#
    #----------------------------------------------------------------#

    ####################
    def __init__( self, target_file: Path = None ) :

        self.name       = None
        self.filepath   = None
        self.yaml_data  = None
        self.eval_data  = OrderedDict()
        self.flat_data  = OrderedDict()

        self.tree       = None
        self.parents    = OrderedDict()
        self.children   = OrderedDict()

        # try:


        #self.read_yaml( target_file )


    #----------------------------------------------------------------#
    #----------------------------------------------------------------#


    ####################
    def read_yaml( self, filepath_target: Path ) :

        path_target = filepath_target.parents[0]
        log.debug( colored(
            "***********************************************************************************************************",
            'green', attrs=['bold'] ), path_target )
        self.name = path_target

        struct = read_yaml( filepath_target )       ### Read Yaml File

        if 'config' not in struct :
            raise ValueError( 'yaml does not contain config section' )

        if not isinstance( struct['config'], dict ) :
            raise ValueError( "config should contain a dict, instead:" + str( type( struct['config'] ) ) )

        for section_name in self.section_names :
            try :
                data = self.load_parameters( struct, section_name, path_target )
            except KeyError :
                data = OrderedDict( )

            # self.data_raw[section_name] = data
            # self.data[section_name] = data


#----------------------------------------------------------------------#
