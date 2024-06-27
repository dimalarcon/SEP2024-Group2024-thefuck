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

