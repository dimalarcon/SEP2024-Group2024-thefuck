import pytest
from unittest.mock import patch, MagicMock
from thefuck.specific.archlinux import archlinux_env, branch_coverage

@pytest.mark.parametrize('which_mock, expected_result', [
    (MagicMock(return_value='yay'), ('yay', 'yay')),         
    (MagicMock(return_value='pikaur'), ('pikaur', 'yay')),   
    (MagicMock(return_value='yaourt'), ('yaourt', 'yay')),   
    (MagicMock(return_value=None), (False, None)),           
])
def test_archlinux_env(which_mock, expected_result):
    with patch('thefuck.specific.archlinux.utils.which', which_mock):
        print(branch_coverage)
        assert archlinux_env() == expected_result
        print(branch_coverage)