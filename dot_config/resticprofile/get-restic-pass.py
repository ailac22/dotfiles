#!/usr/bin/env python3
# File: /usr/local/bin/keepassxc-password.py

import subprocess
import time
import sys
from restic_common import *

# Configuration
MAX_ATTEMPTS = 3
DELAY = 300  # Seconds between attempts


def main():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        password, success = get_password()
        if success:
            print(password)
            sys.exit(0)

        send_notification(
            f"Attempt {
                attempt} Failed: KeePassXC is not open or database is locked. "
            f"Please unlock it. Retrying in {DELAY} seconds..."
        )
        time.sleep(DELAY)

    send_notification(f"Failed: Could not retrieve password from KeePassXC after {
                      MAX_ATTEMPTS} attempts.")
    sys.exit(1)


if __name__ == "__main__":
    main()
