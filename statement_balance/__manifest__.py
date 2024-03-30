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

    'license': 'AGPL-3',

    'depends': ['base', 'account'],

    'data': [
        'views/account_bank_statement_view.xml',
    ],

    # 'images': ['static/description/icon.png'],

    'live_test_url': 'https://www.youtube.com/watch?v=SpFJmHVyMKg',

}
