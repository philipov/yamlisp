#-- __main.py

"""
unit tests
"""

import pytest

#----------------------------------------------------------------------#


def test__Config( path_root_config ):
    from yamlisp.config import Config

    config0     = Config()

    config1     = Config( path_root_config )

    assert False


#----------------------------------------------------------------------#
