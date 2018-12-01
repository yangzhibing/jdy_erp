# -*- coding: utf-8 -*-
from odoo import http

# class Core(http.Controller):
#     @http.route('/core/core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/core/core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('core.listing', {
#             'root': '/core/core',
#             'objects': http.request.env['core.core'].search([]),
#         })

#     @http.route('/core/core/objects/<model("core.core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('core.object', {
#             'object': obj
#         })