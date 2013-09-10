"""
    This module calculates the blackbody function for the fits,
    with two parameters (fc and w) or only one parameter (fc).
    
    Marina von Steinkirch, spring/2013
"""

from constants import hc_keV, h_keV, erg_to_keV, Teff
from pylab import *



def blackbody(parameters, energy, index):
    """
        The Planck function for a blackbody spectrum.
    """
    b = []
    w0 = parameters[0]
    fc0 = parameters[1]
    T = Teff[index]
    for i in range(len(energy)):
        b.append((w0/2) * (energy[i])**3 * (1/(exp(energy[i]/(fc0*T)) -1)) / hc_keV**2 / h_keV * (1/(erg_to_keV)))
    
    return b



def blackbody_one_param(parameter, energy, index):
    """
        The Planck function for a blackbody spectrum.
    """
    b = []
    fc0 = parameter[0]
    T = Teff[index]
    for i in range(len(energy)):
        b.append(((1/(fc0**4))/2) * (energy[i])**3 * (1/(exp(energy[i]/(fc0*T)) -1)) / hc_keV**2 / h_keV * (1/(erg_to_keV)))
    
    return b

