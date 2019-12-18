"""
test_kubo_demo
Learn how to use package development tools with Hanbo using Kubo model as an example.
"""

# Add imports here
from .test_kubo_demo import Kubo

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
