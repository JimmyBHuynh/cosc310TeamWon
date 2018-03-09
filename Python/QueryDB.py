
from neo4j.v1 import GraphDatabase;

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def run_Query(self, query):
        with self._driver.session() as session:
            session.write_transaction(self._create_query, query)


    def run_Return_Query(self, query):
        with self._driver.session() as session:
            result = session.write_transaction(self._create_and_return_query, query)
            print(result)  

    @staticmethod
    def _create_query(tx, query):
        tx.run(query)

    @staticmethod
    def _create_and_return_query(tx, query):
        result = tx.run(query)
        out = result.peek()[0]
        myResults = result.records()
        #for i in myResults:
        #  print(myResults[i])
        #  out +=" " + myResults[i]
        return out

test = HelloWorldExample("bolt://localhost:7687","neo4j","test");

#test.run_Query("CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'}) " );
test.run_Query("MATCH (n) DETACH DELETE n ");

data = "CREATE(Ma :Person {name : 'Ma Dalton', female : true, size : 1.50}),(Sweetie : Animal {name : 'Sweetie', species : 'cat'}),(Rantanplan : Animal {name : 'Rantanplan', species : 'dog'}),(Joe : Person : Outlaw {name : 'Joe', bounty : 5000, size : 1.40}),(Jack : Person : Outlaw {name : 'Jack', bounty : 4000, size : 1.67}),(William :Person :Outlaw {name : 'William', bounty : 3000, size : 1.93}),(Averell :Person :Outlaw {name : 'Averell', bounty : 2, size : 2.13}),(Ma) -[:LIKES]-> (Sweetie),(Sweetie) -[:DISLIKES {because : 'fight like cat and dog'}]-> (Rantanplan),(Averell) -[:LIKES {because : 'same IQ'}]-> (Rantanplan),(Ma) -[:PARENTS {gift : 'files'}]-> (Joe),(Ma) -[:PARENTS {gift : 'weapons'}]-> (Jack),(Ma) -[:PARENTS {gift : 'books'}]-> (William),(Ma) -[:PARENTS {gift : 'food'}]-> (Averell),(Joe) -[:BROTHER]-> (Jack),(Jack) -[:BROTHER]-> (William),(William) -[:BROTHER]-> (Averell),(Joe) <-[:BROTHER]- (Jack),(Jack) <-[:BROTHER]- (William),(William) <-[:BROTHER]- (Averell)";
test.run_Query(data);
test.run_Return_Query("MATCH ( n : Person : Outlaw ) RETURN n.name")

#CREATE (Canucks:Team {Name:'Canucks', Season:'2017/2018', gamesPlayed:65, wins:24, losses:32 , ties:0}) 
#CREATE (Flames:Team {Name: 'Flames',Season:'2017/2018', gamesPlayed:66, wins:32, losses:25 , ties:0})
#CREATE (MapleLeafs:Team {Name: 'Maple Leafs', Season:'2017/2018', gamesPlayed:67, wins:39, losses:21 , ties:0})

#CREATE (Leipsic:Player {Name:'Brendan Leipsic', gamesPlayed:2, goals:0, assists:2 })
#CREATE (Vanek:Player {Name:'Thomas Vanek', gamesPlayed:61, goals:17, assists:24 })
#CREATE (Biega:Player {Name:'Alex Biega', gamesPlayed:31, goals:0, assists:6 })
#CREATE (Megna:Player {Name:'Jayson Megna', gamesPlayed:1, goals:0, assists:0 })
#CREATE (Pouliot:Player {Name:'Derrick Pouliot', gamesPlayed:54, goals:2, assists:15 })
#CREATE (Zotto:Player {Name:'Michael Del Zotto', gamesPlayed:65, goals:5, assists:13 })
#CREATE (Gudbranson:player {Name:'Erik Gudbranson', gamesPlayed:47, goals:2, assists:2 })
#CREATE (Burmistrov:player {Name:'Alexander Burmistrov', gamesPlayed:24, goals:2, assists:4 })
#CREATE (Dorsett:player {Name:'Derek Dorsett', gamesPlayed:20, goals:7, assists:2 })
#CREATE (Virtanen:player {Name:'Jake Virtanen', gamesPlayed:59, goals:7, assists:8 })
#CREATE (Gagner:player {Name:'Sam Gagner', gamesPlayed:57, goals:7, assists:16 })
#CREATE (Archibald:player {Name:'Darren Archibald', gamesPlayed:11, goals:2, assists:2 })
#CREATE (Horvat:player {Name:'Bo Horvat', gamesPlayed:47, goals:18, assists:17 })
#CREATE (Goldobin:player {Name:'Nikolay Goldobin', gamesPlayed:22, goals:4, assists:3 })
#CREATE (Hutton:player {Name:'Ben Hutton', gamesPlayed:54, goals:0, assists:6 })
#CREATE (Granlund:player {Name:'Markus Granlund', gamesPlayed:53, goals:8, assists:4 })
#CREATE (Eriksson:player {Name:'Loui Eriksson', gamesPlayed:50, goals:10, assists:10 })
#CREATE (Chaput:player {Name:'Michael Chaput', gamesPlayed:9, goals:0, assists:0 })
#CREATE (Stecher:player {Name:'Troy Stecher', gamesPlayed:51, goals:1, assists:8 })
#CREATE (Holm:player {Name:'Philip Holm', gamesPlayed:1, goals:0, assists:0 })
#CREATE (Boeser:player {Name:'Brock Boeser', gamesPlayed:61, goals:29, assists:26 })
#CREATE (Edler:player {Name:'Alexander Edler', gamesPlayed:53, goals:2, assists:24 })
#CREATE (Sutter:player {Name:'Brandon Sutter', gamesPlayed:44, goals:6, assists:11 })
#CREATE (Tanev:player {Name:'Christopher Tanev', gamesPlayed:38, goals:2, assists:9 })
#CREATE (Baertschi:player {Name:'Sven Baertschi', gamesPlayed:53, goals:14, assists:14 })
#CREATE (Boucher:player {Name:'Reid Boucher', gamesPlayed:8, goals:2, assists:0 })
#CREATE (SedinH:player {Name:'Henrik Sedin', gamesPlayed:65, goals:2, assists:41 })
#CREATE (Guance:player {Name:'Brendan Gaunce', gamesPlayed:34, goals:4, assists:1 })
#CREATE (SedinS:player {Name:'Daniel Sedin', gamesPlayed:64, goals:21, assists:25 })
#CREATE (Dowd:player {Name:'Nic Dowd', gamesPlayed:29, goals:2, assists:0})
#CREATE (Motte:player {Name:'Tyler Motte', gamesPlayed:2, goals:0, assists:0})

