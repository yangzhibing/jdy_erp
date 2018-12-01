# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpWarehouse(http.Controller):
#     @http.route('/znberp_warehouse/znberp_warehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_warehouse/znberp_warehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_warehouse.listing', {
#             'root': '/znberp_warehouse/znberp_warehouse',
#             'objects': http.request.env['znberp_warehouse.znberp_warehouse'].search([]),
#         })

#     @http.route('/znberp_warehouse/znberp_warehouse/objects/<model("znberp_warehouse.znberp_warehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_warehouse.object', {
#             'object': obj
#         })