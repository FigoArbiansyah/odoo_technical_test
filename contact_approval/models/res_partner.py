from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ], default = 'draft')

    approver_id = fields.Many2one('res.users', string='Approved By')
