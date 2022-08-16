# effective-bassoon

## List of ISINS subject to investment ban under U.S. / EU sanctions

This is a repository of Russian ISINs that are subjec to an investment ban under [Executive Order 14071](https://home.treasury.gov/system/files/126/14071.pdf). Under the Order, the Office of Foreign Assets Control (OFAC) has indicated that U.S. persons are prohibited from purchasing any Russian securities such as debt and equity.

This repository contains sample code for curating a bespoke dataset that can be used to enhance due diligence. 

### What is an ISIN?

These are unique 12 character alpha-numeric codes that uniquely identify securities. The first two letters of an ISIN code usually represents the jursidiction where a particular stock or bond was issued, For Russia securities, this two letter code is "RU". 

# Source

The code scrapes data from the NSD, the National Settlement Depository (NSD). The NSD is responsible for assigning ISINs issued within Russia. It is also [sanctioned by the European Union](https://ec.europa.eu/info/sites/default/files/business_economy_euro/banking_and_finance/documents/faqs-sanctions-russia-central-securities-depositories_en.pdf)

# What was found?

~ [25,000 ISINs] were identified.

# What else was found?

The type of data uncovered from the full NSD dataset was rich in identifiers. For instance:

"Новости о присвоении кодов 28.09.09О присвоении  кода акциям обыкновенным   ОАО "ИнтерТрейдИнвест"Закрытое акционерное общество "Национальный депозитарный центр" извещает о присвоении 28 сентября 2009 года международного идентификационного кода  нижеперечисленным ценным бумагам:Открытое акционерное общество "ИнтерТрейдИнвест"Акции обыкновенные  Номинальная стоимость каждой ценной бумаги- 100.00Валюта номинала- Рубли код- 000089

"News on assignment of codes 28.09.09About assignment of a code to shares of ordinary JSC "InterTradeInvest" Closed Joint Stock Company "National Depositary Center" announces the assignment on September 28, 2009 of an international identification code to the following securities: Open Joint Stock Company "InterTradeInvest" Ordinary shares Nominal value of each valuable paper - 100.00 face value - ruble code - 000089

Given any subsequent issued by InterTradeInvest would now be subject to U.S. restrictions and EU restrictions, identifying and blocking such securities is required. The data, which spans over a decade can be mined to identify subsquent issuers, or even related entities. 


[25,000 ISINs]: http://www.reddit.com](https://github.com/DtorrX/effective-bassoon/blob/main/master_list.csv
