# Setting Up

<p class="lead">In a make-to-order system, the products are pre-defined. To begin the order cycle, it is essential to create an Item master, Customers, and Suppliers.</p>

### Item

An [Item](/stock/Item-master) is your company's product or a service. The term Item is applicable to your core products as well as your raw materials. It can be a product or service that you buy/sell from your customers/ suppliers. ERPNext allows you to manage all sorts of Items like raw-materials, sub-assemblies, finished goods, Item variants and service Items.

> Stock > Item > New Item

#### Step 1: Create an Item "Jute Pen Stand"

Since Jute Pen Stand is a sales Item, it is grouped as a 'Product’. The material that goes into making of this product like jute wire and fabric paint will also be called Item. However, the Item Group of jute wire and fabric paint will be termed as raw-material.

**Figure 1: Item**

![Item](/assets/erpnext_org/images/erpnext/m-t-s-item.png)

1. Click Yes on ‘Allow Bill of Materials’, 
1. Click Yes on ‘Allow Production Order’ and 
1. Click No on  ‘Is Purchase Item’.

> **Tip:** Please mention the  Default Warehouse for this Item as “Finished Goods”. This product is available at the Finished Goods Warehouse only after it gets manufactured at the Work-in-Progress Warehouse. It cannot be kept in stores, because it is not purchased, it is manufactured.

**Note on Warehouses:** In reality you may not have three Warehouses. You may have one, which you use for raw materials, for manufacturing/stitching/producing and also for storing finished goods. In such cases, you have to only imagine separate spaces for each activity, and name them accordingly. For system entry purpose, having three different Warehouses for stocking raw materials, manufacturing unfinished goods and storing finished goods is a good practice.

#### Step 2: Create Items for all raw materials

1. Mention Item Group as Raw Material,
1. Click No on ‘Allow Bill of Materials’ (since BOM is required only for products), unless you produce raw-materials in-house.
1. Click No on Allow Production Order, and
1. Click Yes on ‘Is Purchase Item’.

**Figure 2: Item Jute-wire as raw material**

![Jute Wire](/assets/erpnext_org/images/erpnext/m-t-o-jute-wire-rawmaterial.png)

Following is the list of raw materials that will go into making of a Jute Pen-Stand.

1. Fabric Colour
1. Jute Wire
1. Tree Glue

Make a Bill of Materials with the help of these raw materials.

**Figure 3: Item List**

![Item List](/assets/erpnext_org/images/erpnext/m-t-o-item-list.png)



### Customers and Contacts

A Customer, who is sometimes known as a client, buyer, or purchaser is the one who receives goods, services, products, or ideas, from a seller for a monetary consideration. A Customer can also receive goods or services from a vendor or a Supplier for other valuable considerations. [1]

> Selling > Customer > New Customer

A [Customer](/selling/customer-master) name is the name of the organisation and a Contact name is the name of the user who is coordinating.

![Customer Master](/assets/erpnext_org/images/erpnext/customer.png)

Customers are separate from Contacts and Addresses. Customers can have multiple Contacts and Addresses.

### Suppliers and Contacts

 [Suppliers](/buying/supplier-master) are companies or individuals who provide you with products or services. They are treated in exactly the same manner as Customers. [1]

> Buying > Supplier > New Supplier

![Supplier Master](/assets/erpnext_org/images/erpnext/supplier.png)

Before making the Price List and the Sales Order, make the Bill of Materials based on your design document.

Next: [Bill of Material](/guide-books/make-to-order/bill-of-materials)

---

References

1. [Wikipedia: Customer](http://en.wikipedia.org/wiki/Customer)
1. [Business Dictionary: Supplier](http://www.businessdictionary.com/definition/supplier.html)