from restic_common import send_notification, rclone_sync 
import sys
import os

patronArchivosLlaves = "llaves*.kdbx"
aegisBackupFileFilter = "/aegis-backup-*.json"
# resticBackup = "/restic_backup"
llavesBackup = "/llaves_backup"
aegisBackup = "/aegis_backup"
llavesFolder = "/llaves"
# Arg 1 - source
# Arg 2 - destiny
# Arg 3 - pcloud backup folder


def main():

    print("arg 1: ", sys.argv[1], "arg 2 ", sys.argv[2], "arg 3", sys.argv[3])
    rclone_sync(sys.argv[1] + llavesFolder, sys.argv[2] +
                llavesBackup, patronArchivosLlaves)
    rclone_sync(sys.argv[3] + aegisBackup, sys.argv[2] +
                aegisBackup, aegisBackupFileFilter)
    send_notification("Finished backup")


if __name__ == "__main__":
    main()
