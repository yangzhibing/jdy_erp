# -*- coding: utf-8 -*-
{
    'name': "ZNBERP_UUC",

    'summary': """
        ZNBERP 统一更新解决方案""",

    'description': """
        升级定向开发过程中的全部模块
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['base',
                'znberp_core',
                'znberp_buy',
                'znberp_sell',
                'znberp_goods',
                'znberp_money',
                'znberp_warehouse',
                'web_responsive',
                'fixed_header',
                ],

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
