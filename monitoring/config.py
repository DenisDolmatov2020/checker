from monitoring.checks import *

DIR = './monitoring/logs'

EMAILS = []
# EMAILS = ['email_address']

CHECKS = {
    'https://example.ru': [
        StatusCode(200),
        Contains('Some info'),
        Contains('<!-- Yandex.Metrika counter -->'),
        NotContains('id_username', 'id_password')
    ],
    'https://url-test.ru': [
        StatusCode(200),
        Contains('id_username', 'id_password')
    ],
    # '': [
    #     StatusCode(401)
    # ]
}
