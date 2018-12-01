# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpMoney(http.Controller):
#     @http.route('/znberp_money/znberp_money/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_money/znberp_money/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_money.listing', {
#             'root': '/znberp_money/znberp_money',
#             'objects': http.request.env['znberp_money.znberp_money'].search([]),
#         })

#     @http.route('/znberp_money/znberp_money/objects/<model("znberp_money.znberp_money"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_money.object', {
#             'object': obj
#         })