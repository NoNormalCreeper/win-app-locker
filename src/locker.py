from .utils import read_banlist, read_preference
import win32api, win32con, subprocess

preferences = read_preference()
ban_list = read_banlist()
warning_title = preferences['warning_title']
warning_message = preferences['warning_message']

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
    killed_apps = []
    for app in ban_list:
        cmd = f"taskkill /f /im {app}"
        if 'SUCCESS' in run_cmd(cmd):
            win32api.MessageBox(0, warning_message, warning_title, win32con.MB_ICONWARNING)
            killed_apps.append(app)
    return killed_apps if killed_apps else None