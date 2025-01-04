PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER,
            rating REAL
        );
INSERT INTO movies VALUES(13,'Džons Viks 4','Action Epic, Gun Fu, One-Person Army Action, Action, Crime, Thriller, Back to top',NULL,NULL);
INSERT INTO movies VALUES(14,'Tumšais bruņinieks','Action Epic, Epic, Superhero, Action, Crime, Drama, Thriller, Back to top',NULL,NULL);
INSERT INTO movies VALUES(15,'Gredzenu pavēlnieks: Gredzena brālība','Adventure Epic, Epic, Fantasy Epic, Quest, Sword & Sorcery, Adventure, Drama, Fantasy, Back to top',NULL,NULL);
INSERT INTO movies VALUES(16,'Gladiators','Action Epic, Adventure Epic, Epic, Period Drama, Sword & Sandal, Action, Adventure, Drama, Back to top',NULL,NULL);
INSERT INTO movies VALUES(17,'Atriebēji: Bezgalības karš','Space Sci-Fi, Superhero, Action, Adventure, Sci-Fi, Back to top',NULL,NULL);
INSERT INTO movies VALUES(18,'Džokers','Psychological Drama, Psychological Thriller, Tragedy, Crime, Drama, Thriller, Back to top',NULL,NULL);
/****** CORRUPTION ERROR *******/
ROLLBACK; -- due to errors
