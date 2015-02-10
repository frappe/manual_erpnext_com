At the heart of the Manufacturing system is the **Bill of Materials** (BOM).
The **BOM** is a list of all materials (either bought or made) and operations
that go into a finished product or sub-Item. In ERPNext, the component could
have its own BOM hence forming a tree of Items with multiple levels.

To make accurate Purchase Requests, you must always maintain correct BOMs. To
make a new BOM:

> Manufacturing > Bill of Materials > New BOM

#### Figure 1: Select Item

![Bill of Materials](assets/erpnext_org/images/erpnext/bom.png)

In the BOM form:

  * Select the Item for which you want to make the BOM.
  * Add the operations that you have to go through to make that particular Item in the “Operations” table. For each operation, you will be asked to enter a Workstation. You must create new Workstations as and when necessary. 

#### Figure 2: Select Operations-Optional

![Bill of Materials with Operations](assets/erpnext_org/images/erpnext/mfg-bom-3.png)

  * Add the list of Items you require for each operation, with its quantity. This Item could be a purchased Item or a sub-assembly with its own BOM. If the row Item is a manufactured Item and has multiple BOMs, select the appropriate BOM.   You can also define if a part of the Item goes into scrap.

Workstations are defined only for product costing purposes not inventory.
Inventory is tracked in Warehouses not Workstations.

> The “Full BOM” section will list all the Items of that BOM right up to the
lower most child node. This table is automatically updated if any of the BOMs
of the sub-Items are updated.

To see an example of a Bill of Material in detail visit [](/guide-books/make-to-order/bill-of-materials)

> Note : In order to generate a Bill of Materials it is necessary that the Item is checked for "Allow Bill of Materials". The Item should also say 'Yes' to "Allow Production Order" on the Item form.

BOM -Exploded: The 'Materials Required [Exploded]' field will contain the raw materials required by the BOM. It mentions the BOM's Item-Code, Description, Quantity and Rate.
