from restic_common import send_notification

import time
import sys


def main():
    send_notification(
        f"Starting backup {sys.argv[1]}. 2 Min until first attempt at getting pass")
    time.sleep(120)


if __name__ == "__main__":
    main()
