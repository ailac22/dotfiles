import subprocess
import time
import sys

# Configuration
MAX_ATTEMPTS = 3
DELAY = 300  # Seconds between attempts


def send_notification(message, urgency="critical"):
    """Send a notification to dunst using notify-send."""
    subprocess.run(
        ["notify-send", "-u", urgency, "resticprofile Backup", message],
        check=True,
    )


# def get_password(attribute, value):
#     """Attempt to retrieve password from KeePassXC Secret Service."""
#     try:
#         result = subprocess.run(
#             ["secret-tool", "lookup", attribute, value],
#             capture_output=True,
#             text=True,
#             check=True,
#         )
#         return result.stdout.strip(), True
#     except subprocess.CalledProcessError:
#         return None, False


# def get_password_with_retry(attribute: str, value: str) -> str:
#     """
#     Get password from KeePassXC with retry logic.
#
#     Args:
#         attribute: The attribute for secret-tool lookup
#         value: The value for secret-tool lookup
#
#     Returns:
#         The password if successful, None if failed
#     """
#     for attempt in range(1, MAX_ATTEMPTS + 1):
#         password, success = get_password(attribute, value)
#         if success:
#             return password
#
#         send_notification(
#             f"Attempt {
#                 attempt} Failed: KeePassXC is not open or database is locked. "
#             f"Please unlock it. Retrying in {DELAY} seconds..."
#         )
#         time.sleep(DELAY)
#
#     send_notification(f"Failed: Could not retrieve password from KeePassXC after {
#                       MAX_ATTEMPTS} attempts.")
#     return None


def rclone_sync(source: str, destination: str, include_filter: str = None, options: list = None):

    if source.rstrip('/') == destination.rstrip('/'):
        print("Source and destination directories are the same. Sync operation skipped.")
        return

    # Build the command
    cmd = ['rclone', 'sync', source, destination, "-v", "--dry-run"]

    # Add include filter if specified
    if include_filter:
        cmd.append(f'--include={include_filter}')

    print("Ejecutando ", cmd)
    # Add any extra options
    if options:
        cmd.extend(options)

    try:
        result = subprocess.run(
            cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Sync completed successfully.")
        print("Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sync failed.")
        print("Error output:\n", e.stderr)
