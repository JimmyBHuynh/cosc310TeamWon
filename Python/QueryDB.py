
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
        return result.single()[0]

test = HelloWorldExample("bolt://localhost:7687","neo4j","test");

#test.run_Query("CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'}) " );
test.run_Query("MATCH (n) DETACH DELETE n ");

data = "CREATE (Canucks:Team {Name:'Canucks', Season:'2017/2018', gamesPlayed:65, wins:24, losses:32 , ties:0}) CREATE (Flames:Team {Name: 'Flames',Season:'2017/2018', gamesPlayed:66, wins:32, losses:25 , ties:0}) CREATE (MapleLeafs:Team {Name: 'Maple Leafs', Season:'2017/2018', gamesPlayed:67, wins:39, losses:21 , ties:0}) aaCREATE (Leipsic:Player {Name:'Brendan Leipsic', gamesPlayed:2, goals:0, assists:2 }) CREATE (Vanek:Player {Name:'Thomas Vanek', gamesPlayed:61, goals:17, assists:24 }) CREATE (Leipsic:Player {Name:'Alex Biega', gamesPlayed:31, goals:0, assists:6 })");
 test.run_Query(data);

