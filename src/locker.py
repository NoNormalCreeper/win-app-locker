from distutils.command.config import config
from .utils import config
from .log import log
import win32api, win32con, subprocess
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import asyncio


preferences = config.preference
ban_list = config.preference
warning_title = preferences['warning_title']
warning_message = preferences['warning_message']

def show_warning_box(message: str, title: str) -> None:
    """
    Shows a warning box
    """
    asyncio.get_running_loop().run_in_executor(None, partial(
        win32api.MessageBox, 0, message, title, win32con.MB_ICONWARNING))

async def show_error_box(message: str, title: str) -> None:
    """
    Shows an error box
    """
    asyncio.get_running_loop().run_in_executor(None, partial(
        win32api.MessageBox, 0, message, title, win32con.MB_ICONERROR))

def run_cmd(cmd: str) -> list:
    """
    Runs a command in the background and returns the output.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return p.communicate()[0].decode('utf-8').split('\n')

async def kill_all_app(ban_list: list) -> None:
    """
    Kills all programs in the banlist
    Returns a list of killed apps
    """
    killed_apps = []
    for app in ban_list:
        cmd = f"taskkill /f /im {app}"
        run_result = run_cmd(cmd)
        for line in run_result:
            if 'SUCCESS' in line:
                killed_apps.append(app)
                show_warning_box(warning_message, warning_title)
                break
    if killed_apps:
        log(f'Successfully killed {killed_apps}')