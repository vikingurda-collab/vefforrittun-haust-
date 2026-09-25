/*Fyrsta verkefni*/
SELECT FirstName, LastName, Customerid, Country 
FROM Customer where Country != "USA"

/*Verkefni 2*/
SELECT FirstName, LastName, Country 
FROM Customer WHERE Country = "Brazil"

/*Verkefni 3*/
SELECT FirstName, LastName, InvoiceId, InvoiceDate, BillingCountry
FROM Customer
JOIN Invoice
    USING(CustomerId)
WHERE BillingCountry = "Brazil"

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

/*Verkefni 12*/
SELECT Name
FROM Track
JOIN InvoiceLine
    USING (TrackId)

/*Verkefni 13*/
SELECT
    InvoiceLine.InvoiceLineId,
    Track.Name,
    Artist.Name
FROM InvoiceLine
JOIN Track
    ON Track.TrackId = InvoiceLine.TrackId
JOIN Album
    ON Album.AlbumId = Track.AlbumId
JOIN Artist
    ON Artist.ArtistId = Album.ArtistId

/*Verkefni 14*/
SELECT BillingCountry, COUNT(InvoiceId)
FROM Invoice
GROUP BY BillingCountry

/*Verkefni 15*/
SELECT COUNT(TrackId), Playlist.Name
FROM Track
JOIN PlaylistTrack
    USING (TrackId)
JOIN Playlist
    USING (PlaylistId)
GROUP BY Playlist.Name

/*Verkefni 16*/
SELECT Track.Name, Album.Title, MediaType.Name, Genre.Name
FROM Track
JOIN Album
    USING (AlbumId)
JOIN MediaType
    USING (MediaTypeId)
JOIN Genre
    USING (GenreId)

/*Verkefni 17*/
SELECT InvoiceId, COUNT(InvoiceLineId)
FROM Invoice
JOIN InvoiceLine
    USING(InvoiceId)
GROUP BY InvoiceId

/*Verkefni 18*/
SELECT Employee.EmployeeId, SUM(Invoice.Total)
FROM Invoice
JOIN Customer
    USING (CustomerId)
JOIN Employee
    ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY Employee.EmployeeId

/*Verkefni 19*/
SELECT Employee.FirstName, Employee.LastName, Employee.Title,
SUM(InvoiceLine.Quantity),  Invoice.InvoiceDate
FROM Employee
JOIN Customer
    ON Customer.SupportRepId = Employee.EmployeeId
JOIN Invoice
    USING (CustomerId)
JOIN InvoiceLine
    USING (InvoiceId)
WHERE Invoice.InvoiceDate LIKE "%2009%"
GROUP BY Employee.LastName

/*Verkefni 20*/
SELECT Employee.FirstName, Employee.LastName, Employee.Title,
SUM(InvoiceLine.Quantity)
FROM Employee
JOIN Customer
    ON Customer.SupportRepId = Employee.EmployeeId
JOIN Invoice
    USING (CustomerId)
JOIN InvoiceLine
    USING (InvoiceId)
GROUP BY Employee.LastName

/*Verkefni 21*/
SELECT Employee.FirstName, Employee.LastName, Employee.Title, 
Sum(Customer.CustomerId)
FROM Employee
JOIN Customer
    ON Customer.SupportRepId = Employee.EmployeeId
GROUP BY Employee.FirstName