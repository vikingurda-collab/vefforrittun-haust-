/*Fyrsta verkefni*/
SELECT FirstName, LastName, Customerid, Country 
FROM Customer where Country != "USA"

/*Verkefni 2*/
SELECT FirstName, LastName, Country 
FROM Customer WHERE Country = "Brazil"

/*Verkefni 4*/
SELECT FirstName, LastName, Title
FROM Employee WHERE Title = "Sales Support Agent"

/*Verkefni 5*/
SELECT DISTINCT BillingCountry
FROM Invoice

/*Verkefni 8*/
SELECT COUNT(*) InvoiceDate 
FROM Invoice 
WHERE InvoiceDate LIKE "2009-%" OR InvoiceDate LIKE "2011-%"

/*Verkefni 9*/
SELECT substr(InvoiceDate, 1, 4) AS Year, SUM(Total)
FROM Invoice
WHERE InvoiceDate LIKE '2009-%' OR InvoiceDate LIKE '2011-%'
GROUP BY substr(InvoiceDate, 1, 4);

/*Verkefni 10*/
SELECT COUNT(*) FROM InvoiceLine
WHERE InvoiceId = 37

/*Verkefnii 11*/
SELECT COUNT(InvoiceId)
FROM InvoiceLine
GROUP BY InvoiceId

/*Verkefni 14*/
SELECT BillingCountry, COUNT(InvoiceId)
FROM Invoice
GROUP BY BillingCountry