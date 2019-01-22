#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=testdb")

def db_execute(statement, params=False):
    '''
     A helper function for statements that do not return anything
    Args:
      statement: the sql statement to be executed
      params: the parameters of the statement
    '''
    db = connect()
    cursor = db.cursor()
    cursor.execute(statement, params)
    db.commit()
    db.close()

def db_fetch_one(query, params=False):
    '''
    A helper function for queries returning one result
    Args:
      query: the sql statement to be executed
      params: the parameters of the query
    Returns:
      The first value of the first row returned from the query.
    '''
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()[0]
    db.close()
    return result

def db_fetch_all(query, params=False):
    '''
    A helper function for queries that return a result set
    Args:
      query: the sql statement to be executed
      params: the parameters of the query
    Returns:
      A list of tuples, All rows returned from the query.
    '''
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    db.close()
    return results


def deleteMatches():
    """Remove all the match records from the database."""
    db_execute("DELETE FROM MATCHES;")


def deletePlayers():
    """Remove all the player records from the database."""
    db_execute("DELETE FROM PLAYERS;")


def countPlayers():
    """Returns the number of players currently registered."""
    return db_fetch_one("SELECT COUNT(*) FROM PLAYERS;")


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    clean_name = bleach.clean(name)
    db_execute("insert into PLAYERS (name) values (%s);", (clean_name,))


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
    return db_fetch_all("SELECT * FROM STANDINGS \
                         ORDER BY wins DESC, matches ASC;")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_execute("INSERT INTO MATCHES (winner, loser) VALUES (%s, %s);",
               (winner, loser))


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
    num_players = len(standings)
    pairings = []

    for player in range(0, num_players, 2):
        pair = ((standings[player][0], standings[player][1],
                standings[player + 1][0], standings[player + 1][1]))
        pairings.append(pair)
    return pairings
