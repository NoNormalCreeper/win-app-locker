import (
    win32api,
    win32con,
    subprocess
)

def run_cmd(cmd: str) -> list:
    """
    Runs a command in the background and returns the output.
    """
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.readlines()

def kill_all_app(ban_list: list) -> list:
    """
    Kills all programs in the banlist
    Returns a list of killed apps
    """
    cmd = f"taskkill /f /im {app}"
    killed_apps = []
    for app in ban_list:
        if 'SUCCESS' in run_cmd(cmd):
            win32api.MessageBox(0, "别玩啦！", "WARNING",win32con.MB_ICONWARNING)
            killed_apps.append(app)
    return killed_apps if killed_apps else None