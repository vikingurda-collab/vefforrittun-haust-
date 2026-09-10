CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    gun TEXT DEFAULT 'help me',
    health INTEGER CHECK (health > 150),
);

INSERT INTO classes (name, gun, health) VALUES
('Scout','scattergun', 125),
('Soldier', 'Rocket Launcher', 200),
('Pyro', 'Flamethrower', 175),
('Demoman', 'Grenade Launcher', 175),
('Heavy', 'Minigun', 300),
('Engineer', 'Shotgun', 125),
('Medic', 'Medi Gun', 150),
('Sniper', 'Sniper Rifle', 125),
('Spy', 'Revolver', 125);

SELECT name, gun, health
FROM classes;

Select name as "Class Name", gun as 
"Primary Weapon", health as "Health Points"
from classes
where health >= 200
order by health desc;
