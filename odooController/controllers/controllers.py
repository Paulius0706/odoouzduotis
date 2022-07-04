# -*- coding: utf-8 -*-
from logging import root
from msilib.schema import ODBCDataSource
from odoo import http



class OdooController(http.Controller):

    @http.route('/odooController/odooController',csrf=False, auth='public',website=True)
    def odooController(self, **kw):
        documents = []
        companies = []
        try:
            documents = http.request.env['my.document'].sudo().search([])
            companies = http.request.env['res.company'].sudo().search([])
        except:
            print('Something went wrong')
        
        return http.request.render("odooController.index",{
            'documents':documents,
            'companies':companies,
            'documentsCount': len(documents),
            'companiesCount': len(companies),
            'root': '/odooController/odooController'
        })

    @http.route('/odooController/odooController/document/<int:obj>/', auth='public',website=True)
    def document(self, obj, **kw):
        document = http.request.env['my.document'].sudo().browse(obj)
        company = http.request.env['my.document'].sudo().browse(obj).company_id
        print('document: ',document)
        print('company: ',company)
        return http.request.render('odooController.document', {
            'document':  document,
            'company':  company,
            'root': '/odooController/odooController'
        })
    @http.route('/odooController/odooController/documentEdit/<int:obj>/', auth='public',website=True)
    def documentEdit(self, obj, **kw):
        document = http.request.env['my.document'].sudo().browse(obj)
        companies = http.request.env['res.company'].sudo().search([])
        print('documentEdit vvvvv')
        print('document: ',document)
        print('companies: ',companies)
        return http.request.render('odooController.documentEdit', {
            'document':  document,
            'companies':  companies,
            'root': '/odooController/odooController'
        })
    
    @http.route('/odooController/documentUpdate', methods=['POST'],csrf=False,type="http", auth="public", website=True)
    def documentUpdate(self, **kw):
        d_id = int(kw.get('id'))
        d_name = str(kw.get('name'))
        d_description = str(kw.get('description'))
        d_company_id = kw.get('company_id')
        if(d_company_id != 'No Company'):
                d_company_id = int(kw.get('company_id'))
                print(d_company_id)
        
        try:
            document = http.request.env['my.document'].sudo().browse(d_id)
            print(document)
            print("d_id=",d_id)
            print("d_name=",d_name)
            print("d_description=",d_description)
            print("d_company_id=",d_company_id)
            document.name = d_name
            document.description = d_description
            if(d_company_id != 'No Company'):
                d_company_id = int(kw.get('company_id'))
                company = http.request.env['res.company'].sudo().browse(d_company_id)
                print(company)
                document.company_id = company 
                # http.request.env["my.document"].browse(d_id).write({'name':d_name,'description':d_description,'company_id':d_company_id}) 
        except:
            print('Something went wrong')
        return http.request.render("odooController.documentUpdate",{
            'root': '/odooController/odooController',
            'document': document
        })
    
    @http.route('/odooController/odooController/documentAdd', methods=['POST'],csrf=False,type="http", auth="public", website=True)
    def documentAdd(self, **kw):
        companies = http.request.env['res.company'].sudo().search([])
        creationCompany = kw.get('company')
        print('raw creationCompany:', creationCompany)
        if creationCompany:
            creationCompany = http.request.env['res.company'].sudo().browse(int(creationCompany))
            print('creationCompany:', creationCompany)
            return http.request.render('odooController.documentAdd', {
                'root' : '/odooController/odooController',
                'companies': companies,
                'creationCompany': creationCompany
            })
        else:
            print('no creationCompany')
            return http.request.render('odooController.documentAdd', {
                'root' : '/odooController/odooController',
                'companies': companies,
            })
    
    @http.route('/odooController/documentInsert', methods=['POST'],csrf=False,type="http", auth="public", website=True)
    def documentInsert(self, **kw):
        d_name = str(kw.get('name'))
        d_description = str(kw.get('description'))
        d_company_id = kw.get('company_id')
        if(d_company_id != 'No Company'):
                d_company_id = int(kw.get('company_id'))
                d_company_id = http.request.env['res.company'].sudo().browse(d_company_id)
        # try:
        print("d_name=",d_name)
        print("d_description=",d_description)
        print("d_company_id=",d_company_id)
        if(d_company_id != 'No Company'):
            print('creating with company link')
            http.request.env['my.document'].sudo().create({'name':d_name,'description':d_description,'company_id':d_company_id.id})
        else:
            print('creating without company link')
            http.request.env['my.document'].sudo().create({'name':d_name,'description':d_description}) 
        # except:
        #     print('Something went wrong')
        return http.request.render('odooController.documentInsert', {
            'company': d_company_id,
            'root': '/odooController/odooController'
        })
        
    
    
    
    @http.route('/odooController/odooController/company/<int:obj>/', auth='public',website=True)
    def company(self, obj, **kw):
        company = http.request.env['res.company'].sudo().browse(obj)
        documents = http.request.env['res.company'].sudo().browse(obj).documents_id
        print('company: ',company)
        print('documents: ',documents)
        return http.request.render('odooController.company', {
            'company':  company,
            'documents':  documents,
            'root': '/odooController/odooController'
        })
    @http.route('/odooController/odooController/companyEdit/<int:obj>/', auth='public',website=True)
    def companyEdit(self, obj, **kw):
        company = http.request.env['res.company'].sudo().browse(obj)
        documents = http.request.env['res.company'].sudo().browse(obj).documents_id
        print('company: ',company)
        print('documents: ',documents)
        return http.request.render('odooController.companyEdit', {
            'company':  company,
            'documents':  documents,
            'root': '/odooController/odooController'
        })
    
    
        
    
    
    
# def call_users(self,data):
#      cr, uid, context = request.cr, request.uid, request.context
#      request.registry.get('res.users').change_value(cr,uid,context=context) 
#      return True