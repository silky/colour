#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .all import MUNSELL_COLOURS_ALL
from .experimental import MUNSELL_COLOURS_1929
from .real import MUNSELL_COLOURS_REAL

__all__ = ['MUNSELL_COLOURS_ALL']
__all__ += ['MUNSELL_COLOURS_1929']
__all__ += ['MUNSELL_COLOURS_REAL']

MUNSELL_COLOURS = {
    'Munsell Colours All': MUNSELL_COLOURS_ALL,
    'Munsell Colours 1929': MUNSELL_COLOURS_1929,
    'Munsell Colours Real': MUNSELL_COLOURS_REAL}
"""
Aggregated *Munsell* colours.

MUNSELL_COLOURS : dict

Aliases:

-   'all': 'Munsell Colours All'
-   '1929': 'Munsell Colours 1929'
-   'real': 'Munsell Colours Real'
"""
MUNSELL_COLOURS['all'] = MUNSELL_COLOURS['Munsell Colours All']
MUNSELL_COLOURS['1929'] = MUNSELL_COLOURS['Munsell Colours 1929']
MUNSELL_COLOURS['real'] = MUNSELL_COLOURS['Munsell Colours Real']

__all__ += ['MUNSELL_COLOURS']
