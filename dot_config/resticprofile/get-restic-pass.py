#!/usr/bin/env python3
# File: /usr/local/bin/keepassxc-password.py

import sys
import os
from restic_common import get_password_with_retry


def main():
    password = get_password_with_retry("backup_type", "restic")
    if password is None:
        sys.exit(1)
    
    os.environ["RESTIC_PASSWORD"] = password
    print(password)


if __name__ == "__main__":
    main()

