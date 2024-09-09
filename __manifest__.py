{
    'name': 'SMS Scheduler Delay',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'SMS sending delay in Odoo',
    'description': """
        Application for delaying SMS sending in Odoo. The SMS will be sent at a specified time (scheduled_date).
    """,
    'author': 'Your Name',
    'depends': ['base','sms'],

    'data': [
        'views/sms_sms_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'translation': ['i18n/pl_PL.csv'],
}