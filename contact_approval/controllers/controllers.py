# -*- coding: utf-8 -*-
# from odoo import http


# class ContactApproval(http.Controller):
#     @http.route('/contact_approval/contact_approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_approval/contact_approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_approval.listing', {
#             'root': '/contact_approval/contact_approval',
#             'objects': http.request.env['contact_approval.contact_approval'].search([]),
#         })

#     @http.route('/contact_approval/contact_approval/objects/<model("contact_approval.contact_approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_approval.object', {
#             'object': obj
#         })

