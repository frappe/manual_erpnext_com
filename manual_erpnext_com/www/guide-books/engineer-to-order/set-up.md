# Setting Up

<p class="lead"> In an engineer-to-order system, the products are manufactured based on the client's product requirements followed by their Sales Order. To begin this order cycle, it is essential to create an Item master along with raw materials and sub assemblies, Warehouse, Customers, and Suppliers.</p>

### Customer

> Selling > Customer > New Customer

A Customer, who is sometimes known as a client, buyer, or purchaser is the one who receives goods, services, products, or ideas, from a seller for a monetary consideration. A Customer can also receive goods or services from a vendor or a Supplier for other valuable considerations. [1]

In this case-example, the [Customer](/selling/customer-master) is Ms. Jane Dsouza. She is keen on making a multipurpose bed for her daughter.

__Figure 1: Customer__

![Customer](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-jane-dsouza.png)

After setting up the Customer name in the system, it is time to create an Item based on the requirement of the Customer. In this example, the Customer Ms. Jane Dsouza wants a baby bed with a wardrobe attached to it. Thus, create an  Item, and the possible raw materials that will go into its making.

### Item

An [Item](/stock/item-master) is your company's product or a service. The term Item is applicable to your core products as well as your raw materials. It can be a product or service that you buy/sell from your Customers/Suppliers. ERPNext allows you to manage all sorts of Items like raw-materials, sub-assemblies, finished goods, Item variants and service Items.

> Stock > Item > New Item

__Figure 2: Item__

![Item](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-item-child-bed-baby.png)

Make Items for all the raw materials that will go into the final product. Let us call the final product as Child Bed Baby. The raw materials required will be wood, plywood, fevicol, hinges, nails, beadings, slotted angles, foam, wooden panels, sponge, coir, paint etc. The raw materials will also be created as Items. However, their Item Group will be raw materials.

In E-T-O type of manufacturing, you can store milestones as Items. For example, the baby-bed cum wardrobe custom order requires one bed, one wardrobe and 5 drawers. So the Item-milestones can be bed, wardrobe and drawers individually. The final product will be a result of assembling these milestone Items.

### Item Codification

Item Codification helps in keeping a count of long and and complicated names. It is preferred if you have lots of products.

In this example, lets make Bbed-1 as one product milestone, Bwardrobe-1 as another and Bdrawer-1 as the last milestone product. Note that B stands for the Baby range, then comes the name of the Item along with the order no in this category. The product is codified so that there is no confusion with other orders. The completed and assembled Item will be ‘Child Bed Baby’.

__Figure 3: Item Code__

![Item Code](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-item-codes.png)



### Sub-assembly
An assembled unit forming a component to be incorporated into a larger assembly is known as a Sub-assembly. To produce an Item , you require a lot of raw-materials. [2]

These raw-materials themselves have to be manufactured in some cases. Thus, along with standard raw materials, there is a requirement of raw materials with their own Bill of Materials. These raw materials have their own BOM’s and are called sub-assemblies.

__Figure 4: Sub assembly__

![Sub assembly](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-sub-assembly.png)

Note that for milestone Items like Bwardrobe1, Bbed1 and Bdrawers1,

1. ‘Allow BOM’ field should be marked as 'Yes'. They should be grouped as raw materials, since these will be produced in-house and will go into the making of the final product. The Item milestones are the sub-assemblies.
1. ‘Allow Production Order’ should be marked as 'No'. All sub-assemblies will  follow the one Production Order raised for the main product Child Bed Baby.

In this example Child Bed Baby is the final product, the Bbed1, Bwardrobe1 and Bdrawers1 are sub-assemblies.

### Warehouse

A Warehouse is a commercial building for storage of goods. Warehouses are used by manufacturers, importers, exporters, wholesalers, transport businesses, customs, etc. They are usually large plain buildings in industrial areas of cities, towns, and villages. They usually have loading docks to load and unload goods from trucks.

> Setup > Warehouse

This is a mandatory field. No Item form will be saved without a Warehouse master. In E-T-O type of company, create one Warehouse for Work-In-Progress and one for Finished Goods.

> Note: The Warehouses should be under the __'Stock-Expenses'__ category. Here the goods will be under the __parent group__ 'Stock-Expenses'. Assign these Warehouses to Items accordingly. Select Stock-Expenses under parent group section in the system. You will have to create this new Warehouses in the system. The existing work-in-progress and finished goods Warehouses are by default categorised under __'Assets'__ by the system. For E-T-O transactions, the finished goods will come under the expense category. Thus, create new Warehouses under Stock-Expenses category.

__Figure 5: Warehouse__

![Warehouse](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-warehouse-expense.png)

__Note :__ In reality you may not have three Warehouses. You may have only one, which you use for raw material, for manufacturing/stitching/producing and also for storing finished goods. In this case, you have to only imagine separate spaces for each activity, and name them accordingly. For system entry purpose, having three different Warehouses for stocking raw materials, manufacturing unfinished goods and storing finished goods is a necessity.

### Suppliers and Contacts

 [Suppliers](/buying/supplier-master) are companies or individuals who provide you with products or services. They are treated in exactly the same manner as Customers. [2]

> Buying > Supplier > New Supplier

Suppliers are separate from Contacts and Addresses. Suppliers can have multiple Contacts and Addresses.

__Figure 6: Supplier__

![Supplier Master](/assets/manual_erpnext_com/old_images/erpnext/e-t-o-supplier-rk-hardware.png)

Make the Bill of Materials based on your design document and product requirements specified by the client.

Next: [Bill of Material](/guide-books/engineer-to-order/bill-of-material)

---

References

1. [Wikipedia: Customer](http://en.wikipedia.org/wiki/Customer)
1. [The Free Dictionary: Sub-assembly](http://www.thefreedictionary.com/subassembly)
1. [Business Dictionary: Supplier](http://www.businessdictionary.com/definition/supplier.html)
