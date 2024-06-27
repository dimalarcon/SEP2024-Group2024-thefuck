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

### Rudolfs Altens

### Function 1: instant_mode_alias in shells/bash.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![bash.py-how_to_configure_before_instrumentation](/screenshots/how_to_configure_before_instrumentation.jpg)

- **After instrumentation:**

![bash.py-how_to_configure_after_instrumentation](/screenshots/how_to_configure_after_instrumentation.jpg)

#### 2. Coverage Improvement

- **Coverage before adding new tests to the corresponding test file: /tests/shells/test_bash.py**

![coverage_before](/screenshots/bash.py_coverage_before.jpg)


- **Creating new tests to cover the function**

![test_bash.py-Instant_mode_alias_tests](/screenshots/Instant_mode_alias_tests.png)


- **Coverage after adding new tests for intant_mode_alias function to the corresponding test file: /tests/shells/test_bash.py**

![coverage_with_instant_mode_alias_tests](/screenshots/coverage_with_instant_mode_alias_tests.png)


### Function 2: how_to_configure in shells/bash.py

#### 1. Function Instrumentation

- **Before instrumentation:**

![bash.py-how_to_configure_before_instrumentation](/screenshots/how_to_configure_before_instrumentation.jpg)


- **After instrumentation:**

![bash.py-how_to_configure_after_instrumentation](/screenshots/how_to_configure_after_instrumentation.jpg)

#### 2. Coverage Improvement

- **Coverage before adding new tests for how_to_configurte function to the corresponding test file: /tests/shells/test_bash.py**

![coverage_before](/screenshots/bash.py_coverage_before.jpg)

- **Creating new tests to cover the function**

![test_bash.py-how_to_configure_test](/screenshots/how_to_configure_test.png)

- **Coverage after adding new tests to the corresponding test file: /tests/shells/test_bash.py**

![coverage_with_how_to_configure_test](/screenshots/coverage_with_how_to_configure_test.png)


- **Coverage after adding both tests for instant_mode_alias and for how_to_configurte funcitons to the corresponding test file: /tests/shells/test_bash.py**

![bash.py_coverage_after](/screenshots/bash.py_coverage_after.jpg)


### Print Function: in shells/bash.py

- **Print funciton for branch coverage**

![print_coverage_function](/screenshots/print_coverage_function.png)

![print_coverage_result](/screenshots/print_coverage_result.png)


