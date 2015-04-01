from frappe.website.utils import delete_page_cache

def clear_contents(path):
	delete_page_cache("contents")
