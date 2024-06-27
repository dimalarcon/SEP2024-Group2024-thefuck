# Report for Assignment 1 - Group 82

## Project Information

- **Name:** TheFuck - Magnificent app which corrects your previous console command
- **URL:** https://github.com/dimalarcon/SEP2024-Group82-thefuck
- **Programming Language:** Python

## Code Metrics

- **Number of lines of code:** 13059 (13.0 KLOC)
- **Tool used to measure the number of lines of code:** lizard

![Lizard-KLOC-Screenshot-output-command](/screenshots/n_lines_of_code.png)

## Coverage Measurement

- **Existing tool used to measure the coverage:** coverage.py
- **Coverage result:** 94%

![Coverage.py-Coverage-Measurement](/screenshots/coverage-py-2(2024-06-21_17-09-11).png)
![Coverage.py-Coverage-Measurement](/screenshots/coverage-py-1(21-06-2024_17-06-39).png)

## Tasks

### Luca De Nobili

### Function 1 (property): script_parts in thefuck/types.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![Function1-BeforeInstrumentation](/screenshots/function_script_parts_before_instrumentation.png)

- **After instrumentation:**

![Function1-AfterInstrumentation](/screenshots/function_script_parts_after_instrumentation.png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/test_types.py**

![Function1-CoverageBeforeImprov](/screenshots/initial_branch_coverage_script_parts.png)

- **Creating new tests to cover the function**

```python
    def test_script_parts_exception(self, mocker, caplog):
        mocker.patch('thefuck.shells.shell.split_command', side_effect=Exception('Mocked exception'))
        command = Command('invalid command', 'output')
        
        with caplog.at_level('DEBUG'):
            parts = command.script_parts
            assert parts == []

        print(f"Branch coverage: {sum(branch_coverage.values())/len(branch_coverage) * 100}%\n")
```
- **Coverage after adding new tests to the corresponding test file: /tests/types.py**

![Function1-CoverageAfterImprov](/screenshots/final_branch_coverage_script_parts(fix).png)


### Function 2: get_installation_version in thefuck/utils.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![Function2-BeforeInstrumentation](/screenshots/function_get_installation_version_before_instrumentation.png)

- **After instrumentation:**

![Function2-AfterInstrumentation](/screenshots/function_get_installation_version_after_instrumentation.png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/test_utils.py**

![Function2-CoverageBeforeImprov](/screenshots/initial_branch_coverage_get_installation_version.png)

- **Creating new tests to cover the function**

```python
class TestGetInstallationVersion(unittest.TestCase):

    @patch('importlib.metadata.version', unittest.mock.MagicMock(return_value='1.2.3'))
    def test_get_installation_version_with_importlib(self):
        version = get_installation_version()
        self.assertEqual(version,'1.2.3')

    @patch('importlib.metadata.version', side_effect=ImportError)
    @patch('pkg_resources.require', return_value=[unittest.mock.MagicMock(version='4.5.6')])
    def test_get_installation_version_with_pkg_resources(self, mock_require, mock_version):
        version = get_installation_version()
        self.assertEqual(version, '4.5.6')
        print(f"Branch coverage: {sum(branch_coverage.values())/len(branch_coverage) * 100}% ")
        
```
- **Coverage after adding new tests to the corresponding test file: /tests/test_utils.py**

![Function2-CoverageAfterImprov](/screenshots/final_branch_coverage_get_installation_version.png)

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


### Function 2/3: getch and get_key in system/unix.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![Function2-BeforeInstrumentation](/screenshots/janis-function2-before_instrumentation.png)
![Function3-BeforeInstrumentation](/screenshots/janis-function3-before_instrumentation.png)

- **After instrumentation:**

![Function2-AfterInstrumentation](/screenshots/janis-function2-after_instrumentation.png)
![Function3-AfterInstrumentation](/screenshots/janis-function3-after_instrumentation.png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/rules/test_yarn_help.py**

![Function2-CoverageBeforeImprov](/screenshots/janis-function2-coverage_before_improvement.png)
![Function3-CoverageBeforeImprov](/screenshots/janis-function3-coverage_before_improvement.png)

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

                print(branch_coverage_getch)
                
                # print percentage of branch coverage
                covered = 0
                for key in branch_coverage_getch:
                    if branch_coverage_getch[key]:
                        covered += 1
                print("getch branch coverage: " + str(covered / len(branch_coverage_getch) * 100) + "%")

@pytest.fixture
def mock_getch():
    with patch('thefuck.system.unix.getch') as mock:
        yield mock

def test_get_key_ctrl_n(mock_getch):
    mock_getch.return_value = '\x0e'  # Simulate Ctrl+N
    assert get_key() == KEY_MAPPING['\x0e']

def test_get_key_ctrl_c(mock_getch):
    mock_getch.return_value = '\x03'  # Simulate Ctrl+C
    assert get_key() == KEY_MAPPING['\x03']

def test_get_key_arrow_up(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'A']  # Simulate Up arrow key
    assert get_key() == KEY_UP

def test_get_key_arrow_down(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'B']  # Simulate Down arrow key
    assert get_key() == KEY_DOWN

def test_get_key_regular_char(mock_getch):
    mock_getch.return_value = 'a'  # Simulate regular character 'a'
    assert get_key() == 'a'
    # print percentage of branch coverage
    covered = 0
    for key in branch_coverage_get_key:
        if branch_coverage_get_key[key]:
            covered += 1
    print(branch_coverage_get_key)
    print("get_key branch coverage: " + str(covered / len(branch_coverage_get_key) * 100) + "%")
```
- **Coverage after adding new tests to the corresponding test file: /tests/rules/test_yarn_help.py**
![Function2-CoverageAfterImprov](/screenshots/janis-function23-coverage_after_improvement.png)


### Dmitri Bespalii
### Function 1: get_new_command in /rules/cd_correction.py
#### 1. Function Instrumentation

- **Before instrumentation:**

![Function1-BeforeInstrumentation](/screenshots/dima-function1-before_instrumentation(2024-06-21_17-35-56).png)
    
- **After instrumentation:**

![Function1-AfterInstrumentation-1](/screenshots/dima-function1-after_instrumentation_1(2024-06-21_17-48-32).png)
![Function1-AfterInstrumentation-2](/screenshots/dima-function1-after_instrumentation_2(2024-06-21_17-53-14).png)

- **Write all information about conditional branches to console:**

![Function1-WriteInformation](/screenshots/dima-function1-write_info_branch_coverage(2024-06-21_18-14-39).png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/rules/test_cd_correction.py**

![Function1-CoverageBeforeImprov](/screenshots/dima-function1-coverage_before_improvement(2024-06-21_19-07-47).png)

- **Creating new tests to cover the function**

![Function1-NewTestsAdded](/screenshots/dima-function1-newtestadded(2024-06-21_18-43-27).png)

- **Coverage after adding new tests to the corresponding test file: /tests/rules/test_cd_correction.py**

![Function-CoverageAfterImprov](/screenshots/dima-function1-coverage_after_improv(2024-06-21_19-11-59).png)


### Function 2: archlinux_env in /specific/archlinux.py
#### 1. Function Instrumentation

- **Before instrumentation:**

![Function2-BeforeInstrumentation](/screenshots/dima-function2-before_instrumentation(2024-06-23_20-43-17).png)

- **After instrumentation:**

![Function2-AfterInstrumentation-1](/screenshots/dima-function2-after_instrumentation_1(2024-06-23_20-58-53).png)
![Function2-AfterInstrumentation-2](/screenshots/dima-function2-after_instrumentation_2(2024-06-23_21-03-15).png)

- **Write all information about conditional branches to console:**

![Function2-WriteInformation](/screenshots/dima-function2-write_info_branch_coverage(2024-06-23_21-07-55).png)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/specific/test_archlinux.py**

![Function2-CoverageBeforeImprov](/screenshots/dima-function2-coverage_before_improvement(2024-06-23_21-12-26).png)

- **Creating new tests to cover the function**

![Function2-NewTestsAdded](/screenshots/dima-function2-newtestadded(2024-06-23_21-14-31).png)

- **Coverage after adding new tests to the corresponding test file: /tests/specific/test_archlinux.py**

![Function2-CoverageAfterImprov](/screenshots/dima-function2-coverage_after_improv(2024-06-23_21-17-22).png)
    
