import numpy as np
from wave import open as open_wave
import matplotlib.pyplot as plt
import IPython
import pathlib
import logging

log = logging.getLogger(__name__)

__all__ = ['Wave', 'read_wave']

class Wave:

    def __init__(self, ys, ts=None, framerate=44100):
        self.ys = np.asanyarray(ys)
        self.framerate = framerate
        if ts is None:
            self.ts = np.arange(len(ys)) / self.framerate
        else:
            self.ts = ts


    @property
    def start(self):
        return self.ts[0]

    @property
    def end(self):
        return self.ts[-1]

    def normalize(self, amp=1.0):
        self.ys = normalize(self.ys, amp=amp)

    def make_audio(self):
        audio = None
        try:
            audio = IPython.display.Audio(data=self.ys, rate=self.framerate)
        except ModuleNotFoundError:
            log.warn("Can't import IPython.display.Audio.")
        finally:
            return audio

    def plot(self, ax=None, title=''):
        plot(self.ts, self.ys, ax, title)

    def make_spectrum(self):
        n = len(self.ys)
        period = 1 / self.framerate
        
        hs = np.fft.rfft(self.ys)
        fs = np.fft.rfftfreq(n, period)

        return Spectrum(hs, fs, self.framerate)

    def slice(self, start, end):
        return Wave(
            ys          = self.ys[start:end].copy(),
            ts          = self.ts[start:end].copy(),
            framerate   = self.framerate
        )

    def window(self, window):
        self.ys *= window

    def make_spectrogram(self, seg_length, window_flag=True):
        if window_flag:
            window = np.hamming(seg_length)
        i, j = 0, seg_length
        step = seg_length // 2

        spectrum_map = dict()

        while j < len(self.ys):
            segment = self.slice(i, j)
            if window_flag:
                segment.window(window)
            t = (segment.start + segment.end) / 2
            spectrum_map[t] = segment.make_spectrum()

            i += step
            j += step

        return Spectrogram(spectrum_map, seg_length)


class Spectrum:

    def __init__(self, hs, fs, framerate):
        self.hs = np.asanyarray(hs)
        self.fs = np.asanyarray(fs)
        self.framerate = framerate

    @property
    def amps(self):
        return np.abs(self.hs)

    def plot(self, cut_off=None, ax=None, title='', log_scale_flag=True):
        if log_scale_flag:
            plot(self.fs, np.log10(self.amps), ax, title)
        else:
            plot(self.fs, self.amps, ax, title)
        

def plot(xs, ys, ax=None, title=''):

    if ax is None:
        plt.plot(xs, ys)
    else:
        ax.plot(xs, ys)
        ax.set_title(title)

def normalize(ys, amp=1.0):
    high, low = abs(max(ys)), abs(min(ys))
    return amp * ys / max(high, low)

def read_wave(filename='sound.wav'):
    """Reads a wave file.

    filename: string

    returns: Wave
    """
    if type(filename) is pathlib.PosixPath:
        filename = str(filename)
    fp = open_wave(filename, 'r')

    nchannels = fp.getnchannels()
    nframes = fp.getnframes()
    sampwidth = fp.getsampwidth()
    framerate = fp.getframerate()
    
    z_str = fp.readframes(nframes)
    
    fp.close()

    dtype_map = {1:np.int8, 2:np.int16, 3:'special', 4:np.int32}
    if sampwidth not in dtype_map:
        raise ValueError('sampwidth %d unknown' % sampwidth)
    
    if sampwidth == 3:
        xs = np.fromstring(z_str, dtype=np.int8).astype(np.int32)
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.fromstring(z_str, dtype=dtype_map[sampwidth])

    # if it's in stereo, just pull out the first channel
    if nchannels == 2:
        ys = ys[::2]

    #ts = np.arange(len(ys)) / framerate
    wave = Wave(ys, framerate=framerate)
    wave.normalize()
    return wave


class Spectrogram:
    def __init__(self, spectrum_map, seg_length):
        self.spectrum_map = spectrum_map
        self.seg_length = seg_length

    def any_spectrum(self):
        index = next(iter(self.spectrum_map))
        return self.spectrum_map[index]

    def frequencies(self):
        return self.any_spectrum().fs

    def times(self):
        return sorted(iter(self.spectrum_map))

    def plot(self, ax=None, title=''):
        fs = self.frequencies()
        ts = self.times()

        size = len(fs), len(ts)
        