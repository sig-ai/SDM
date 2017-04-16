from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import random
import sys
import numpy as np


class Discrete(object):
    """
    Discrete space from [0, dims-1]
    """
    def __init__(self, dims):
        self._dims = dims


    def sample(self):
        """
        Randomly sample from distribution space
        """
        return random.randrange(self.dims)


    def __eq__(self, other):
        if isinstance(other, Discrete):
            return other.dims == self.dims

        return False


    def __repr__(self):
        return "Discrete(%d)" % (self.dims)


    def __str__(self):
        return "Discrete space from 0 to %d" % (self.dims - 1)

    @property
    def dims(self):
        return self._dims



class Box(object):
    """
    Continuous space for R^n, all from a lower bound to an upper bound
    if lower or upper is None, there is no bound (we use MAX_INT and MIN_INT to bound it)
    """
    def __init__(self, dims, lower=sys.maxint, upper=(-sys.maxint-1)):
        self._dims = dims
        self._lower = lower
        self._upper = upper


    def sample(self):
        """
        Return a random sample from the R^n space.
        """
        return np.array([random.randrange(self.lower, self.upper) for _ in range(self.dims)])


    def __repr__(self):
        return "Box(%d, %d, %d)" % (self.dims, self.lower, self.upper)


    def __str__(self):
        return "Continuous Space of %d dimensions in [%d, %d]" % (self.dims, self.lower, self.upper)


    def __eq__(self, other):
        if isinstance(other, Box):
            return (other.dims == self.dims) and (other.lower == self.lower) and (other.upper and self.upper)

        return False

    @property
    def dims(self):
        return self._dims


    @property
    def lower(self):
        return self._lower


    @property
    def upper(self):
        return self._upper
