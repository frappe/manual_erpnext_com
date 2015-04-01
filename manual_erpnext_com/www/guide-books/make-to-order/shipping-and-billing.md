# Shipping and Billing

<p class="lead"> Shipping goods requires a Delivery Note and Billing involves making a Sales Invoice and a Payment Entry.</p>

Delivery Note is a document accompanying a shipment of goods that lists the description, and quantity of the goods delivered [1]. You can make a Delivery Note from Stocks or from a submitted Sales Order by clicking on the Action button placed at the right hand corner of the form. 

> Stocks > Delivery Note > New Delivery Note 

### Delivery Note

Make a Delivery Note and save it after affirming the shipping address. In case the document has no shipping address, create one by clicking on the + button. You can create the new address in the address form, which opens after clicking the + button . Save it and come back to the Delivery Note. Submit the Delivery Note. 

__Figure 1: Delivery Note__

![Delivery Note](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-delivery-note-1.png)

### Sales Invoice

A Sales Invoice is a bill that you send to your Customers against which the Customer processes the payment. Sales Invoice is an accounting transaction. On submission of Sales Invoice, the system updates the receivables and books income against a Customer account.

> Accounts > Sales Invoice > New Sales Invoice

You can either make a Sales Invoice from the Accounts module or make it by clicking on the right hand corner of the Delivery Note.

__Figure 2: Invoice__

![Invoice](/assets/manual_erpnext_com/old_images/erpnext/m-t-o-invoice-jps-1.png)

Save and submit the Invoice. When you submit the Invoice, an email pop-up box will appear. Correct / change / Confirm the email ID and click on 'Send' button. An email will be sent.

### Payment Entry

Payment Entry is a part of booking-keeping. It records accounts and manages balance sheets. You can make it through a Journal Voucher or directly from a submitted Invoice by clicking on the 'Make Payment Entry' button.
 
> Accounts > Journal Voucher

#### Double Entry Accounting

Double Entry Accounting or bookkeeping is a system of accounting in which every transaction has a corresponding positive and a negative entry: debits and credits. Every transaction involves a debit entry in one account and a credit entry in another account. This means that every transaction must be recorded in two accounts; one account will be debited, because it receives value and the other account will be credited, because it has given value. [2]
 
#### Journal Voucher

To make a Payment Entry update the Journal Voucher with debit and credit columns. Make sure to click on the button that says ‘Make Difference Entry’. Note that the reference number and reference date is mandatory along with the Account entry. In case for some reason, the account section is blank, it means that you have not selected your default bank account. To do so from the same form, click on the triangle button next to the Company and set the default master account.

The click will take you to the Master-Company page. Now enter your default entry account as HDFC Bank / Axis Bank etc and save. This will enable the system to post debit / credit entries directly against this particular account.

__Figure 3: Payment Entry__

![Payment Entry](/assets/manual_erpnext_com/old_images/erpnext/m-t-o-payment-entry-jps-1.png)

Save and submit the Payment Entry. After submitting, you can check the Gross Profit Report, and review your profits. You can also check your Stock Balance Report.

Next: [Reports](/guide-books/make-to-order/reports)

---

References: 

1. [Business Directory: Delivery Note](http://www.businessdictionary.com/definition/delivery-note.html)
2. [Wikipedia: Double Entry Accounting](http://en.wikipedia.org/wiki/Double-entry_bookkeeping_system)