import pytest
import sys
import tty
from unittest.mock import patch, MagicMock
from thefuck.rules.yarn_help import match, get_new_command
from thefuck.types import Command
from thefuck.system.unix import open_command, getch, branch_coverage_getch, get_key, branch_coverage_get_key
from thefuck.const import KEY_MAPPING, KEY_UP, KEY_DOWN


output_clean = '''

  Usage: yarn [command] [flags]

  Options:

    -h, --help                      output usage information
    -V, --version                   output the version number
    --verbose                       output verbose messages on internal operations
    --offline                       trigger an error if any required dependencies are not available in local cache
    --prefer-offline                use network only if dependencies are not available in local cache
    --strict-semver                 
    --json                          
    --ignore-scripts                don't run lifecycle scripts
    --har                           save HAR output of network traffic
    --ignore-platform               ignore platform checks
    --ignore-engines                ignore engines check
    --ignore-optional               ignore optional dependencies
    --force                         ignore all caches
    --no-bin-links                  don't generate bin links when setting up packages
    --flat                          only allow one version of a package
    --prod, --production [prod]     
    --no-lockfile                   don't read or generate a lockfile
    --pure-lockfile                 don't generate a lockfile
    --frozen-lockfile               don't generate a lockfile and fail if an update is needed
    --link-duplicates               create hardlinks to the repeated modules in node_modules
    --global-folder <path>          
    --modules-folder <path>         rather than installing modules into the node_modules folder relative to the cwd, output them here
    --cache-folder <path>           specify a custom folder to store the yarn cache
    --mutex <type>[:specifier]      use a mutex to ensure only one yarn instance is executing
    --no-emoji                      disable emoji in output
    --proxy <host>                  
    --https-proxy <host>            
    --no-progress                   disable progress bar
    --network-concurrency <number>  maximum number of concurrent network requests

  Visit https://yarnpkg.com/en/docs/cli/clean for documentation about this command.
'''  # noqa


@pytest.mark.parametrize('command', [
    Command('yarn help clean', output_clean)])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, url', [
    (Command('yarn help clean', output_clean),
     'https://yarnpkg.com/en/docs/cli/clean')])
def test_get_new_command(command, url):
    assert get_new_command(command) == open_command(url)

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