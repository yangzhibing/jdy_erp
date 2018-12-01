# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'partner'

    @api.one
    @api.depends('child_ids.is_default_add', 'child_ids.province_id', 'child_ids.city_id', 'child_ids.county_id',
                 'child_ids.town', 'child_ids.detail_address')
    # 重新定义默认联系人的 2018/11/13 杨志兵添加
    def _compute_partner_contact(self):
        '''如果业务伙伴地址中有默认联系人，则显示在业务伙伴列表上'''
        if not self.child_ids:
            return {}
        for child in self.child_ids:
            if child.is_default_add:  # 如果有默认地址取默认联系人
                self._put_info_to_partner(child)

        # 如果没有默认地址取第一个联系人的
        if not any([child.is_default_add for child in self.child_ids]):
            partners_add = self.env['partner.contact'].search(
                [('partner_id', '=', self.id)], order='id')
            child = partners_add and partners_add[0] or False
            if child:
                self._put_info_to_partner(child)

    contact = fields.Char(
        u'收货人', compute='_compute_partner_address', store=True)
