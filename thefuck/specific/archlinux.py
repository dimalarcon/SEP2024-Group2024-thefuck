""" This file provide some utility functions for Arch Linux specific rules."""
import subprocess
from .. import utils


@utils.memoize
def get_pkgfile(command):
    """ Gets the packages that provide the given command using `pkgfile`.

    If the command is of the form `sudo foo`, searches for the `foo` command
    instead.
    """
    try:
        command = command.strip()

        if command.startswith('sudo '):
            command = command[5:]

        command = command.split(" ")[0]

        packages = subprocess.check_output(
            ['pkgfile', '-b', '-v', command],
            universal_newlines=True, stderr=utils.DEVNULL
        ).splitlines()

        return [package.split()[0] for package in packages]
    except subprocess.CalledProcessError as err:
        if err.returncode == 1 and err.output == "":
            return []
        else:
            raise err

# Initialize coverage tracking global variable
branch_coverage = {
    "archlinux_env_1": False,  #if utils.which('yay'):
    "archlinux_env_2": False,  #elif utils.which('pikaur'):
    "archlinux_env_3": False,  #elif utils.which('yaourt'):
    "archlinux_env_4": False,  #elif utils.which('pacman'):
    "archlinux_env_5": False,  #else:
}

def archlinux_env():
    if utils.which('yay'):
        branch_coverage['archlinux_env_1'] = True
        pacman = 'yay'
    elif utils.which('pikaur'):
        branch_coverage['archlinux_env_2'] = True
        pacman = 'pikaur'
    elif utils.which('yaourt'):
        branch_coverage['archlinux_env_3'] = True
        pacman = 'yaourt'
    elif utils.which('pacman'):
        branch_coverage['archlinux_env_4'] = True
        pacman = 'sudo pacman'
    else:
        branch_coverage['archlinux_env_5'] = True
        return False, None

    enabled_by_default = utils.which('pkgfile')

    return enabled_by_default, pacman
