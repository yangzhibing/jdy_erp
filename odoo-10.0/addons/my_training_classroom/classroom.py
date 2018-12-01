from openerp.osv import fields, osv

class my_training_classroom(osv.osv):
    _name = 'my.training.classroom'
    _discription = u'教室'
    _columns = {
        'number': fields.char(u'编号', size=64, select=True),
        'capacity': fields.integer(u'容纳人数', select=True),
        'location': fields.char(u'地点', size=125, select=True),
    }
my_training_classroom()