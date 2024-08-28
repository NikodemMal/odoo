from datetime import datetime, timedelta
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPicking, self).button_validate()

        today = fields.Date.context_today(self)
        today_datetime = datetime.combine(today, datetime.min.time())
        for picking in self:
            if picking.scheduled_date:
                # Konwertuj scheduled_date do datetime
                scheduled_date_datetime = datetime.combine(picking.scheduled_date, datetime.min.time())
                if scheduled_date_datetime < (today_datetime - timedelta(weeks=2)):
                    # return {
                    #     'name': 'Overdue Picking Confirmation',
                    #     'type': 'ir.actions.act_window',
                    #     'res_model': 'stock.picking.wizard',
                    #     'view_mode': 'form',
                    #     'view_id': self.env.ref('stock_picking_wizard.view_stock_picking_wizard').id,
                    #     'target': 'new',
                    #     'context': {'active_id': picking.id},
                    # }

                    return {
                        'name': 'Send Email',
                        'type': 'ir.actions.act_window',
                        'res_model': 'mail.compose.message',
                        'view_mode': 'form',
                        'view_id': self.env.ref('mail.email_compose_message_wizard_form').id,
                        'target': 'new',
                        'context': {
                            'default_model': 'stock.picking',
                            'default_res_ids': [self.id],  # Zaktualizowany parametr (jako lista)
                            'default_subject': 'Overdue Stock Picking Notification',
                        },
                    }

                # gotowy wizard mail compose
        print("koniec")
        return res
