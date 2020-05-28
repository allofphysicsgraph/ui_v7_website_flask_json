#!/usr/bin/env python3

import sympy  # type: ignore
from sympy.parsing.latex import parse_latex  # type: ignore
import common_lib as clib
from typing import Tuple  # , TextIO
import logging
import random
import re
import latex_to_sympy

# https://docs.sympy.org/latest/modules/physics/units/examples.html
import sympy.physics.units.systems
import sympy.physics.units.systems.si
import sympy.physics.units


logger = logging.getLogger(__name__)

# https://pymotw.com/3/doctest/
# how to use doctest for the entire file:
# python -m doctest -v validate_inference_rules_sympy.py

# testing per function on the command line:
# import doctest
# from validate_inference_rules_sympy import *
# doctest.run_docstring_examples(split_expr_into_lhs_rhs, globals(), verbose=True)

def validate_dimensions(expr_global_id: str, path_to_db: str) -> str:
    """
    >>> validate_dimensions()
    """
    trace_id = str(random.randint(1000000, 9999999))
    logger.info("[trace start " + trace_id + "]")

    #logger.debug('expr_global_id = ' + expr_global_id)

    dat = clib.read_db(path_to_db)

    if expr_global_id in dat['expressions'].keys():
        latex_expr_str = dat['expressions'][expr_global_id]['latex']
    else:
        raise Exception(expr_global_id + " is not in dat expressions")

    LHS, RHS = latex_to_sympy.split_expr_into_lhs_rhs(latex_expr_str)

    logger.debug('LHS = ' + str(LHS))
    logger.debug('RHS = ' + str(RHS))

    list_of_symbols = latex_to_sympy.get_symbols_from_latex(latex_expr_str)
    logger.debug('list of symbols = ' + str(list_of_symbols))

    # for each symbol, what is the dimension according to PDG?
    logger.debug(str(dat['expressions'][expr_global_id]['AST']))

    return "just a stub"

# EOF
