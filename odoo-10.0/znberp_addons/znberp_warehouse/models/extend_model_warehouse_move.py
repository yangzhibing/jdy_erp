# -*- coding: utf-8 -*-
from odoo import models, fields, api


class WhMove(models.Model):
    _inherit = 'wh.move'

    qc_result = fields.One2many('qc.result.more', 'wh_move_id',
                                string=u'质检报告',
                                help=u'质检报告明细行')


class QcResultMore(models.Model):
    _name = 'qc.result.more'
    _description = u'质检报告'

    wh_move_id = fields.Many2one('wh.move', string=u'移库单',
                                 help=u'质检报告对应的库存移动单据')
    name = fields.Char(u'编号')
    introduction = fields.Char(u'质检名称')
    qc_result_more = fields.Binary(u'质检报告',
                                   help=u'点击上传质检报告')


