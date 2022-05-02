"""
Let Windows run main.pyw with Windows startup.
"""
import os
import sys

bat_file_name = 'startuppyw.bat'

startup_dir = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

fixed_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
mainfile_path = os.path.join(fixed_path, 'main.pyw')

bat_content = ""
bat_content += "@echo off\n"
bat_content += "pythonw {mainfile_path}\n"

with open(os.path.join(startup_dir, bat_file_name), 'w', encoding='utf-8') as f:
    f.write(bat_content)

print('Done!')
print(f'{bat_file_name} created in {startup_dir}')