# Advance Payment Entry

<p class="lead"> To record an advance payment a Journal Voucher is made along with a Sales Invoice for future payment.</p>

### Journal Voucher

A Journal Voucher (JV) is a method of entering accounting information. JV entries include debit and credit information. Make a Journal Voucher to note the advance given by Jane-the Customer.

> Accounts > Journal Voucher > New Journal Voucher

Payment done by the Customer before accepting delivery of the product is an Advance Payment. This is done to confirm the order and is paid as token to start manufacturing the product. For orders of high value, the business houses expect to receive advance. Thus, open a new Journal Voucher and make the advance entry.

__Figure 1: Journal Voucher-Advance Payment Entry__

![Advance Entry](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-advance.png)

Since the Customer has given 10000/- as cash advance, it will be recorded as a credit entry against the Customer. To balance it with the debit entry (Double Entry Accounting) enter 10000/- as debit against the Company’s cash account.

__Double Entry Accounting__

Double Entry Accounting or bookkeeping is a system of accounting in which every transaction has a corresponding positive and a negative entry: debits and credits. Every transaction involves a debit entry in one account and a credit entry in another account. This means that every transaction must be recorded in two accounts; one account will be debited, because it receives value and the other account will be credited, because it has given value. [1]
 

__Figure 2: Double Entry Accounting__

![Double Accounting Entry](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-jv-advance-childbed.png)

Save and submit the JV. If this document is not saved it will not be pulled in other accounting documents.

### Sales Invoice

A Sales Invoice is a bill that you send to your Customers, against which the Customer processes the payment. Sales Invoice is an accounting transaction. On submission of Sales Invoice,  the system updates the receivable and books income against a Customer Account.

> Accounts > Sales Invoice > New Sales Invoice

In this case, the Sales Order is made for an amount of Rs 100000/- Supreme Furniture will charge the Customer in phases. Thus they will make 3 Sales Invoices, two will charge 25,000 each and one will be for Rs 50, 000/- Quantity will be specified as 0.25, 0.25 and 0.50 respectively.

__Figure 3: Sales Invoice for Quarter of the total amount__

![Sales Invoice](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-sales-invoice-childbed.png)

To link the Sales Invoice to the Journal Voucher which mentions the advance Payment Entry, click on ‘Get Advances Received’.  Allocate the amount of  advance in the advances table. The accounting will be adjusted accordingly.

> Note: In case you get error while saving, due to Qty being in fraction, go to UOM master and uncheck the box that says ‘Must be whole number’.

__Figure 4: Advance pulled from JV__

![Advance Pulled](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-advance-payment.png)


Save and submit the Sales Invoice. You can start making the Production Order and raise Material Requests for manufacturing this product via the Production Planning Tool.

Next: [Production Planning Tool](/contents/guide-books/engineer-to-order/production-planning-tool)

---

References

1. [Wikipedia: Double Entry Accounting](http://en.wikipedia.org/wiki/Double-entry_bookkeeping_system)
