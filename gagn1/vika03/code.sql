CREATE TABLE nemendur (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    braut TEXT
);

INSERT INTO nemendur (name, age, braut) VALUES
('Jón', 17, 'Tölvubraut'),
('María', 21, 'Rafvirkjabraut'),
('Anna', 19, 'Sjúkraliðabraut'),
('Pétur', 15, 'Byggingabraut'),
('Kristján', 23, 'Byggingabraut'),
('Ólafur', 23, 'Byggingabraut'),
('Sigríður', 20, 'Tölvubraut'),
('Björn', 21, 'Rafvirkjabraut');

SELECT name, braut
FROM nemendur
where age <= 18;







CREATE TABLE afangar (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    credits INTEGER,
    teacher TEXT
);

INSERT INTO afangar (name, credits, teacher) VALUES
('Forritun 1', 5, 'sara'),
('vefforritun 1', 5, 'Jón'),
('Íslenska', 3, 'Anna'),
('Stærðfræði 1', 5, 'Björn'),
('Enska', 3, 'Kristín');




CREATE TABLE tolvur (
    id INTEGER PRIMARY KEY,
    tegund TEXT NOT NULL,
    styrikerfi TEXT,
    ram_gb INTEGER
);

INSERT INTO tolvur (tegund, styrikerfi, ram_gb) VALUES
('Lenovo', 'Windows', 8),
('Macbook', 'MacOS', 16),
('Dell', 'Windows', 32),
('Asus', 'Linux', 16),
('HP', 'Windows', 8);

select tegund, styrikerfi from tolvur where ram_gb >= 16
order by ram_gb desc;