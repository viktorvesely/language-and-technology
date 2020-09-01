import sys
import numpy as np
import math
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100 # or sample frequency
DEFAULT_AMPLITUDE = 1
DEFAULT_PHI = 0

DURATION = 1
FREQUENCY = 2
AMPLITUDE = 3
PHI = 4

TIME = 1
PRESSURE = 0

def to_time_step(total_time, step, max_step):
    portion = step / max_step
    return total_time * portion

def periodic(t, f, A=DEFAULT_AMPLITUDE, phi=DEFAULT_PHI):
    n_samples = int(t * SAMPLE_RATE)
    samples = []
    sample_times = np.linspace(0, t, num=n_samples, endpoint=False)
    for i in range(n_samples):
        current_time = sample_times[i]
        angle = math.pi * (2 * f * current_time + phi)
        sample = A * math.cos(angle)
        samples.append(sample) 
    return samples, sample_times

def plot_wave(wave1, wave2, labels):
    
    plt.plot(wave1[TIME], wave1[PRESSURE], color='blue', label=[0])
    plt.plot(wave2[TIME], wave2[PRESSURE], color='red', label=labels[1])

    plt.show()


if __name__ == '__main__':
    dur = float(sys.argv[DURATION])
    f = float(sys.argv[FREQUENCY])
    A = DEFAULT_AMPLITUDE
    phi = DEFAULT_PHI

    __length = len(sys.argv)

    if __length > 3:
        A = float(sys.argv[AMPLITUDE])
    
    if __length > 4:
        phi  = float(sys.argv[PHI])    

    x, sample_times = periodic(dur, f, A=A, phi=phi)
    x0, sample_times0 = periodic(dur, f, A=A)

    print(x[:10])
    

    plot_wave([x, sample_times],[x0, sample_times0], ["X", "X0"])