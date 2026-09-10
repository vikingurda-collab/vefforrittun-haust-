CREATE table games (
    game_id integer primary key,
    name text
);

insert into games(name);

values 
    ("minecraft"), 
    ("dark souls"), 
    ("hollow knight"),
    ("animal crossing");

select * from games;

select name as "Tölvuleikur" from games order by name;