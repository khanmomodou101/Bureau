import frappe
from frappe import auth
import requests

#set exchange rate for every 8 hours
@frappe.whitelist()
def exchange_rate():
    docs = frappe.get_list("Currency", filters={
        'enabled': 1
    })
    api_key = 'a7a15842901bad36bb927098'

    for doc in docs:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{doc.name}/GMD"
        response = requests.get(url).json()
        rate = response['conversion_rate']
        frappe.db.set_value('Currency', doc.name, "exchange_rate", rate)
        frappe.db.commit()


@frappe.whitelist( allow_guest=True )
def login(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key":0,
            "message":"Authentication Error!"
        }

        return

    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)

    frappe.response["message"] = {
        "success_key":1,
        "message":"Authentication success",
        "sid":frappe.session.sid,
        "api_key":user.api_key,
        "api_secret":api_generate,
        "username":user.username,
        "email":user.email
    }



def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()

    return api_secret
