SELECT COUNT(TrackId) AS TotalTracks
FROM Track
WHERE Composer IS NOT NULL;

SELECT COUNT(TrackId) AS TotalTracks
FROM Track
WHERE Composer IS NOT NULL
AND Milliseconds > 300000;

SELECT COUNT(TrackId) AS TotalTracks, MAX(PlaylistId) AS LargestPlaylist
FROM PlaylistTrack

SELECT DISTINCT(Artist.Name), COUNT(Track.TrackId)
FROM Artist
JOIN Album
    USING(ArtistId)
JOIN Track
    USING(AlbumId)