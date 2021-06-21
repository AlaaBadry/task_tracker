// Copyright (c) 2016, xsolutions and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Task Status Report"] = {
	"filters": [
		{
			"fieldname": "exp_start_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"width": 120
		},
		{
			"fieldname": "exp_end_date",
			"label": __("End Date"),
			"fieldtype": "Date",
			"width": 120
		}
	]
};
