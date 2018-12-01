# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp

# class znberp_sell(models.Model):
#     _name = 'znberp_sell.znberp_sell'
#
# #     name = fields.Char()
# #     value = fields.Integer()
# #     value2 = fields.Float(compute="_value_pc", store=True)
# #     description = fields.Text()
# #
# #     @api.depends('value')
# #     def _value_pc(self):
# #         self.value2 = float(self.value) / 100
#



# class SellOrder(models.Model):
#     _inherit = 'sell.order'
#
#     uos_id = fields.Many2one('uom', u'辅助单位', ondelete='restrict',
#                              help=u'商品辅助单位')
#     goods_uos_qty = fields.Float(u'辅助数量',
#                             default=1,
#                             digits=dp.get_precision('Quantity'),
#                             help=u'商品的辅助数量')