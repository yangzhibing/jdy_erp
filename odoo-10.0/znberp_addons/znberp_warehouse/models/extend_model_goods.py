# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Goods(models.Model):
    _inherit = 'goods'

    # net_weight_uom = fields.Many2one('uom', string=u'净重单位' )
