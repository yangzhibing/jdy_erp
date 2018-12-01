# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_MONEY",

    'summary': """
    """,
    'description': """
    """,

    'author': "ZNB",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'money'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/extend_money_order_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
