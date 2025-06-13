from restic_common import send_notification

import time
import sys
import os


def main():
    send_notification(f"Starting backup {sys.argv[1]}. 3 Min until first attempt at getting pass")
    
    time.sleep(180)

    send_notification(f"Starting backup now")



if __name__ == "__main__":
    main()
