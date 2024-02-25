import frappe
from frappe import auth

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

    #create chart of account if branch is created
def create_chart_of_account(doc, method=None):

    if not frappe.db.exists("Account", f'{doc.branch_name} - {frappe.db.get_value("Bureau", doc.bureau, "abbr")}'):
        chart_of_accounts = frappe.get_doc({
            "doctype": "Account",
            "company": frappe.db.get_value("Bureau", doc.bureau, "business_name"),
            "account_name": doc.branch_name,
            'parent_account': f'Cash In Hand - {frappe.db.get_value("Bureau", doc.bureau, "abbr")}',
            "account_type": "Cash",
            "root_type": "Asset",
            "is_group": 0,
            "account_currency": "GMD",
           
        })
        chart_of_accounts.save(ignore_permissions=True)

    bureau = frappe.get_doc("Bureau", doc.bureau)
    bureau.append('branches', {
        'branch': doc.branch_name,
        'branch_location': doc.branch_location
    })
    bureau.save()


