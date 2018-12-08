# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class SellOrder(models.Model):
    _inherit = "sell.order"


class SellOrderLine(models.Model):
    _inherit = "sell.order.line"

    @api.one
    @api.depends('goods_id')
    def _compute_uom_uos(self):
        if self.goods_id:
            self.uom_id = self.goods_id.uom_id
            self.uos_id = self.goods_id.uos_id

    @api.onchange('quantity')
    def _change_uos_qty(self):
        if self.goods_id and self.quantity:
            self.uos_qty = self.quantity / self.goods_id.conversion
        else:
            self.uos_qty = 0

    @api.onchange('uos_qty')
    def _change_quantity(self):
        if self.goods_id and self.uos_qty:
            self.quantity = self.uos_qty * self.goods_id.conversion
        else:
            self.quantity = 0

    # @api.one
    # def _inverse_quantity(self):
    #     self.quantity = self.uos_qty * self.goods_id.conversion

    uos_id = fields.Many2one('uom', string=u'辅助单位', ondelete='restrict', compute=_compute_uom_uos,
                             readonly=True, help=u'商品的辅助单位', store=True)

    quantity = fields.Float(u'数量',
                            default=1,
                            required=True,
                            digits=dp.get_precision('Quantity'),
                            store=True,
                            help=u'下单数量')

    uos_qty = fields.Float(u'辅助数量',
                           digits=dp.get_precision('Quantity'),
                           # compute=_get_uos_qty,
                           # inverse=_inverse_quantity,
                           store=True,
                           help=u'辅助数量')
