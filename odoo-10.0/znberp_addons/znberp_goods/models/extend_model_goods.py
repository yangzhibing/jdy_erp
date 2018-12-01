# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Goods(models.Model):
    _inherit = 'goods'

    price = fields.Float(u'单价')
