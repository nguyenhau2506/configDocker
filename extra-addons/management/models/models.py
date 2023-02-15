# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class management(models.Model):
#     _name = 'management.management'
#     _description = 'management.management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class management (models.Model):
    _name= "list.telephone.number"
    _description= "this is the list of customer telephonenumber"

    name= fields.Char("Name",required=True)
    telephoneNumber= fields.Char("tel",required=True)
    created_at=fields.Date()
    def toggle_hidden(self):
        self.ensure_one()
        for management in self:
            management.hidden = False if management.hidden else True
        return True

