{
    'name': 'Stock Picking Popup',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Displays a popup for stock pickings that are overdue by 2 weeks.',
    'depends': ['stock', 'mail'],
    'data': [
        'views/stock_picking_views.xml',
        'data/ir_config_parameter.xml',
        'views/email_template.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
