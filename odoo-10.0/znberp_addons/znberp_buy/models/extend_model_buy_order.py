# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_compare, float_is_zero
from datetime import datetime
import odoo.addons.decimal_precision as dp


class BuyOrder(models.Model):
    _inherit = "buy.order"

    # "供应商订单号"改为："合同编号"
    ref = fields.Char(u'合同编号')

    def _get_vals(self):
        '''返回创建 money_order 时所需数据'''
        flag = (self.type == 'buy' and 1 or -1)  # 用来标志入库或退货
        amount = flag * self.amount
        this_reconcile = flag * self.prepayment
        money_lines = [{
            'bank_id': self.bank_account_id.id,
            'amount': this_reconcile,
        }]
        return {
            'partner_id': self.partner_id.id,
            # 2018年6月13号 张宁波——添加
            'bank_user_name': self.partner_id.bank_user_name,
            'bank_name': self.partner_id.bank_name,
            'bank_num': self.partner_id.bank_num,
            'date': fields.Date.context_today(self),
            'line_ids':
                [(0, 0, line) for line in money_lines],
            'amount': amount,
            'reconciled': this_reconcile,
            'to_reconcile': amount,
            'state': 'draft',
            'origin_name': self.name,
            'buy_id': self.id,
        }


class Payment(models.Model):
    _inherit = "payment.plan"

    @api.one
    def request_payment(self):
        categ = self.env.ref('money.core_category_purchase')
        if not float_is_zero(self.amount_money, 2):
            source_id = self.env['money.invoice'].create({
                'name': self.buy_id.name,
                'partner_id': self.buy_id.partner_id.id,
                'category_id': categ.id,
                'date': fields.Date.context_today(self),
                'amount': self.amount_money,
                'reconciled': 0,
                'to_reconcile': self.amount_money,
                'date_due': fields.Date.context_today(self),
                'state': 'draft',
            })
            self.with_context(type='pay').env["money.order"].create({
                'partner_id': self.buy_id.partner_id.id,
                # 2018年6月13号 张宁波——添加
                'bank_user_name': self.buy_id.partner_id.bank_user_name,
                'bank_name': self.buy_id.partner_id.bank_name,
                'bank_num': self.buy_id.partner_id.bank_num,
                'date': fields.Date.context_today(self),
                'source_ids':
                    [(0, 0, {'name': source_id.id,
                             'category_id': categ.id,
                             'date': source_id.date,
                             'amount': self.amount_money,
                             'reconciled': 0.0,
                             'to_reconcile': self.amount_money,
                             'this_reconcile': self.amount_money})],
                'type': 'pay',
                'amount': self.amount_money,
                'reconciled': 0,
                'to_reconcile': self.amount_money,
                'state': 'draft',
                'buy_id': self.buy_id.id,
            })
        self.date_application = datetime.now()

class BuyOrderLine(models.Model):
    _inherit = "buy.order.line"

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

