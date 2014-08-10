#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines units tests for :mod:`colour.algebra.extrapolation` module.
"""

from __future__ import unicode_literals

import sys
import numpy as np

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.algebra import Extrapolator1d
from colour.algebra import LinearInterpolator1d

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["TestExtrapolator1d"]


class TestExtrapolator1d(unittest.TestCase):
    """
    Defines :func:`colour.algebra.extrapolation.Extrapolator1d` class units
    tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ("interpolator",)

        for attribute in required_attributes:
            self.assertIn(attribute, dir(Extrapolator1d))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ()

        for method in required_methods:
            self.assertIn(method, dir(Extrapolator1d))

    def test___call__(self):
        """
        Tests :func:`colour.algebra.extrapolation.Extrapolator1d.__call__`
        method.
        """

        extrapolator = Extrapolator1d(
            LinearInterpolator1d(
                np.array([5., 6., 7.]),
                np.array([5., 6., 7.])))

        np.testing.assert_almost_equal(extrapolator([4., 8.]), [4., 8.])
        self.assertEqual(extrapolator(4.), 4.)


if __name__ == "__main__":
    unittest.main()