An Item is your companys' product or a service. The term Item is applicable to your core products as well as your raw materials. It can be a product or service that you buy/sell from your customers/ suppliers. ERPNext allows you to manage all sorts of items like raw-materials, sub-assemblies, finished goods, item variants and service items.

ERPNext is optimized for itemized management of your sales and purchase. If you are in services, you can create an Item for each services that your offer. Completing the Item Master is very essential for successful implementation of ERPNext.

## Item Properties

  * **Item Name:** Item name is the actual name of your product or service.
  * **Item Code:** Item Code is a short-form to denote your Item. If you have very few Items, it is advisable to keep the Item Name and the Item Code same. This helps new users to recognise and update Item details in all transactions. In case you have lot of Items with long names and the list runs in hundreds, it is advisable to code. To understand naming Item codes see [Item Codification](/contents/stock/item/item-codification)
  * **Item Group:** Item Group is used to categorize an Item under various criterias like products, raw materials, services, sub-assemblies, consumables or all Item groups. Create your default Item Group list under Setup> Item Group and pre-select the option while filling your New Item details under [Item Group](/contents/stock/setup/item-group)
  * **Default Unit of Measure:** This is the default measuring unit that you will use for your product. It could be in nos, kgs, meters, etc. You can store all the UOM’s that your product will require under Set Up> Master Data > UOM. These can be preselected while filling New Item by using % sign to get a pop up of the UOM list.
  * **Brand:** If you have more than one brand save them under Set Up> Master Data> Brand and pre-select them while filling a New Item.
  * **Variant:** A Item Variant is a different version of a Item.To learn more about managing varaints see [Item Variants](/contents/stock/item/item-variants)
  
### Upload an Image

To upload an image for your icon that will appear in all transactions, save
the partially filled form. Only after your file is saved  the 'upload' button will
work above the Image icon. Click on this sign and upload the image.

### Inventory : Warehouse and Stock Setting

In ERPNext, you can select different type of Warehouses to stock your
different Items. This can be selected based on Item types. It could be Fixed
Asset Item, Stock Item or even Manufacturing Item.

  * **Stock Item:** If you are maintaining stock of this Item in your Inventory, ERPNext will make a stock ledger entry for each transaction of this item.
  * **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions. 
  * **Allowance Percentage:** This is the percent by which you will be allowed to over-bill or over-deliver this Item. If not set, it will select from the Global Defaults. 
  * **Valuation Method:** There are two options to maintain valuation of stock. FIFO (first in - first out) and Moving Average. To understand this topic in detail please visit “ Item Valuation, FIFO and Moving Average”.

### Serialized and Batched Inventory

These numbers help to track individual units or batches of Items which you sell. It also tracks warranty and returns. In case any individual Item is recalled by the supplier the number system helps to track individual Item. The numbering system also manages expiry dates. Please note that if you sell your items in thousands, and if the items are very small like pens or erasers, you need not serialize them. In ERPNext, you will have to mention the serial number in some accounting entries. To create serial numbers you will have to manually create all the numbers in your entries. If your product is not a big consumer durable Item, if it has no warranty and has no chances of being recalled, avoid giving serial numbers.

> Important: Once you mark an item as serialized or batched or neither, you cannot change it after you have made any stock entry.

  * [Discussion on Serialized Inventory](/contents/setting-up/stock-reconciliation-for-non-serialized-item)  

### Re Ordering

  * **Re-order level** suggests the amount of stock balance in the Warehouse. 
  * **Re-order Qty** suggests the amount of stock to be ordered to maintain minimum stock levels.
  * **Minimum Order Qty** is the minimum quantity for which a Material Request / Purchase Order must be made.

### Item Tax

These settings are required only if a particular Item has a different tax rate
than the rate defined in the standard tax Account. For example, If you have a
tax Account, “VAT 10%” and this particular Item is exempted from tax, then you
select “VAT 10%” in the first column, and set “0” as the tax rate in the
second column.

Go to [Setting Up Taxes](/contents/setting-up/setting-up-taxes) to understand this topic in detail.

### Inspection

Inspection Required: If an incoming inspection (at the time of delivery from
the Supplier) is mandatory for this Item, mention “Inspection Required” as
“Yes”. The system will ensure that a Quality Inspection will be prepared and
approved before a Purchase Receipt is submitted.

Inspection Criteria: If a Quality Inspection is prepared for this Item, then
this template of criteria will automatically be updated in the Quality
Inspection table of the Quality Inspection. Examples of Criteria are: Weight,
Length, Finish etc.

### Purchase Details

![Purchase Details](/assets/manual_erpnext_com/old_images/erpnext/item-purchase.png)

**Lead time days:** Lead time days are the number of days required for the Item to reach the warehouse.

**Default Expense Account:** It is the account in which cost of the Item will be debited.

**Default Cost Centre:** It is used for tracking expense for this Item.

### Sales Details

![Sales Details](/assets/manual_erpnext_com/old_images/erpnext/item-sales.png)

**Default Income Account:** Income account selected here will be fetched automatically in sales invoice for this item.

**Cost Centre:** Cost center selected here will be fetched automatically in sales invoice for this item.

### Manufacturing And Website

![Manufacturing](/assets/manual_erpnext_com/old_images/erpnext/item-manufacturing-website.png)

Visit [Manufacturing](/contents/manufacturing) and [Website ](/contents/website)to understand these topics in detail.

{next}
