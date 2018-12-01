# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpSell(http.Controller):
#     @http.route('/znberp_sell/znberp_sell/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_sell/znberp_sell/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_sell.listing', {
#             'root': '/znberp_sell/znberp_sell',
#             'objects': http.request.env['znberp_sell.znberp_sell'].search([]),
#         })

#     @http.route('/znberp_sell/znberp_sell/objects/<model("znberp_sell.znberp_sell"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_sell.object', {
#             'object': obj
#         })