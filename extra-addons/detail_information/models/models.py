from odoo import fields,models 

class detail_information(models.Model):
    _name ="detail.information"
    _description= " detail "
    _inherit = "list.telephone.number"
    is_available = fields.Boolean("is Available")
    age=fields.Char("Age",required=True)
    relation=fields.Selection([ ('type1', 'Father'),('type2', 'Mother'),],'Type', default='type1')
    family_of_member=fields.Char("family of member",required=False)

class NoteID(models.Model):
    _inherit= "list.telephone.number"
    note_id= fields.Many2one("detail.information",relation="de_rel",string="Detail")    
    

