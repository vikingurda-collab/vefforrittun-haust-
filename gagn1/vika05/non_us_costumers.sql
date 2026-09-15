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
WHERE InvoiceDate LIKE 2009 AND InvoiceDate LIKE 2011