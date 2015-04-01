# Supplier Billing

<p class="lead"> Supplier Billing is done by raising a Purchase Invoice and making a Payment Entry through a Journal Voucher.</p>

### Purchase Invoice

Depending on the payment terms, Purchase Invoice is  made either on Purchase Order or on receipt of materials. If your Supplier's billing is linked to receipts, then make the Purchase Invoice from Purchase Receipt, or else, make it from Purchase Order.

> Accounts > Purchase Invoice > New Purchase Invoice

__Figure 1: Make Purchase Invoice__

![Purchase Invoice](assets/manual_erpnext_com/old_images/erpnext/m-t-s-purchase-invoice.png)

Payment Entry is done to book all accounting transactions in your system. It is an important step of Book Keeping.

__Double Entry Accounting__

Double entry bookkeeping is a system of accounting in which every transaction has a corresponding positive and negative entry : debits and credits. Every transaction involves a debit entry in one account and a credit entry in another account. [1] This means that every transaction must be recorded in two accounts; one account will be debited because it receives value and the other account will be credited because it has given value. ERPNext follows the Double Entry Accounting method.

### Payment Entry

Payment Entry is done after you click on the button Make Payment Entry. The entries will be done by the system. However, it is necessary that you click on the button ‘Make Difference Entry’. This step will calculate the total debt and the total credit. Payment Entry can also be done independently through the Journal Voucher.

> Accounts > Journal Voucher > New Journal Voucher

__Figure 2: Make Payment Entry__

![Payment Entry](assets/manual_erpnext_com/old_images/erpnext/m-t-s-payment-entry.png)

In case for some reason, the account section is blank, it means that you have not selected your default bank account. If you wish that your bank account field is pre-filled you can click on the triangle button next to the Company and set the default master account.

__Figure 3: Go to Masters (Optional: In case defaults not set)__

![Default setting](/assets/manual_erpnext_com/old_images/erpnext/triangle-button-company.png)

The click will take you to the Master-Company file. Now enter your default entry account as HDFC Bank/Axis Bank etc and Save. This will enable the system to post debit/credit entries directly against this particular account.

After completing the Purchase cycle, you can start manufacturing the Item.


Next: [Manufacturing](/guide-books/make-to-stock/manufacturing)


References


1. [Wikipedia: Double Entry Accounting](http://en.wikipedia.org/wiki/Double-entry_bookkeeping_system)
