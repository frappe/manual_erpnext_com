# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

from __future__ import unicode_literals
from frappe.website.utils import get_full_index

def get_context(context):
	for item in get_full_index():
		if item.page_name=="contents":
			context.full_index = item.children
			break
