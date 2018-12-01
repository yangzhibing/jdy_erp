# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MoneyOrder(models.Model):
    _inherit = 'money.order'

    bank_user_name = fields.Char(u'户名',
                                 readonly=True,
                                 states={'draft': [('readonly', False)]},
                                 help=u'户名取自业务伙伴，可修改')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        对partner修改的监控当 partner 修改时，就对 页面相对应的字段进行修改（bank_name，bank_num，source_ids）
        :return:
        """
        if not self.partner_id:
            return {}

        source_lines = []
        self.bank_user_name = self.partner_id.bank_user_name
        self.bank_name = self.partner_id.bank_name
        self.bank_num = self.partner_id.bank_num

        for invoice in self.env['money.invoice'].search(self._get_invoice_search_list()):
            source_lines.append(self._get_source_line(invoice))
        if source_lines:
            self.source_ids = source_lines



