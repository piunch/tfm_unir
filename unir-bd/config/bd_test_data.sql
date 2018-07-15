-- 123456
USE TFMUNIRBD;

INSERT INTO USER (USERNAME,FULLNAME,PASSWORD,CREATIONDATE) VALUES ('USUPRUEBAS','USUARIO DI PRUEBA','BA3253876AED6BC22D4A6FF53D8406C6AD864195ED144AB5C87621B6C233B548BAEAE6956DF346EC8C17F5EA10F35EE3CBC514797ED7DDD3145464E2A0BAB413',CURRENT_TIMESTAMP - INTERVAL 5 MONTH);

INSERT INTO ACCOUNT (ACCOUNTNUMBER,USERID) VALUES ('ES111122223333344445555',1);

INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,1,1000,'NOMINA',1000,CURRENT_TIMESTAMP - INTERVAL 4 MONTH);
INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,1,1000,'NOMINA',2000,CURRENT_TIMESTAMP - INTERVAL 3 MONTH);
INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,1,-500,'PAGO GAMBAS FRITAS',1500,CURRENT_TIMESTAMP - INTERVAL 2 MONTH - INTERVAL 6 DAY);
INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,1,1000,'NOMINA',2500,CURRENT_TIMESTAMP - INTERVAL 2 MONTH);
INSERT INTO TRANSACTIONS (USERID,ACCOUNTID,AMOUNT,DESCRIPTION,CURRENTBALANCE,TRANSACTIONDATE) VALUES (1,1,-750,'IMPUESTO DE CALCETINES',1750,CURRENT_TIMESTAMP - INTERVAL 6 DAY);