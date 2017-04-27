# Tournament Results

This project contains the code to generate, run and test a Swiss-style
tournament results database. A Python test file has been provided to 
show how the all of the database functions work.

# Installation

You will need to have Python, PostgreSQL, and Git installed.
You will also need to clone this repo. You can do so by entering the following command in the terminal:

git clone https://github.com/toriancrane/tournament-results-database

#### Usage

1) CD into the appropriate folder.

$ cd tournament-results-database

2) Create a clean database and tables by importing tournament.sql

$ psql
=> \i tournament.sql

Note: The program has been built to drop existing databases and create a new one for you upon import.

3) You should see the following if successful:

=> \i tournament.sql
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE

$ Exit out of psql and run the following python command to test the database functionality with the provided test script:

tournament=> \q
$python tournament_test.py

#### Building Your Own Tournament Database
1)Create a clean database and tables by importing tournament.sql

$ psql
=> \i tournament.sql

2) Exit out of psql.

tournament=> \q

3) Use the following commands to manipulate your database:

*Register a new Player: tournament.registerPlayer(player_name)
*Report a match results: tournament.reportMatch(winner_id, loser_id)
*Get pairings: tournament.swissPairings()
*Delete all players: tournament.deletePlayers()
*Delete all matches: tournament.deleteMatches()
*Generate list of players and their wins: tournament.playerStandings()
*Delete entire database and create a new one: exit()
*** psql -f tournament.sql

Feel free to use the contents of the tournament_test.py file as a helpful guide.
