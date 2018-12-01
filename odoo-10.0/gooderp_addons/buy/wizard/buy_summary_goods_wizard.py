# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api
from odoo.exceptions import UserError


class BuySummaryGoodsWizard(models.TransientModel):
    _name = 'buy.summary.goods.wizard'
    _description = u'采购汇总表（按商品）向导'

    @api.model
    def _default_date_start(self):
        return self.env.user.company_id.start_date

    @api.model
    def _default_date_end(self):
        return date.today()

    date_start = fields.Date(u'开始日期', default=_default_date_start,
                             help=u'报表汇总的开始日期，默认为公司启用日期')
    date_end = fields.Date(u'结束日期', default=_default_date_end,
                           help=u'报表汇总的结束日期，默认为当前日期')
    partner_id = fields.Many2one('partner', u'供应商',
                                 help=u'只统计选定的供应商')
    goods_id = fields.Many2one('goods', u'商品',
                               help=u'只统计选定的商品')
    goods_categ_id = fields.Many2one('core.category', u'商品类别',
                                     help=u'只统计选定的商品类别')
    warehouse_dest_id = fields.Many2one('warehouse', u'仓库',
                                        help=u'只统计选定的仓库')
    company_id = fields.Many2one(
        'res.company',
        string=u'公司',
        change_default=True,
        default=lambda self: self.env['res.company']._company_default_get())

    @api.multi
    def button_ok(self):
        self.ensure_one()
        if self.date_end < self.date_start:
            raise UserError(u'开始日期不能大于结束日期！')

        read_field = ['date_start', 'date_end', 'partner_id',
                      'goods_id', 'goods_categ_id', 'warehouse_dest_id']
        return {
            'name': u'采购汇总表（按商品）',
            'view_mode': 'tree',
            'res_model': 'buy.summary.goods',
            'type': 'ir.actions.act_window',
            'context': self.read(read_field)[0],
            'limit': 65535,
        }
