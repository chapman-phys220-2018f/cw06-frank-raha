#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####
# Raha and Frank
# Email: pirzadeh@chapman.edu
# Elementary module for CW 5
# PHYS 220
# 10/1/18
####

import scipy.constants

class Particle(object):
    """Particle is a class that should have 3 initialized variables: Mass(a float), Position(A triplet of floats), Momentum(A triplet of floats)"""
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)

    def __init__(self, x, y, z):
        """Inits the class, arg1: x position float, arg2: y position float, arg3: z positionfloat"""
        self.position = (x, y, z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        """Alters the momentum by the impulse amount. Needs floating point triple."""
        self.momentum = (self.momentum[0]+px,self.momentum[1]+py,self.momentum[2]+pz)

    def move(self, dt):
        self.position = (self.position[0] + (dt/self.mass)*self.momentum[0],self.position[1]+(dt/self.mass)*self.momentum[1],self.position[2]+(dt/self.mass)*self.momentum[2])


class ChargedParticle(Particle):
    charge = 0.0

    def __init__(self, x, y, z):
        """uses the super constructor to construct the class instance"""
        super(Particle,self).__init__(x, y, z)
        self.charge = 0.0

class Electron(ChargedParticle):

    def __init__(self, x, y, z):
        self.charge = -scipy.constants.e
        super(ChargedParticle,self).__init__(x, y, z)
        self.mass = scipy.constants.m_e

class Proton(ChargedParticle):

    def __init__(self, x, y, z):
        self.charge = scipy.constants.e
        super(ChargedParticle,self).__init__(x, y, z)
        self.mass = scipy.constants.m_p

    def main(argv):
        pass