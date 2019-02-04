import numpy as np
from wave import open as open_wave
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