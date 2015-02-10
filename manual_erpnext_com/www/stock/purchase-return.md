ERPNext has an option to account for products that are returned to the
supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc. The transactions
dealing with return of goods are also accounting transactions and have to be
recorded in the books of accounts just like any other accounting transaction.

> Stock > Stock Entry > New Stock Entry

__Step 1:__ Select Purpose as Purchase Return.

Enter Purchase Return No and the Default Source Warehouse. Source Warehouse is
a place from where you issue or transfer materials.

#### Figure 1: Enter Purchase Return as Purpose

![](assets/erpnext_org/images/erpnext/purchase-return-5.png)  

  

__Step 2:__ Add New Row and Enter Item Code. 

#### Figure 2: Enter Item Code and Quantity  

![](assets/erpnext_org/images/erpnext/purchase-invoice-2.png)  

__Step 3:__ Enter Accounting Information.  

  
#### Figure 3: Enter Accounting Information

![](assets/erpnext_org/images/erpnext/purchase-return-3-3.png)  

  
__Step 4:__ Save the Document and Submit it.  

  

Make a Debit Note and Save the Journal Voucher.

  
#### Figure 4: Journal Entries details

![](assets/erpnext_org/images/erpnext/purchase-return-4-3.png)  

  

> If supplier doesn't send an invoice after sending goods, there is no need of
making a Debit Note. However, if he has sent an invoice and his goods are
returned due to some fault, then there could be 2 situations which arise;
either, you have made partial/full payment or not made any payment.

> Either way, generally supplier will issue you a Credit Note. And in that
case, you will make a Debit Note which will debit the supplier account and
credit the expense / stock received but not billed (perpetual inventory)
account. This Debit Note can be adjusted at the time of any future payment
against any outstanding invoices.  

**Quick Review**  

  * To select Purchase Return go to Stock Entry.
  * Select Purchase Return under Purpose.
  * Enter Purchase Receipt number.
  * Enter Source Warehouse details.
  * Provide Supplier Information.
  * Save  and Submit the document.
  * Make a Debit Note.

