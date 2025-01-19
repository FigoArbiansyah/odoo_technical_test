from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_rental_order = fields.Boolean()
    rental_start_date = fields.Datetime('Rental Start Date')
    rental_return_date = fields.Datetime('Rental Return Date')
    duration_days = fields.Integer(string = 'Duration Days', compute = '_compute_duration_days')
    rental_status = fields.Selection([
      ('draft', 'Draft'),
      ('reserved', 'Reserved'),
      ('returned', 'Returned'),
      ('cancelled', 'Cancelled'),
    ], default = 'draft', string='Rental Status')

    @api.depends('rental_start_date', 'rental_return_date')
    def _compute_duration_days(self):
        for rent in self:
            if rent.rental_start_date and rent.rental_return_date:
                duration = rent.rental_return_date - rent.rental_start_date
                rent.duration_days = max(duration.days, 0)  # Agar tidak mendapatkan negatif
            else:
                rent.duration_days = 0

    @api.onchange('rental_return_date')
    def _onchange_rental_return_date(self):
        isPriorThanStartDate = self.rental_return_date >= self.rental_start_date
        if not isPriorThanStartDate:
            self.rental_return_date = False
            return  {"warning": {"title": _("Warning"), "message": _("Return date must higher than start date")}}

