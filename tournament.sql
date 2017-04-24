-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop table/db if it already exists;
DROP DATABASE IF EXISTS tournament;

--Tournament database
CREATE DATABASE tournament;
\connect tournament;

-- Players table
CREATE TABLE players (
    player_id SERIAL primary key, 
    player_name text
    );

-- Matches table
CREATE TABLE matches (
    match_id SERIAL primary key, 
    winner SERIAL references players(player_id), 
    loser SERIAL references players(player_id)
    );

-- Total matches per player view
CREATE OR REPLACE VIEW total_view AS
SELECT players.player_id, COUNT(matches.*) AS total_matches
FROM players LEFT JOIN matches
ON players.player_id = matches.winner OR players.player_id = matches.loser
GROUP BY players.player_id;