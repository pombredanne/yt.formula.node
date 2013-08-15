"""
Tests for the node formula
"""
import tempfile
import shutil

from sprinter.testtools import create_mock_environment

source_config = """
[update]
formula = yt.formula.node
version = 0.10.16
packages =
  grunt-cli@0.3.1
"""

target_config = """
[install]
formula = yt.formula.node
version = 0.10.16
packages =
  grunt-cli@~0.4.1

[update]
formula = yt.formula.node
version = 0.10.16
packages =
  grunt-cli@0.4.2
"""


class NodeFormulaTests(object):
    """
    Run node.js formula tests
    """

    def setup(self):
        self.temp_dir = tempfile.mkdtemp()
        self.environment = create_mock_environment(source_config=source_config,
                                                   target_config=target_config,
                                                   mock_directory=False,
                                                   root=self.temp_dir)

    def teardown(self):
        shutil.rmtree(self.temp_dir)

    def test_install(self):
        self.environment.run_feature("install", 'sync')
        assert 