from frappe.website.utils import delete_page_cache

def clear_contents():
	delete_page_cache("contents")
