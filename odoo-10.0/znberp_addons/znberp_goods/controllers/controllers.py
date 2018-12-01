# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpGoods(http.Controller):
#     @http.route('/znberp_goods/znberp_goods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_goods/znberp_goods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_goods.listing', {
#             'root': '/znberp_goods/znberp_goods',
#             'objects': http.request.env['znberp_goods.znberp_goods'].search([]),
#         })

#     @http.route('/znberp_goods/znberp_goods/objects/<model("znberp_goods.znberp_goods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_goods.object', {
#             'object': obj
#         })