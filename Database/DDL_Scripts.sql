DROP TABLE IF EXISTS USER
DROP TABLE IF EXISTS TURF
DROP TABLE IF EXISTS BOOKING

CREATE TABLE USER (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR2 NOT NULL, PASSWORD VARCHAR2 NOT NULL, IS_ACTIVE INT NOT NULL);
CREATE TABLE TURF (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR2 NOT NULL, BOOKING_RATE NUMBER NOT NULL, IS_ACTIVE INT NOT NULL);
CREATE TABLE BOOKING (ID INTEGER PRIMARY KEY AUTOINCREMENT, TURF_ID REFERENCES TURF(ID), USER_ID REFERENCES USER(ID), STATUS INT NOT NULL, SLOT VARCHAR NOT NULL);