DROP DATABASE IF EXISTS warrior_db;
CREATE DATABASE warrior_db;
USE warrior_db;

CREATE TABLE arenas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    arena_name VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE warriors(
    id INT AUTO_INCREMENT PRIMARY KEY,
    war_name VARCHAR(50),
    health INT,
    attack_max INT,
    block_max INT
);

CREATE TABLE fights(
    id INT AUTO_INCREMENT PRIMARY KEY,
    winner_id INT,
    loser_id INT,
    arena_id INT,
    FOREIGN KEY(winner_id) REFERENCES warriors(id),
    FOREIGN KEY(loser_id) REFERENCES warriors(id),
    FOREIGN KEY(arena_id) REFERENCES arenas(id)
);
