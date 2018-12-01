# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpBuy(http.Controller):
#     @http.route('/znberp_buy/znberp_buy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_buy/znberp_buy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_buy.listing', {
#             'root': '/znberp_buy/znberp_buy',
#             'objects': http.request.env['znberp_buy.znberp_buy'].search([]),
#         })

#     @http.route('/znberp_buy/znberp_buy/objects/<model("znberp_buy.znberp_buy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_buy.object', {
#             'object': obj
#         })