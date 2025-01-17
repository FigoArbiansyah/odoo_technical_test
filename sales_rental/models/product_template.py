from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'product.template'

    is_rent = fields.Boolean('Can be Rent')
    count_rent = fields.Integer(string = 'Count Rent', compute = '_compute_count_rent')

    @api.depends('is_rent')
    def _compute_count_rent(self):
        for rent in self:
            count = 0
            for record in self:
                if record.is_rent:
                    count += 1
            rent.count_rent = count
            # rent.count_rent = sum(1 for record in self if record.is_rent)
