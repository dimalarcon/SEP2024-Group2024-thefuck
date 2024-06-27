import pytest
from mock import Mock
from unittest.mock import patch, MagicMock
from thefuck.entrypoints.fix_command import _get_raw_command, fix_command, branch_coverage
from thefuck.exceptions import EmptyCommand


class TestGetRawCommand(object):
    def test_from_force_command_argument(self):
        known_args = Mock(force_command='git brunch')
        assert _get_raw_command(known_args) == ['git brunch']

    def test_from_command_argument(self, os_environ):
        os_environ['TF_HISTORY'] = None
        known_args = Mock(force_command=None,
                          command=['sl'])
        assert _get_raw_command(known_args) == ['sl']

    @pytest.mark.parametrize('history, result', [
        ('git br', 'git br'),
        ('git br\nfcuk', 'git br'),
        ('git br\nfcuk\nls', 'ls'),
        ('git br\nfcuk\nls\nfuk', 'ls')])
    def test_from_history(self, os_environ, history, result):
        os_environ['TF_HISTORY'] = history
        known_args = Mock(force_command=None,
                          command=None)
        assert _get_raw_command(known_args) == [result]

class TestFixCommand(object):
    @patch('thefuck.entrypoints.fix_command.settings')
    @patch('thefuck.entrypoints.fix_command.logs')
    @patch('thefuck.entrypoints.fix_command.types.Command.from_raw_script')
    @patch('thefuck.entrypoints.fix_command.get_corrected_commands')
    @patch('thefuck.entrypoints.fix_command.select_command')
    def test_fix(self, mock_select_command, mock_get_corrected_commands, mock_from_raw_script, mock_logs, mock_settings):
        # Mock known_args
        known_args = Mock(command=['echo hello'], force_command=None)

        # Mock the behavior of settings.init
        mock_settings.init = MagicMock()

        # Mock the behavior of logs.debug_time
        mock_logs.debug_time = MagicMock()
        mock_logs.debug = MagicMock()

        # Mock the behavior of from_raw_script
        mock_command = MagicMock()
        mock_from_raw_script.return_value = mock_command

        # Mock the behavior of get_corrected_commands
        mock_corrected_commands = [MagicMock()]
        mock_get_corrected_commands.return_value = mock_corrected_commands

        # Mock the behavior of select_command
        mock_selected_command = MagicMock()
        mock_select_command.return_value = mock_selected_command

        # Call the function
        fix_command(known_args)

        # Assert that settings.init was called with known_args
        mock_settings.init.assert_called_once_with(known_args)

        # Assert that from_raw_script was called with the raw command
        mock_from_raw_script.assert_called_once_with(known_args.command)

        # Assert that get_corrected_commands was called with the command
        mock_get_corrected_commands.assert_called_once_with(mock_command)

        # Assert that select_command was called with the corrected commands
        mock_select_command.assert_called_once_with(mock_corrected_commands)

        # Assert that the selected command's run method was called with the command
        mock_selected_command.run.assert_called_once_with(mock_command)

    @patch('thefuck.entrypoints.fix_command.settings')
    @patch('thefuck.entrypoints.fix_command.logs')
    @patch('thefuck.entrypoints.fix_command.types.Command.from_raw_script', side_effect=EmptyCommand)
    def test_fix_empty_command(self, mock_from_raw_script, mock_logs, mock_settings):
        # Mock known_args
        known_args = Mock(command=['echo hello'], force_command=None)

        # Mock the behavior of settings.init
        mock_settings.init = MagicMock()

        # Mock the behavior of logs.debug_time
        mock_logs.debug_time = MagicMock()
        mock_logs.debug = MagicMock()

        # Call the function
        fix_command(known_args)

        # Assert that settings.init was called with known_args
        mock_settings.init.assert_called_once_with(known_args)

        # Assert that from_raw_script was called and raised EmptyCommand
        mock_from_raw_script.assert_called_once_with(known_args.command)

        # Assert that a debug message was logged for the empty command
        mock_logs.debug.assert_any_call('Empty command, nothing to do')

        print(branch_coverage)

        # print percentage of branch coverage
        covered = 0
        for key in branch_coverage:
            if branch_coverage[key]:
                covered += 1
        print("Branch coverage: " + str(covered / len(branch_coverage) * 100) + "%")