import mock
import pytest


class TestSettings:
    package_name = 'risclog.zestreleaser.keybase'


@pytest.fixture(autouse=True)
def settings():
    patcher = mock.patch(
        'risclog.zestreleaser.keybase.config.Settings', side_effect=TestSettings
    )
    patcher.start()
    yield patcher
    patcher.stop()
