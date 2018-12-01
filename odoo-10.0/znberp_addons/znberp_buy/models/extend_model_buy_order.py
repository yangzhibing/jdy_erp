# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_compare, float_is_zero
from datetime import datetime


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



