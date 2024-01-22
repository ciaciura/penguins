"""
This module contains an example test.

Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py. They are simply functions
named ``test_*`` which test a unit of logic.

To run the tests, run ``kedro test`` from the project root directory.
"""

from pathlib import Path

import pytest
from kedro.config import OmegaConfigLoader
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager
from kedro.framework.project import settings


@pytest.fixture
def config_loader():
    """Load the config file for tests"""
    return OmegaConfigLoader(conf_source=str(Path.cwd() / settings.CONF_SOURCE))


@pytest.fixture
def project_context(cfg_loader):
    """Introduce project context so tests behave like in a real project."""
    return KedroContext(
        package_name="penguins",
        project_path=Path.cwd(),
        config_loader=cfg_loader,
        hook_manager=_create_hook_manager(),
    )


# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality
class TestProjectContext:
    """Example test for project context"""
    def test_project_path(self, proj_context):
        """Example test for project path"""
        assert proj_context.project_path == Path.cwd()
    def test_project_name(self, proj_context):
        """Example test for project name"""
        assert proj_context.project_name == "penguins"
