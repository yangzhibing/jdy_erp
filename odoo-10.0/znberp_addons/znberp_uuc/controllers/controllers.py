# -*- coding: utf-8 -*-
from odoo import http

# class ZnberpUuc(http.Controller):
#     @http.route('/znberp_uuc/znberp_uuc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/znberp_uuc/znberp_uuc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('znberp_uuc.listing', {
#             'root': '/znberp_uuc/znberp_uuc',
#             'objects': http.request.env['znberp_uuc.znberp_uuc'].search([]),
#         })

#     @http.route('/znberp_uuc/znberp_uuc/objects/<model("znberp_uuc.znberp_uuc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('znberp_uuc.object', {
#             'object': obj
#         })