from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'product.template'

    is_rent = fields.Boolean('Can be Rent')
    count_rent = fields.Integer(string = 'Count Rent', compute = '_compute_count_rent')

    @api.depends('is_rent')
    def _compute_count_rent(self):
        for rent in self:
            rent.count_rent = self.env['product.template'].search_count([('is_rent', '=', True)])

    def action_open_list_rent(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rented Products',
            'view_mode': 'kanban',
            'res_model': 'product.template',
            'views': [(self.env.ref('product.product_template_kanban_view').id, 'kanban')],
            'domain': ['|', ('is_rent', '=', True), ('is_rent', '=', 1)],
            'context': {'default_is_rent': True},
        }
