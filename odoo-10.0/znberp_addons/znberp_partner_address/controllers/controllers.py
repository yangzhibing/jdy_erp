# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpPartnerAddress(http.Controller):
#     @http.route('/znberp_partner_address/znberp_partner_address/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_partner_address/znberp_partner_address/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_partner_address.listing', {
#             'root': '/znberp_partner_address/znberp_partner_address',
#             'objects': http.request.env['znberp_partner_address.znberp_partner_address'].search([]),
#         })

#     @http.route('/znberp_partner_address/znberp_partner_address/objects/<model("znberp_partner_address.znberp_partner_address"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_partner_address.object', {
#             'object': obj
#         })