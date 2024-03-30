# -*- coding: utf-8 -*-
{
    'name': "Statement Balance",

    'summary': """
        Statement Balance""",

    'description': """
        Add new field to get sum of statement lines.
    """,

    'author': "Bola Ayman",

    'category': 'Accounting/Accounting',
    
    'version': '14.0.0.1',

    'depends': ['base', 'account'],

    'data': [
        'views/account_bank_statement_view.xml',
    ],

    'images': ['static/description/logo.png'],

    'live_test_url': 'static/description/logo.png',

}
