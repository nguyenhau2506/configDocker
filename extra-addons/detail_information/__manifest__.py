# -*- coding: utf-8 -*-
{
    'name': "detail_information",

    'summary': """
        Thông tin chi tiết các khách hàng """,

    'description': """
        Thông tin cụ thể khách hàng để làm việc
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/detail_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application":False
}
