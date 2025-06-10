import subprocess


def send_notification(message, urgency="critical"):
    """Send a notification to dunst using notify-send."""
    subprocess.run(
        ["notify-send", "-u", urgency, "resticprofile Backup", message],
        check=True,
    )


def get_password():
    """Attempt to retrieve password from KeePassXC Secret Service."""
    try:
        result = subprocess.run(
            ["secret-tool", "lookup", "backup_type", "restic"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip(), True
    except subprocess.CalledProcessError:
        return None, False
