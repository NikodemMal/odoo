from odoo import models, fields, api

class StockPickingWizard(models.TransientModel):
    _name = 'stock.picking.wizard'
    _description = 'Wizard for Confirming Email Sending for Overdue Stock Picking'

    message = fields.Text(string="Message", readonly=True, default="This picking is overdue by 2 weeks. Do you want to send an email notification?")

    def action_send_email(self):
        # Logika wysyłania e-maila
        picking = self.env['stock.picking'].browse(self._context.get('active_id'))
        if picking:
            template = self.env.ref('stock_picking_wizard.email_template_stock_picking')
            template.send_mail(picking.id, force_send=True)
        return {'type': 'ir.actions.act_window_close'}
