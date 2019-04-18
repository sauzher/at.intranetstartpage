# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class StartPageView(BrowserView):

    template = ViewPageTemplateFile('templates/startpage.pt')

    def __call__(self):
        """
        """
        return self.template()
