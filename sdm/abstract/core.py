from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import six
from abc import ABCMeta, abstractmethod, abstractproperty


@six.add_metaclass(ABCMeta)
class AbstractWorld:
    @abstractmethod
    def step(self, *args):
        pass

    @abstractproperty
    def state(self):
        pass

    @abstractproperty
    def reset(self):
        pass

    @abstractproperty
    def min_agents(self):
        pass

    @abstractproperty
    def max_agents(self):
        pass

    @abstractproperty
    def num_agents(self):
        pass
    

@six.add_metaclass(ABCMeta)
class AbstractAgent:
    pass
