from odoo import fields,models 

class detail_information(models.Model):
    _name ="detail.information"
    _description= " detail "
    _inherit = "list.telephone.number"
    is_available = fields.Boolean("is Available")
    age=fields.Char("Age",required=True)
    family_of_membe=fields.Char("family of member",required=False)

