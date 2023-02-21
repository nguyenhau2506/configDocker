from odoo import http
import logging

_logger= logging.getLogger(__name__)
class Management(http.Controller):

    @http.route("/management/managementTel")
    def list (self,*args,**kwargs ):
        Manage =http.request.env["list.telephone.number"]
        managers= Manage.search([])
        return http.request.render('management.management_list_template',{"managers":managers})
    