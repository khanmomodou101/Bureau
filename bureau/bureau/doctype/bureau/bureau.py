# Copyright (c) 2023, Momodou khan and contributors
# For license information please see license.txt

import frappe
from frappe.model.document import Document

class Bureau(Document):
    def validate(self):
        self.create_company()
    #     self.validate_company()
    #     self.validate_user()
    # def validate_company(self):
    #         """Create a System user for Agent creation if not already exists"""
    #         if not frappe.db.exists("Company", self.business_name):
    #             company = frappe.get_doc({
	# 				"doctype": "Company",
    #                 "company_name":self.business_name,
	# 				"abbr": self.abbr,
	# 				"default_currency": self.default_currency,
                    
	# 			})
    #             company.save(ignore_permissions=True)
    # def on_update(self):
        #    self.update_user()
           
	# #validate user
    # def create_user(self):
    #         """Create a System user for Agent creation if not already exists"""
    #         agent_user = frappe.get_doc({
    #             "doctype": "User",
    #             "first_name": self.first_name,
    #             "last_name": self.last_name,
    #             "middle_name": self.middle_name,                                   
    #             "username": self.username,
    #             "email": self.email,
    #             "gender": self.gender,
    #             "send_welcome_email": 0,
    #             "user_type": "System User",
    #             "role_profile_name":"Bureau Admin",
    #             "module_profile":"Bureau Admin",
                
    #         })
    #         agent_user.save(ignore_permissions=True)
    #if user is updated
    def update_user(self):
           user_doc = frappe.get_doc("User", self.email)
           user_doc.first_name =  self.first_name
           user_doc.last_name = self.last_name
           user_doc.middle_name = self.middle_name
           user_doc.username = self.username
           user_doc.gender = self.gender
           user_doc.save(ignore_permissions=True)


    #create company if bureau is created
    def create_company(self):
        if not frappe.db.exists("Company", self.business_name):
            company = frappe.get_doc({
                "doctype": "Company",
                "company_name":self.business_name,
                "abbr": self.abbr,
                "default_currency": self.default_currency,
                "Country": 'Gambia',
                "email": self.email,
                "create_chart_of_accounts_based_on": 'Standard Template',
                "charts_of_accounts": "Standard",
                "default_currency": "GMD",


                
            })
            company.save(ignore_permissions=True)


                