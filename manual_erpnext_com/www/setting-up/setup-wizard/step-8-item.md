# Step 8: Item Names

In this final step, please enter the names of the Items you buy or sell.

![Item Names](/assets/erpnext_org/images/setup-wizard/setup-wizard-8.png)

---

#### Difference between a Product and a Service

A Product is something that is made and sold. It is something produced by human or mechanical effort or by a natural process. It is a tangible commodity.

Service is an intangible commodity. Services have little or no tangible components and therefore cannot be stored for a future use. Services are produced and consumed during the same period of time.

For Example: Amongst pens, laptops, laptop maintenance, banking, hoteling, distributing and jute bags, products are - pens, laptops and Jute Bags. Services are - laptop maintenance, banking, hoteling and distributing.

### Sub-assemblies

An assembled unit forming a component to be incorporated into a larger assembly is known as a Sub-assembly. To produce an Item , you require a lot of raw-materials. These raw-materials themselves have to be manufactured in some cases. Thus, along with standard raw materials, there is a requirement of raw materials with their  own Bill of Materials. These raw materials have their own BOM’s and are called sub-assemblies.

For Example: To prepare a Jute Bag,  you require Jute cloth, Jute hand woven strings, Jute decorative patchwork, fabric colour for painting, paint brush, etc. All these requirements that go into building the product Jute Bag are raw materials. However, if you are preparing the Jute decorative patchwork in-house then that patchwork will be a sub-assembly. The sub-assembly will have its own Bill of Materials stating raw material list like wool, beads and colourful frills.

Thus you should click on the sub-assembly option if you manufacture all your spare parts in-house and have  Bill of Materials within a Bill of Materials.

###  Difference beetween Raw-material and Sub-assembly?

Raw materials are materials that have not been processed. They are in the form in which they are found in nature without any thing done to them. Raw materials are made into other things.  A sub assembly is a Collection of parts put together as a unit, to be used in the making of a larger assembly or a final or higher item.

### Unit of Measure (UOM)

A unit of measurement is a property by which any object can be compared as larger or smaller than other objects of the same kind. It is used as a standard for measurement of the same physical quantity. Any other value of the physical quantity can be expressed as a simple multiple of the unit of measurement.

For example weight is a physical quantity. The Kilogram (Kg) is a unit of weight that represents a definite predetermined weight. When we say 5 kgs, we actually mean 5 times the definite predetermined weight called Kilogram(Kg)
ERPNext has some built-in UOM’s. If you have specific requirements which are not mentioned in the system, you can create your own UOM.

Go to the Setup Page and Click on UOM

> Setup > UOM > New UOM

Key-in the new UOM name and save . Note that the box that appears below UOM field, which says disallows fraction should be checked only if you wish your UOM quantity to be mentioned in whole numbers. What this means is you will be able to type 5 kgs. But if you wish to type 0.05 Kgs the field will not accept your value. Thus if you have quantities which requires you to mention the amount in fractions, then check the box.
