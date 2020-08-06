import uninstall
from uninstall import is_empty_dir


class TestUninstall:
    def test_uninstall(self):  # tests to see if any files are left after uninstall
        uninstall()
        path = r"AppData\Local\autojump\bin"
        result = is_empty_dir(path)
        assert result, True

    if __name__ == '__main__':
        test_uninstall()
