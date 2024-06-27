import os
import sys
import tty
import termios
import colorama
from distutils.spawn import find_executable
from .. import const

init_output = colorama.init

branch_coverage_getch = {
    "try_block": False,
    "exception_block": False,
    "finally_block": False
}

branch_coverage_get_key = {
    "const_key_mapping_branch": False,
    "escape_branch": False,
    "up_arrow_branch": False,
    "down_arrow_branch": False,
    "default_branch": False
}

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
        branch_coverage_getch["try_block"] = True
        return char
    except Exception as e:
        branch_coverage_getch["exception_block"] = True
        raise e
    finally:
        branch_coverage_getch["finally_block"] = True
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def get_key():
    ch = getch()

    if ch in const.KEY_MAPPING:
        branch_coverage_get_key["const_key_mapping_branch"] = True
        return const.KEY_MAPPING[ch]
    elif ch == '\x1b':
        branch_coverage_get_key["escape_branch"] = True
        next_ch = getch()
        if next_ch == '[':
            last_ch = getch()

            if last_ch == 'A':
                branch_coverage_get_key["up_arrow_branch"] = True
                return const.KEY_UP
            elif last_ch == 'B':
                branch_coverage_get_key["down_arrow_branch"] = True
                return const.KEY_DOWN

    branch_coverage_get_key["default_branch"] = True
    return ch



def open_command(arg):
    if find_executable('xdg-open'):
        return 'xdg-open ' + arg
    return 'open ' + arg


try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


def _expanduser(self):
    return self.__class__(os.path.expanduser(str(self)))


if not hasattr(Path, 'expanduser'):
    Path.expanduser = _expanduser
