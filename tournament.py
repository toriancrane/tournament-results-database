#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM matches')
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM players')
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT count(player_id) from players')
    player_count = c.fetchone()[0]
    db.close()
    return player_count



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    clean_name = bleach.clean(name)
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO players (player_name) VALUES (%s)', (clean_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    sql = ("select player_id, player_name, "
	       "(select count(*) from matches where matches.winner = players.player_id) as wins, "
	       "(select count(*) from matches where matches.winner = players.player_id "
                                        "or matches.loser = players.player_id) as total_matches "
			"from players "
			"order by wins desc")
    c.execute(sql)
    results = c.fetchall()
    db.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    clean_winner = bleach.clean(winner)
    clean_loser = bleach.clean(loser)
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO matches (winner, loser) '
              'VALUES (%s, %s)', (clean_winner, clean_loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    length = len(standings)
    pairings = []

    x = 0
    while(x < length):
        id1 = standings[x][0]
        name1 = standings[x][1]
        id2 = standings[x + 1][0]
        name2 = standings[x + 1][1]
        pairings.append((id1, name1, id2, name2))
        x += 2
    return pairings


