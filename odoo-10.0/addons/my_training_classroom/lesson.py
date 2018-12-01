from openerp.osv import fields, osv

class my_training_lesson(osv.osv):
    _name = 'my.training.lesson'  #本对象的名称
    _inherit = 'my.training.lesson'  #要继承的对象的_name
    _columns = {
       'classroom_id': fields.many2one('my.training.classroom', u'教室'), #添加一个教室属性，为多对一对象。
    }

my_training_lesson()