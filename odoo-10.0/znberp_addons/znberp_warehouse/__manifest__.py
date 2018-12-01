# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_WAREHOUSE",

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
    'depends': ['base', 'warehouse'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/extend_production_view.xml',
        'views/extend_warehouse_view.xml',
        'views/qc_result_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
