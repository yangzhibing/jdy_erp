# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_GOODS",

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
    'depends': ['base', 'goods'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
