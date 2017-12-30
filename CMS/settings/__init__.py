import os


if os.uname().nodename == 'production_nodename':
    from .deploy import *
else:
    from .develop import *
