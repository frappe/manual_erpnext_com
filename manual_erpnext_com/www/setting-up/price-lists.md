ERPNext lets you maintain multiple selling and buying prices for an Item using Price Lists. A PriceList is a name you can give to a set of Item prices. 

Why would you want Price Lists? You have different prices for different zones (based on the shipping costs), for different currencies etc.

An Item can have multiple prices based on customer, currency, region, shipping cost etc, which can be stored as different rate plans. In ERPNext, you are required to store all the lists separately. Buying Price List is different from Selling Price List and thus is stored separately.

Standard Buying and Selling Price List are created by default.

Step to create Price List.

Step 1: Go to

> Selling/Buying/Stock  > Setup > Price List >> New

Step 2: Enter name of new Price List.

![Price List Name](assets/erpnext_org/images/erpnext/price-list-name.png)

Step 3: Select Currency

Select Currency for this Price List. Currency option in Price List allows you to maintain item's price in Currency other than your companies base currency.

![Price List Currency](assets/erpnext_org/images/erpnext/price-list-currency.png)	

Step 4: Select Buying and Selling

Select for which transaction this Price List is application. Mostly it will be one of the Buying or Selling, however you can choose both as well.

![Price List For](assets/erpnext_org/images/erpnext/price-list-for.png)

Step 5: Select Territory

Select Territory for which this Price List will be applicable.

![Price List Terriory](assets/erpnext_org/images/erpnext/price-list-territory.png)

Step 6: Save Price List.

These Price List will be used when creating Item Price record to track selling or buying price of an item. Click here to learn more about Item Price.

To disable specific Price List, uncheck Enabled field in it. Disabled Price List will not be availale for selection in the Sales and Purchase transactions.