# -*- coding: utf-8 -*-
# from odoo import http


# class SalesRental(http.Controller):
#     @http.route('/sales_rental/sales_rental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_rental/sales_rental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_rental.listing', {
#             'root': '/sales_rental/sales_rental',
#             'objects': http.request.env['sales_rental.sales_rental'].search([]),
#         })

#     @http.route('/sales_rental/sales_rental/objects/<model("sales_rental.sales_rental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_rental.object', {
#             'object': obj
#         })

