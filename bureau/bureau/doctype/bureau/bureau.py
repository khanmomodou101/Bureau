# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Bureau(Document):
    def validate(self):
        self.validate_company()
        self.validate_user()
    def validate_company(self):
            """Create a System user for Agent creation if not already exists"""
            if not frappe.db.exists("Company", self.business_name):
                company = frappe.get_doc({
					"doctype": "Company",
                    "company_name":self.business_name,
					"abbr": self.abbr,
					"default_currency": self.default_currency,
                    
				})
                company.save(ignore_permissions=True)
    def on_update(self):
           company = frappe.get_doc("Company", self.business_name)
           company.business_name =  self.business_name
           company.abbr = self.abbr
           company.default_currency = self.default_currency
           
           company.save(ignore_permissions=True)
           
	#validate user
    def validate_user(self):
            """Create a System user for Agent creation if not already exists"""
            if not frappe.db.exists("User", self.email):
                agent_user = frappe.get_doc({
					"doctype": "User",
					"first_name": self.first_name,
					"last_name": self.last_name,
					"middle_name": self.middle_name,                                   
                    "username": self.username,
					"email": self.email,
					"gender": self.gender,
					"send_welcome_email": 0,
					"user_type": "System User",
                    "role_profile_name":"Bureau Admin",
                    "module_profile":"Bureau Admin",
                    
				})
                agent_user.save(ignore_permissions=True)
    #if user is updated
    def on_update(self):
           user_doc = frappe.get_doc("User", self.email)
           user_doc.first_name =  self.first_name
           user_doc.last_name = self.last_name
           user_doc.middle_name = self.middle_name
           user_doc.username = self.username
           user_doc.gender = self.gender
           

           
           
           user_doc.save(ignore_permissions=True)
                
    def on_trash(self):
                frappe.delete_doc("User", self.email)
        # def on_update(self):
        #       full_name = self.first_name + " " + self.last_name
        #       self.db_set("full_name", full_name)
                
    def on_trash(self):
                frappe.delete_doc("Company", self.business_name)
        # def on_update(self):
        #       full_name = self.first_name + " " + self.last_name
        #       self.db_set("full_name", full_name)