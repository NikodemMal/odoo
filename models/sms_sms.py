from odoo import models, fields, api
from datetime import datetime

class SmsSms(models.Model):
    _inherit = 'sms.sms'

    scheduled_date = fields.Datetime(
        string="Scheduled Send Date",
        help="The date and time when the SMS will be sent. The SMS will only be sent after this date is reached."
    )

    @api.model
    def _process_queue(self):
        sms_to_send = self.search([('scheduled_date', '<=', datetime.now()), ('state', '=', 'outgoing')])

        for sms in sms_to_send:
            try:
                super(SmsSms, sms).send()

            except Exception as e:
                sms.write({'state': 'error'})


    def send(self):

        for sms in self:
            sms.write({'state': 'outgoing'})
