from datetime import datetime, timedelta
from odoo import models, fields, api, _
class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPicking, self).button_validate()

        today = fields.Date.context_today(self)
        today_datetime = datetime.combine(today, datetime.min.time())
        for picking in self:
            if picking.scheduled_date:

                scheduled_date_datetime = datetime.combine(picking.scheduled_date, datetime.min.time())
                if scheduled_date_datetime < (today_datetime - timedelta(weeks=2)):

                    return {
                        'name': _('Send Email'),
                        'type': 'ir.actions.act_window',
                        'res_model': 'mail.compose.message',
                        'view_mode': 'form',
                        'view_id': self.env.ref('mail.email_compose_message_wizard_form').id,
                        'target': 'new',
                        'context': {
                            'default_model': 'stock.picking',
                            'default_res_ids': [self.id],
                            'default_subject': _('Overdue Stock Picking Notification'),
                        },
                    }

        return res
