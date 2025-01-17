from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ], default = 'draft')

    approver_id = fields.Many2one('res.users', string='Approved By')

    def action_approve(self):
        for record in self:
            record.state = 'approved'
            record.approver_id = self.env.user.id

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
            record.approver_id = False

    def action_reset(self):
        for record in self:
            record.state = 'draft'
            record.approver_id = False
