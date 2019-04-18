# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from at.intranetstartpage.testing import AT_INTRANETSTARTPAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that at.intranetstartpage is properly installed."""

    layer = AT_INTRANETSTARTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if at.intranetstartpage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'at.intranetstartpage'))

    def test_browserlayer(self):
        """Test that IAtIntranetstartpageLayer is registered."""
        from at.intranetstartpage.interfaces import (
            IAtIntranetstartpageLayer)
        from plone.browserlayer import utils
        self.assertIn(IAtIntranetstartpageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = AT_INTRANETSTARTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['at.intranetstartpage'])

    def test_product_uninstalled(self):
        """Test if at.intranetstartpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'at.intranetstartpage'))

    def test_browserlayer_removed(self):
        """Test that IAtIntranetstartpageLayer is removed."""
        from at.intranetstartpage.interfaces import \
            IAtIntranetstartpageLayer
        from plone.browserlayer import utils
        self.assertNotIn(IAtIntranetstartpageLayer, utils.registered_layers())
