--
-- Project: Tournament Planner
--
-- tournament.sql - psql statements for 'create table' and 'create view'
--                  use in keeping track of players and matches in a
--                  Swiss-system game tournament.
--

--
-- Table definitions:
--

--
-- Create and connect to database
--
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

--
-- Create players table
--

DROP TABLE IF EXISTS PLAYERS CASCADE;  -- drop table + dependable objects(views)
CREATE TABLE PLAYERS (
  id serial PRIMARY KEY,            -- player id, autoincrementing
  name text                         -- player name
);

--
-- Create matches table
--

DROP TABLE IF EXISTS MATCHES CASCADE;
CREATE TABLE MATCHES (
  match_id serial PRIMARY KEY,
  winner INT REFERENCES PLAYERS(id),    -- foreign key referencing players id
  loser INT REFERENCES PLAYERS(id)      -- same here
);

--
-- Create standings view
-- Calculate number of wins
-- Calculate number of matches
--

CREATE VIEW STANDINGS AS
SELECT PLAYERS.id,
       PLAYERS.name,
       (SELECT count(*) FROM MATCHES WHERE PLAYERS.id = winner) AS wins,
       (SELECT count(*) FROM MATCHES WHERE PLAYERS.id IN (winner, loser)) AS matches
FROM PLAYERS
GROUP BY PLAYERS.id;
