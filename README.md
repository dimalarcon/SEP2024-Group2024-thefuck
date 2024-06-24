# Report for Assignment 1 - Group 82

## Project Information

- **Name:** TheFuck - Magnificent app which corrects your previous console command
- **URL:** https://github.com/dimalarcon/SEP2024-Group82-thefuck
- **Programming Language:** Python

## Code Metrics

- **Number of lines of code:** 547801 (54.7 KLOC)
- **Tool used to measure the number of lines of code:** lizard

![Lizard-KLOC-Screenshot-output-command](/screenshots/lizard-kloc(21-06-2024_16-39-00).png)

## Coverage Measurement

- **Existing tool used to measure the coverage:** coverage.py
- **Coverage result:** 94%

![Coverage.py-Coverage-Measurement](/screenshots/coverage-py-2(2024-06-21_17-09-11).png)
![Coverage.py-Coverage-Measurement](/screenshots/coverage-py-1(21-06-2024_17-06-39).png)

## Tasks

### Janis Roberts Rozenfelds

### Function 1: fix_command in entrypoints/fix_command.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![Function1-BeforeInstrumentation](/screenshots/janis-function1-before_instrumentation.png)

- **After instrumentation:**

![Function1-AfterInstrumentation](/screenshots/janis-function1-after_instrumentation.png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/entrypoints/test_fix_command.py**

![Function1-CoverageBeforeImprov](/screenshots/janis-function1-coverage_before_improvement.png)

- **Creating new tests to cover the function**

```python
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
```
- **Coverage after adding new tests to the corresponding test file: /tests/entrypoints/test_fix_command.py**

![Function1-CoverageAfterImprov](/screenshots/janis-function1-coverage_after_improvement.png)


### Function 2: getch in system/unix.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![Function2-BeforeInstrumentation](/screenshots/janis-function2-before_instrumentation.png)

- **After instrumentation:**

![Function2-AfterInstrumentation](/screenshots/janis-function2-after_instrumentation.png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/rules/test_yarn_help.py**

![Function2-CoverageBeforeImprov](/screenshots/janis-function2-coverage_before_improvement.png)

- **Creating new tests to cover the function**

```python
def test_getch():
    with patch('thefuck.system.sys.stdin', MagicMock()):
        # Mock termios functions used in getch()
        mock_tcgetattr = MagicMock()
        mock_tcsetattr = MagicMock()
        mock_tcgetattr.return_value = [0] * 6  # Mocking a typical return value for tcgetattr

        with patch('thefuck.system.termios.tcgetattr', mock_tcgetattr):
            with patch('thefuck.system.termios.tcsetattr', mock_tcsetattr):
                # Mock fileno() to return a valid integer
                sys.stdin.fileno = MagicMock(return_value=0)

                # Mock setraw() to bypass actual terminal setup
                tty.setraw = MagicMock()

                # Mock read() to return values for getch() calls
                sys.stdin.read = MagicMock(side_effect=['a', 'b', 'c', '', '\x1b', '\x03'])

                # Test reading multiple characters
                assert getch() == 'a'
                assert getch() == 'b'
                assert getch() == 'c'

                # Test handling of empty input
                assert getch() == ''

                # Test handling of special characters
                assert getch() == '\x1b'
                assert getch() == '\x03'

                # Ensure read(1) is called exactly once per getch() call
                assert sys.stdin.read.call_count == 6  # 3 normal chars + 1 empty + 2 special chars

                print(branch_coverage)
                
                # print percentage of branch coverage
                covered = 0
                for key in branch_coverage:
                    if branch_coverage[key]:
                        covered += 1
                print("Branch coverage: " + str(covered / len(branch_coverage) * 100) + "%")
```
- **Coverage after adding new tests to the corresponding test file: /tests/rules/test_yarn_help.py**

![Function2-CoverageAfterImprov](/screenshots/janis-function2-coverage_after_improvement.png)

