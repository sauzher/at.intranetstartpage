# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import at.intranetstartpage


class AtIntranetstartpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=at.intranetstartpage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'at.intranetstartpage:default')


AT_INTRANETSTARTPAGE_FIXTURE = AtIntranetstartpageLayer()


AT_INTRANETSTARTPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AT_INTRANETSTARTPAGE_FIXTURE,),
    name='AtIntranetstartpageLayer:IntegrationTesting'
)


AT_INTRANETSTARTPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AT_INTRANETSTARTPAGE_FIXTURE,),
    name='AtIntranetstartpageLayer:FunctionalTesting'
)


AT_INTRANETSTARTPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        AT_INTRANETSTARTPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AtIntranetstartpageLayer:AcceptanceTesting'
)
