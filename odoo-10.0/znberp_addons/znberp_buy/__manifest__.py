# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_BUY",

    'summary': """
    """,
    'description': """
    """,

    'author': "ZNB",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'buy'],

    'application': False,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/extend_buy_order_view.xml',
        'views/extend_buy_menu.xml',
        'views/extend_buy_receipt_view.xml',
        'views/extend_vendor_goods_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
