{
    'name': 'Stock Picking Popup',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Displays a popup for stock pickings that are overdue by 2 weeks.',
    'depends': ['stock', 'mail'],
    'data': [
        'data/ir_config_parameter.xml',
        'data/email_template.xml',
        'security/ir.model.access.csv',
        'i18n/pl_PL.csv',
    ],
    'installable': True,
    'application': True,
}
