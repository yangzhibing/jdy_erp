# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'partner'

    # 添加字段：“生产商”
    main_producer = fields.Char(u'生产商')

    # 添加字段：“收货人”
    main_producer = fields.Char(u'生产商')

    # 开户行上面加上一行：‘户名’
    bank_user_name = fields.Char(u'户名')

    # 字段“税务登记号”修改为“统一社会信用代码”
    tax_num = fields.Char(u'统一社会信用代码')

    # 标签修改:代理品牌
    tag_ids = fields.Many2many('core.value',
                               ondelete='restrict',
                               string=u'代理品牌',
                               domain=[('type', '=', 'partner_tag')],
                               context={'type': 'partner_tag'})

    # 企业资质文件形式图片格式，PDF, 及其他常规文档均可支持上传，可支持多张上传，支持压缩包。
    partner_qualification_lines = fields.One2many('partner.qualification.line', 'partner_id',
                                                  string=u'企业资质',
                                                  help=u'企业资质明细行')

    partner_qualification_image_lines = fields.One2many('partner.qualification.image.line', 'partner_id',
                                                        string=u'企业资质',
                                                        help=u'企业资质明细行')


class PartnerQualificationLine(models.Model):
    _name = 'partner.qualification.line'
    _description = u'购货订单PDF明细'

    partner_id = fields.Many2one('partner', string=u'供应商',
                                 ondelete='cascade',
                                 help=u'企业资质对应的供应商')
    name = fields.Char(u'编号')
    introduction = fields.Char(u'资质描述')
    partner_qualification = fields.Binary(u'资质文件',
                                          help=u'点击上传企业资质')


class PartnerQualificationImageLine(models.Model):
    _name = 'partner.qualification.image.line'
    _description = u'购货订单图片明细'

    partner_id = fields.Many2one('partner', string=u'供应商',
                                 ondelete='cascade',
                                 help=u'企业资质对应的供应商')
    name = fields.Char(u'编号')
    introduction = fields.Char(u'资质描述')
    partner_qualification = fields.Binary(u'资质文件',
                                          help=u'点击上传企业资质')
