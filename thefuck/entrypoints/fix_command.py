from pprint import pformat
import os
import sys
from difflib import SequenceMatcher
from .. import logs, types, const
from ..conf import settings
from ..corrector import get_corrected_commands
from ..exceptions import EmptyCommand
from ..ui import select_command
from ..utils import get_alias, get_all_executables

branch_coverage = {
    "fix_command_EmptyCommand": False,  # except EmptyCommand
    "fix_command_no_selected_command": False,  # if selected_command:
    "fix_command_with_selected_command": False,  # else:
}

def _get_raw_command(known_args):
    if known_args.force_command:
        return [known_args.force_command]
    elif not os.environ.get('TF_HISTORY'):
        return known_args.command
    else:
        history = os.environ['TF_HISTORY'].split('\n')[::-1]
        alias = get_alias()
        executables = get_all_executables()
        for command in history:
            diff = SequenceMatcher(a=alias, b=command).ratio()
            if diff < const.DIFF_WITH_ALIAS or command in executables:
                return [command]
    return []


def fix_command(known_args):
    """Fixes previous command. Used when `thefuck` called without arguments."""
    settings.init(known_args)
    with logs.debug_time('Total'):
        logs.debug(u'Run with settings: {}'.format(pformat(settings)))
        raw_command = _get_raw_command(known_args)

        try:
            command = types.Command.from_raw_script(raw_command)
        except EmptyCommand:
            branch_coverage['fix_command_EmptyCommand'] = True
            logs.debug('Empty command, nothing to do')
            return

        corrected_commands = get_corrected_commands(command)
        selected_command = select_command(corrected_commands)

        if selected_command:
            branch_coverage['fix_command_with_selected_command'] = True
            selected_command.run(command)
        else:
            branch_coverage['fix_command_no_selected_command'] = True
            sys.exit(1)
