# Setting Up

<p class="lead">In a make-to-stock system, the products are manufactured and stocked. To begin this order cycle, it is essential to create an Item master, Customers-distributors/retailers, and Suppliers.</p>

An [Item](/stock/item-master) is your company's product or a service. The term Item is applicable to your core products as well as your raw materials. It can be a product or service that you buy/sell from your Customers/Suppliers. ERPNext allows you to manage all sorts of Items like raw-materials, sub-assemblies, finished goods, Item variants and service Items.

> Stock > Item > New Item

#### Step 1: Create an Item 'Butterfly Print' bag

1. Say Yes to ‘ Is Stock Item’, since this is a Stock Item. Mention the default Warehouse as ‘Finished Goods’ because after being manufactured it will be stored at the 'Finished Goods Warehouse'. 
1. Say No to ‘Is Purchase Item’, since this Item will be manufactured. 
1. Say Yes to  ‘Is Sales Item, since this product will be sold. 
1. Say Yes to ‘Allow Production Order’ and 
1. Say Yes to ‘ Allow Bill of Materials’.

__Figure 1: Item__

![Butterfly Print Item](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-item-butterfly-print.png)

Warehouse is a mandatory field. The Item form will not be saved unless you enter a default Warehouse.

**Note:** In reality you may not have three Warehouses. You may have one, which you use for raw materials, for manufacturing/stitching/producing and also for storing finished goods. In such cases, you have to only imagine separate spaces for each activity, and name them accordingly. For system entry purpose, having three different Warehouses for stocking raw materials, manufacturing unfinished goods and storing finished goods is a good practice.

#### Step 2: Create Items for all raw materials 

1. Say No to ‘Allow Bill of Materials’. Items like jute handle and jute cloth are raw materials and are purchased not produced in-house.
1. Say Yes to ‘Is Purchase Item' since, raw material will be purchased not sold. 

__Figure 2: Raw materials__

![Raw Material](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-jute-handle-rawmaterial.png)

### Customers and Contacts

A Customer, who is sometimes known as a client, buyer, or purchaser is the one who receives goods, services, products, or ideas, from a seller for a monetary consideration. A Customer can also receive goods or services from a vendor or a Supplier for other valuable considerations. [1]

In this case-scenario, since the Items will be stocked and there is no advance Sales Order placed by a Customer , you can put your distributor/retailers details into the system. In future you will be delivering your stored products to distributors/ retailers and billing them.

> Selling > Customer > New Customer

A [Customer](/selling/customer-master) name is the name of the organisation and a Contact name is the name of the user who is coordinating.

__Figure 3: Distributor__

![Customer Master](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-distributor.png)

Customers are separate from Contacts and Addresses. Customers can have multiple Contacts and Addresses.

### Suppliers and Contacts

 [Suppliers](/buying/supplier-master) are companies or individuals who provide you with products or services. They are treated in exactly the same manner as Customers. [2]

> Buying > Supplier > New Supplier

Suppliers are separate from Contacts and Addresses. Suppliers can have multiple Contacts and Addresses.

__Figure 4: Supplier__
![Supplier Master](/assets/manual_erpnext_com/old_images/erpnext/m-t-s-supplier.png)

Before making the Price List , make the Bill of Materials based on your design document.

Next: [Bill of Material](/guide-books/make-to-stock/bill-of-materials)

---

References

1. [Wikipedia: Customer](http://en.wikipedia.org/wiki/Customer)
1. [Business Dictionary: Supplier](http://www.businessdictionary.com/definition/supplier.html)