# -*- coding: utf-8 -*-
{
    'name': "Statement Balance",

    'summary': """
        Statement Balance""",

    'description': """
        Add new field to get sum of Statement Lines.
    """,

    'author': "Bola Ayman",

    'category': 'Accounting/Accounting',
    
    'version': '15.0.0.1',
    
    'license": "AGPL-3',

    'depends': ['base', 'account'],

    'data': [
        'views/account_bank_statement_view.xml',
    ],

}