#CREATE (Gaudreau:Player {Name:'Johnny Gaudreau', gamesPlayed:67, goals:20, assists:54 })
#CREATE (Monahan:Player {Name:'Sean Monahan', gamesPlayed:66, goals:29, assists:29 })
#CREATE (Tkachuk:Player {Name:'Matthew Tkachuk', gamesPlayed:65, goals:24, assists:25 })
#CREATE (Backlund:Player {Name:'Mikael Backlund', gamesPlayed:67, goals:13, assists:28 })
#CREATE (Hamilton:Player {Name:'Dougie Hamilton', gamesPlayed:67, goals:14, assists:24 })
#CREATE (Ferland:Player {Name:'Micheal Ferland', gamesPlayed:62, goals:20, assists:14 })
#CREATE (Giordano:Player {Name:'Mark Giordano', gamesPlayed:67, goals:11, assists:22 })
#CREATE (Brodie:Player {Name:'TJ Brodie', gamesPlayed:67, goals:4, assists:26 })
#CREATE (Frolik:Player {Name:'Michael Frolik', gamesPlayed:55, goals:10, assists:13 })
#CREATE (Bennett:Player {Name:'Sam Bennett', gamesPlayed:67, goals:9, assists:14 })
#CREATE (Brouwer:Player {Name:'Troy Brouwer', gamesPlayed:61, goals:5, assists:14 })
#CREATE (Jankowski:Player {Name:'Mark Jankowski', gamesPlayed:58, goals:11, assists:7 })
#CREATE (Hathaway:Player {Name:'Garnet Hathaway', gamesPlayed:44, goals:2, assists:8 })
#CREATE (Hamonic:Player {Name:'Travis Hamonic', gamesPlayed:63, goals:1, assists:9 })
#CREATE (Stajan:Player {Name:'Matt Stajan', gamesPlayed:57, goals:3, assists:6 })
#CREATE (Versteeg:Player {Name:'Kris Versteeg', gamesPlayed:3, goals:5, assists:9 })
#CREATE (Lazar:Player {Name:'Curtis Lazar', gamesPlayed:50, goals:2, assists:5 })
#CREATE (Kulak:Player {Name:'Brett Kulak', gamesPlayed:56, goals:2, assists:5 })
#CREATE (Jagr:Player {Name:'Jaromir Jagr', gamesPlayed:22, goals:1, assists:6 })
#CREATE (Stone:Player {Name:'Michael Stone', gamesPlayed:67, goals:2, assists:3 })
#CREATE (Lomberg:Player {Name:'Ryan Lomberg', gamesPlayed:7, goals:0, assists:1 })
#CREATE (Hamilton:Player {Name:'Freddie Hamilton', gamesPlayed:8, goals:0, assists:1 })
#CREATE (Bartkowski:Player {Name:'Matt Bartkowski', gamesPlayed:14, goals:0, assists:1 })
#CREATE (Hrivik:Player {Name:'Marek Hrivik', gamesPlayed:3, goals:0, assists:0 })
#CREATE (Stewart:Player {Name:'Chris Stewart', gamesPlayed:2, goals:0, assists:0 })
#CREATE (Shore:Player {Name:'Nick Shore', gamesPlayed:1, goals:0, assists:0 })
#CREATE (Klimchuk:Player {Name:'Morgan Klimchuk', gamesPlayed:1, goals:0, assists:0 })
#CREATE (Andersson:Player {Name:'Rasmus Andersson', gamesPlayed:1, goals:0, assists:0 })
#CREATE (Mangiapane:Player {Name:'Andrew Mangiapane', gamesPlayed:10, goals:0, assists:0 })
#CREATE (Glass:Player {Name:'Tanner Glass', gamesPlayed:9, goals:0, assists:0 })


