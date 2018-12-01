# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_SELL",

    'summary': """
       """,
    'description': """
       """,

    'author': "ZNB",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sell'],

    'application': False,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/extend_sell_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}