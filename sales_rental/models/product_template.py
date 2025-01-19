from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_rent = fields.Boolean('Can be Rent')
    count_rent = fields.Integer(string = 'Count Rent', compute = '_compute_count_rent')

    @api.depends('is_rent')
    def _compute_count_rent(self):
        for rent in self:
            rent.count_rent = self.env['product.template'].search_count([('is_rent', '=', True)])

    def action_open_sale_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'views': [
                (self.env.ref('sale.view_order_tree').id, 'tree'),
                (self.env.ref('sale.view_order_form').id, 'form'),
            ],
            # 'domain': [],
            # 'context': {'default_is_rent': True},
        }
