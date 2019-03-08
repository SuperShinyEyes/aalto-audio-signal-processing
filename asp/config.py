from pathlib import Path
import os
class EasyDict(dict):

    def __getattribute__(self, name): return self[name]
    def __setattr__(self, name, value): self[name] = value
    def __delattr__(self, name): del self[name]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

paths = EasyDict()
paths.base = Path(BASE_DIR)
paths.data = list( [str(p) for p in (paths.base / 'data').iterdir()] )