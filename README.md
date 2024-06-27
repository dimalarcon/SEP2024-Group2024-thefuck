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

### Luca De Nobili

### Function 1 (property): in thefuck/types.py

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

![Function1-CoverageAfterImprov](/screenshots/final_branch_coverage_script_parts.png)


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

