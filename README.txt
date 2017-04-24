# Tournament Results

This project contains the code to generate, run and test a Swiss-style
tournament results database. A Python test file has been provided to 
show how the all of the database functions work.

# Installation

Please note that you will need the following programs installed/downloaded:
1) [VirtualBox installation](https://www.virtualbox.org/wiki/Downloads)
2) [Vagrant installation](https://www.vagrantup.com/downloads)
3) [Vagrant VM Package](http://github.com/udacity/fullstack-nanodegree-vm)
4) [Git/ Git Bash](https://git-scm.com/downloads)

# Usage
Once you have completed the above, do the following:
1) Navigate to the vagrant folder inside of the cloned Vagrant VM package.
2) Open a Git Bash terminal inside of this folder.
3) Type in "vagrant up" into the command line.
4) Type in "vagrant ssh" into the command line.
5) cd into /vagrant/tournament
6) Type in "python tournament_test.py" into the command line.

If successful, you should see a success message as the bottom of the terminal.

# Building Your Own Tournament Database

1) Follow steps 1-4 in the Usage section to login to the Vagrant Virtual Machine.
2) Additionally follow step 5 to move into the tournament directory.
3) Once there, run 'psql -f tournament.sql' to create the required database.
4) Type in "python" to run the Python command line.
5) Type in "import tournament" to import the tournament database
6) Use the following commands to manipulate your database:
*Register a new Player: tournament.registerPlayer(player name)
*Report a match results: tournament.reportMatch(winner_id, loser_id)
*Get pairings: tournament.swissPairings()
*Delete all players: tournament.deletePlayers()
*Delete all matches: tournament.deleteMatches()
*Generate list of players and their wins: tournament.playerStandings()
*Delete entire database and create a new one: exit()
*** psql -f tournament.sql
