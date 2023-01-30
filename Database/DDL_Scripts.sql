
DROP TABLE IF EXISTS USER
DROP TABLE IF EXISTS TURF
DROP TABLE IF EXISTS BOOKING

CREATE TABLE USER (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR2 NOT NULL, PASSWORD VARCHAR2 NOT NULL, USER_TYPE VARCHAR2 NOT NULL, IS_ACTIVE INT NOT NULL);
CREATE TABLE TURF (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR2 NOT NULL, LOCATION VARCHAR2 NOT NULL, BOOKING_RATE NUMBER, MANAGER_ID  REFERENCES USER(ID), IS_ACTIVE INT NOT NULL);
CREATE TABLE BOOKING (ID INTEGER PRIMARY KEY AUTOINCREMENT, TURF_ID REFERENCES TURF(ID), USER_ID REFERENCES USER(ID), STATUS VARCHAR2 NOT NULL, START_TIME VARCHAR NOT NULL, DURATION INT NOT NULL, COST NUMBER);

INSERT INTO USER VALUES (1,'admin','admin','ADMIN',1);
--INSERT INTO USER VALUES (2,'m','m','MANAGER',1);
--INSERT INTO TURF VALUES(1,'t','t',45,1,1);
--INSERT INTO TURF VALUES(2,'t2','t2',35,NULL,1);
COMMIT
