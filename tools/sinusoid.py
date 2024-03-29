import numpy as np


def sinusoid(min_, max_, period, t, phase_shift, dt=1.):
    """
    Phi is a sinusoid function related to neuron inhibition.
    It follows the general sine wave function:
        f(x) = amplitude * (2 * pi * frequency * time)
    In order to adapt to the phi_min and phi_max parameters the amplitude
    and an additive shift term have to change.
    Frequency in discrete time has to be adapted from the given tau_0
    period in continuous time.
    """
    amplitude = (max_ - min_) / 2
    frequency = (1 / period) * dt
    shift = min_ + amplitude  # Moves the wave in the y-axis

    return \
        amplitude \
        * np.sin(2 * np.pi * (t + phase_shift / dt) * frequency) \
        + shift
