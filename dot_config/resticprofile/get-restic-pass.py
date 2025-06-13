#!/usr/bin/env python3
# File: /usr/local/bin/keepassxc-password.py

import sys
import os
from restic_common import get_password_with_retry


def main():


    # profile_name = sys.argv[1]
    # # Set rclone password for cloud backup
    # if profile_name == "cloud" and "RCLONE_CONFIG_PASS" not in os.environ:
    #     password = get_password_with_retry("backup_type", "rclone")
    #     if password is None:
    #         send_notification("Failed to get rclone password, backup might fail")
    #     else:
    #         os.environ["RCLONE_CONFIG_PASS"] = password

    password = get_password_with_retry("backup_type", "restic")
    if password is None:
        sys.exit(1)
    
    os.environ["RESTIC_PASSWORD"] = password
    print(password)


if __name__ == "__main__":
    main()

