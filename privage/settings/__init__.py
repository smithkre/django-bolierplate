import os
import sys
import __future__

env = os.environ.get('ENV', 'DEV')

if env == 'PROD':
    from .production import *
else:
    try:
        from .localhost import *
        env = 'LOCAL'
    except:
        from .development import *

print('Django is starting with', env, 'setting.')
