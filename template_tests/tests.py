import re
import os

from django.test import TestCase

from .utils import get_template_dirs

re_url = re.compile(r'\shref="(?P<url>(?!https?:|mailto:|\?|{|#)[^"]*)"')

class TestTemplates(TestCase):
    def assertValidURLs(self, filename):
        with open(filename) as f:
            urls = [m.group('url') for m in re_url.finditer(f.read())]

        self.failIf(urls, "%s contains hardcoded URLs: %r" % (
            filename,
            urls,
        ))

    idx = 0
    for x in get_template_dirs():
        for root, _, filenames in os.walk(x):
            for y in filenames:
                def wrapper(self, filename=os.path.join(root, y)):
                    self.assertValidURLs(filename)
                idx += 1
                locals()['test_template_idx_%04d' % idx] = wrapper
