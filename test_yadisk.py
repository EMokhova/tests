import pytest
from yandex_disk import create_folder, get_status_folder


class TestYaDisk:

    @pytest.mark.parametrize('folder, status', [('new3', 201), ('new3', 409)])
    def test_create_folder(self, folder, status):
        assert (create_folder(folder) == status)

    def test_get_status_folder(self):
        assert (get_status_folder('new3') == 'dir')
        assert (get_status_folder('new5') != 'dir')
