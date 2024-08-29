from odoo import models, fields, api
from datetime import datetime

class SmsSms(models.Model):
    _inherit = 'sms.sms'

    scheduled_date = fields.Datetime(
        string="Scheduled Send Date",
        help="Data i czas wysyłki SMS. SMS zostanie wysłany dopiero po osiągnięciu tej daty."
    )

    @api.model
    def _process_queue(self):
        sms_to_send = self.search([('scheduled_date', '<=', datetime.now()), ('state', '=', 'outgoing')])

        for sms in sms_to_send:
            # Wyślij SMS jeśli data jest odpowiednia
            sms.delayed_sending()

    def send(self):

        for sms in self:
            sms.write({'state': 'outgoing'})

    def delayed_sending(self):
        for sms in self:
            try:
                super(SmsSms, sms).send()

            except Exception as e:
                sms.write({'state': 'error'})
                print("Blad sms")
