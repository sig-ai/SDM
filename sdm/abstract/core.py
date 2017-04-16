from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import six
from abc import ABCMeta, abstractmethod, abstractproperty
import torch

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
class Sensor:

    @abstractmethod
    def observe(self):
        pass

    @abstractproperty
    def space(self):
        pass

    def __call__(self):
        return self.observe()


@six.add_metaclass(ABCMeta)
class Actuator:

    @abstractmethod
    def act(self):
        pass

    @abstractproperty
    def space(self):
        pass

    def __call__(self):
        self.act()



@six.add_metaclass(ABCMeta)
class AbstractAgent:

    def __init__(self, sensor, actuator, model):
        in_shape = model.input_shape
        out_shape = model(torch.zeros(1, *in_shape)).shape
        if in_shape != sensor.space.shape():
            raise ValueError
        self.sensor = sensor
        self.actuator = actuator
