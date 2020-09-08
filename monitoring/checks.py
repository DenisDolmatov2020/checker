import re


class Check(object):
    def do(self, response):
        return False

    def error2str(self, url, response):
        pass


class StatusCode(Check):
    status_code = None

    def __init__(self, status_code):
        self.status_code = status_code

    def do(self, response):
        return response.status_code == self.status_code

    def error2str(self, url, response):
        return 'STATUS_CODE ERROR: {}. Current: {}. Expected {}.'.format(url, response.status_code, self.status_code)


class RegEx(Check):
    regex = None

    def __init__(self, pattern, flags):
        self.regex = re.compile(pattern, flags)

    def do(self, response):
        return self.regex.match(response.content)

    def error2str(self, url, response):
        return 'REGEX ERROR: {}. Expected {}.'.format(url, self.regex.pattern)


class Contains(Check):
    strings = None
    failed = None

    def __init__(self, *args):
        self.strings = args

    def do(self, response):
        for string in self.strings:
            if string not in response.text:
                self.failed = string
                return False
        return True

    def error2str(self, url, response):
        return 'CONTAINS ERROR: {}. Expected {}.'.format(url, self.failed)


class NotContains(Check):
    strings = None
    failed = None

    def __init__(self, *args):
        self.strings = args

    def do(self, response):
        for string in self.strings:
            if string in response.text:
                self.failed = string
                return False
        return True

    def error2str(self, url, response):
        return 'NOT_CONTAINS ERROR: {}. Not expected {}.'.format(url, self.failed)
