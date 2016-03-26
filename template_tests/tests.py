import re
import os

from django.test import TestCase
from django.utils.text import slugify

from .utils import get_template_dirs

re_url = re.compile(r'\shref="(?P<url>(?!https?:|mailto:|\?|{|#)[^"]*)"')

class TestTemplatesMeta(type):
    def __new__(cls, name, bases, attrs):
        def generate(template):
            def fn(self):
                self.assertValidURLs(template)
            return fn

        for x in get_template_dirs():
            for root, _, templates in os.walk(x):
                for y in templates:
                    template = os.path.join(root, y)

                    attrs['test_%s' % slugify(template)] = generate(template)

        return super(TestTemplatesMeta, cls).__new__(cls, name, bases, attrs)

class TestTemplates(TestCase):
    __metaclass__ = TestTemplatesMeta

    def assertValidURLs(self, template):
        with open(template) as f:
            urls = [m.group('url') for m in re_url.finditer(f.read())]

        self.failIf(urls, "%s contains hardcoded URLs: %r" % (
            template,
            urls,
        ))
