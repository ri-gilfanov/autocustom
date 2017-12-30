import os


if os.uname().nodename == 'pharmacosphere':
    from .deploy import *
else:
    from .develop import *