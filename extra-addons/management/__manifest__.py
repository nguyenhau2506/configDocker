# -*- coding: utf-8 -*-
{
    'name': "management",

    'summary': """
        test coi co gi""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale_management',
    'version': '16.0',
    'description':'icon.jpg',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True ,
    # always loaded
    'data': [
        "security/management_security.xml",
        'security/ir.model.access.csv',
        "views/manage_view.xml",
        "views/menu_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
