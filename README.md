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

    Dmitri Bespalii
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


### Function 2: archlinux_env in /specific/test_archlinux.py
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

