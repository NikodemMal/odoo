{
    'name': 'SMS Scheduler Delay',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Opóźnienie wysyłki SMS w Odoo',
    'description': """
        Aplikacja do opóźniania wysyłki SMS w Odoo. SMS będzie wysyłany w określonym czasie (scheduled_date).
    """,

    'depends': ['base','sms'],  # Zależność od aplikacji SMS

    'data': [
        'views/sms_sms_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}