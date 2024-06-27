"""Attempts to spellcheck and correct failed cd commands"""

import os
import six
from thefuck.specific.sudo import sudo_support
from thefuck.rules import cd_mkdir
from thefuck.utils import for_app, get_close_matches

__author__ = "mmussomele"

MAX_ALLOWED_DIFF = 0.6


def _get_sub_dirs(parent):
    """Returns a list of the child directories of the given parent directory"""
    return [child for child in os.listdir(parent) if os.path.isdir(os.path.join(parent, child))]


@sudo_support
@for_app('cd')
def match(command):
    """Match function copied from cd_mkdir.py"""
    return (
        command.script.startswith('cd ') and any((
            'no such file or directory' in command.output.lower(),
            'cd: can\'t cd to' in command.output.lower(),
            'does not exist' in command.output.lower()
        )))

# Initialize coverage tracking global variable
branch_coverage = {
    "get_new_command_1": False,  #if dest[-1] == '':
    "get_new_command_2": False,  #if dest[-1] == '':
    "get_new_command_3": False,  #elif six.PY2:
    "get_new_command_4": False,  #else:
    "get_new_command_5": False,  #if directory == ".":
    "get_new_command_6": False,  #elif directory == "..":
    "get_new_command_7": False,  #if best_matches:
    "get_new_command_8": False   #else:
}

@sudo_support
def get_new_command(command):
    """
    Attempt to rebuild the path string by spellchecking the directories.
    If it fails (i.e. no directories are a close enough match), then it
    defaults to the rules of cd_mkdir.
    Change sensitivity by changing MAX_ALLOWED_DIFF. Default value is 0.6
    """
    dest = command.script_parts[1].split(os.sep)
    if dest[-1] == '':
        branch_coverage["get_new_command_1"] = True
        dest = dest[:-1]

    if dest[-1] == '':
        branch_coverage["get_new_command_2"] = True
        cwd = os.sep
        dest = dest[1:]
    elif six.PY2:
        branch_coverage["get_new_command_3"] = True
        cwd = os.getcwdu()
    else:
        branch_coverage["get_new_command_4"] = True
        cwd = os.getcwd()
    for directory in dest:
        if directory == ".":
            branch_coverage["get_new_command_5"] = True
            continue
        elif directory == "..":
            branch_coverage["get_new_command_6"] = True
            cwd = os.path.split(cwd)[0]
            continue
        best_matches = get_close_matches(directory, _get_sub_dirs(cwd), cutoff=MAX_ALLOWED_DIFF)
        if best_matches:
            branch_coverage["get_new_command_7"] = True
            cwd = os.path.join(cwd, best_matches[0])
        else:
            branch_coverage["get_new_command_8"] = True
            return cd_mkdir.get_new_command(command)
    return u'cd "{0}"'.format(cwd)
