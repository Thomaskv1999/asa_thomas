// // Copyright (c) 2025, thomas and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Annual Service Agreement", {

    customer_name: function(frm){
        if(frm.doc.customer_name){
            frappe.call({
                method: "asa_thomas.asa_thomas.doctype.annual_service_agreement.annual_service_agreement.get_customer_email",
                args: {
                    customer_name: frm.doc.customer_name
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("customer_email", r.message.email)
                        frm.set_value("contact_number", r.message.phone)
                    }}
                })
            }},
    asa_billing_add: function(frm) {
        update_totals(frm)
    },
    asa_billing_remove: function(frm) {
        update_totals(frm)
    },
    asa_coverage_add: function(frm) {
        update_totals(frm)
    },
    asa_coverage_remove: function(frm) {
        update_totals(frm)
    },
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button("Update Agreement Status", function() {
                let d = new frappe.ui.Dialog({
                    title: 'Update Agreement Status',
                    fields: [
                        {
                            label: 'Status',
                            fieldname: 'status',
                            fieldtype: 'Select',
                            options: ["Expired", "Suspended", "Terminated"],
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Confirm',
                    primary_action(values) {
                        d.hide();
                        frappe.call({
                            method: "asa_thomas.asa_thomas.doctype.annual_service_agreement.annual_service_agreement.update_agreement_status",
                            args: {
                                docname: frm.doc.name,
                                status: values.status
                            },
                            callback: function(r) {
                                if (!r.exc) {
                                    frappe.msgprint("Status updated successfully")
                                    frm.reload_doc()
                                }
                            }
                        })
                    }
                })
                d.show()
            })
        } },
    status: function(frm) {
        if (frm.doc.status === "Active") {
            frm.add_custom_button("Add Visit Entry", function() {
                let d = new frappe.ui.Dialog({
                    title: 'Add Visit Entry',
                    fields: [
                        {
                            label: 'Date',
                            fieldname: 'date',
                            fieldtype: 'Date',
                            reqd: 1
                        },
                        {
                            label: 'Performed By',
                            fieldname: 'performed_by',
                            fieldtype: 'Link',
                            options:'Employee',
                            reqd: 1
                        },
                        {
                            label: 'Service Provided',
                            fieldname: 'service_provided',
                            fieldtype: 'Small Text',
                            reqd: 1
                        },
                        {
                            label: 'Time Spend(hrs)',
                            fieldname: 'time_spendhrs',
                            fieldtype: 'Float',
                            reqd: 1
                        },
                         {
                            label: 'Remarks',
                            fieldname: 'remarks',
                            fieldtype: 'Small Text',
                            reqd: 1
                        },
                         {
                            label: 'Visit Verified',
                            fieldname: 'visit_verified',
                            fieldtype: 'Check',
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Confirm',
                    primary_action(values) {
                        d.hide()
                        let child = frm.add_child("asa_visit")
                        child.visit_date = values.date
                        child.performed_by= values.performed_by
                        child.service_provided = values.service_provided
                        child.time_spendhrs = values.time_spendhrs
                        child.remarks = values.remarks
                        child.visit_verified = values.visit_verified

                        frm.refresh_field("asa_visit")
                        let row_count = frm.doc.asa_visit.length
                        frm.set_value('total_visits', row_count)
                        frappe.msgprint("Visit entry added")
                    }
                })
                d.show()
            })
        }
        else{
				frm.remove_custom_button("Add Visit Entry")
			}
    },

    agreement_title: function(frm) {
        if (frm.doc.agreement_title) {
            frappe.call({
                method: "asa_thomas.asa_thomas.doctype.annual_service_agreement.annual_service_agreement.generate_agreement_id",
                args: {
                    agreement_title: frm.doc.agreement_title
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("agreement_id", r.message)
                    }
                }
            })
        }
    },
    start_date: function(frm) {
        date_diff(frm)
    },
     end_date: function(frm) {
        date_diff(frm)
    },



    after_save:function(frm) {
        let d = new frappe.ui.Dialog({
            title: 'Confirm Submission',
            fields: [
                {
                    label: 'Agreement Title',
                    fieldname: 'agreement_title',
                    fieldtype: 'Data',
                    default: frm.doc.agreement_title,
                    read_only: 1
                },
                {
                    label: 'SLA Type',
                    fieldname: 'sla_type',
                    fieldtype: 'Data',
                    default: frm.doc.sla_type,
                    read_only: 1
                },
                {
                    label: 'Total SLA Value',
                    fieldname: 'total_sla_value',
                    fieldtype: 'Data',
                    default: frm.doc.total_sla_value,
                    read_only: 1
                },
                {
                    label: 'Duration',
                    fieldname: 'duration',
                    fieldtype: 'Data',
                    default: frm.doc.duration,
                    read_only: 1
                },
            ],
           primary_action_label: 'Confirm',
        secondary_action_label: 'Cancel',
        primary_action() {
            d.hide()
            frm.save().then(() => {
                frappe.msgprint("Document Saved")
                frm.reload_doc()
            })
        },
        secondary_action() {
            d.hide()
            frappe.msgprint("Submission Cancelled")
        }
    })

    d.show()
}
    
    
})

frappe.ui.form.on("ASA Coverage", {
    estimated_service_time: function(frm, cdt, cdn) {
        update_totals(frm, cdt, cdn)
    },
    rate: function(frm, cdt, cdn) {
        update_totals(frm, cdt, cdn)
    }
})


function update_totals(frm, cdt, cdn) {
    let row = locals[cdt][cdn]

    let service_time = row.estimated_service_time || 0
    let rate = row.rate || 0
    let total = rate * service_time
 
    frappe.model.set_value(cdt, cdn, "sla_value", total)
    
    let total_sla = 0
    frm.doc.asa_coverage.forEach(value =>{
        total_sla += value.sla_value || 0
    })
    frm.set_value("total_sla_value",total_sla)

    let total_invo = 0
    frm.doc.asa_billing.forEach(value =>{
        total_invo += value.amount || 0
    })

    frm.set_value("total_invoiced",total_invo)
    frm.set_value("outstanding_amount",total_sla - total_invo)
}




frappe.ui.form.on("ASA Visit", {
    asa_visit_add: function(frm) {
        update_total_visits(frm)
    },
    asa_visit_remove: function(frm) {
        update_total_visits(frm)
    }
})
function update_total_visits(frm) {
    let row_count = frm.doc.asa_visit.length
    frm.set_value('total_visits', row_count)
}
function date_diff(frm){
 if (frm.doc.start_date && frm.doc.end_date) {
            let start= frappe.datetime.str_to_obj(frm.doc.start_date)
            let end = frappe.datetime.str_to_obj(frm.doc.end_date)
            let diff = frappe.datetime.get_day_diff(end,start)
            frm.set_value("duration", diff)
        }
        
    }
frappe.ui.form.on("ASA Billing", {
    amount :function(frm,cdt,cdn){
        update_totals(frm,cdt,cdn)
    },
   

})
