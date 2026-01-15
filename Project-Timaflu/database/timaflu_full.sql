-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: timaflu
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adres`
--

DROP TABLE IF EXISTS `adres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adres` (
  `adres_id` int NOT NULL AUTO_INCREMENT,
  `straatnaam` varchar(100) NOT NULL,
  `huisnummer` varchar(10) NOT NULL,
  `postcode` varchar(20) NOT NULL,
  `plaats` varchar(50) NOT NULL,
  PRIMARY KEY (`adres_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adres`
--

LOCK TABLES `adres` WRITE;
/*!40000 ALTER TABLE `adres` DISABLE KEYS */;
INSERT INTO `adres` VALUES (1,'Kruisstraat','12','1011AB','Amsterdam'),(2,'Lindelaan','45','3512CD','Utrecht'),(3,'Dorpsstraat','78','2000EF','Rotterdam'),(4,'Beukenweg','23','3012GH','Den Haag'),(5,'Stationsplein','5','1012IJ','Amsterdam'),(6,'Hofstraat','11','3013KL','Den Haag'),(7,'Noordlaan','50','2001MN','Rotterdam'),(8,'Zuidstraat','33','3513OP','Utrecht'),(9,'Oostsingel','22','1013QR','Amsterdam'),(10,'Westend','44','3514ST','Utrecht'),(11,'Molenstraat','14','1014UV','Amsterdam'),(12,'Duinstraat','7','3515WX','Utrecht'),(13,'Bergzichtlaan','3','2002YZ','Rotterdam'),(14,'Bloemstraat','18','3015AB','Den Haag'),(15,'Rivierweg','22','1015CD','Amsterdam'),(16,'Valkenstraat','27','3516EF','Utrecht'),(17,'Lijsterlaan','9','2003GH','Rotterdam'),(18,'Eikenweg','12','3016IJ','Den Haag'),(19,'Zandpad','5','1016KL','Amsterdam'),(20,'Kastanjelaan','31','3517MN','Utrecht');
/*!40000 ALTER TABLE `adres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `betaling`
--

DROP TABLE IF EXISTS `betaling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `betaling` (
  `betaling_id` int NOT NULL AUTO_INCREMENT,
  `betaaldatum` date NOT NULL,
  `bedrag` decimal(10,2) NOT NULL,
  `factuur_id` int NOT NULL,
  PRIMARY KEY (`betaling_id`),
  KEY `fk_Betaling_Factuur1_idx` (`factuur_id`),
  CONSTRAINT `fk_Betaling_Factuur1` FOREIGN KEY (`factuur_id`) REFERENCES `factuur` (`factuur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `betaling`
--

LOCK TABLES `betaling` WRITE;
/*!40000 ALTER TABLE `betaling` DISABLE KEYS */;
INSERT INTO `betaling` VALUES (1,'2026-01-11',1250.00,1),(2,'2026-01-12',500.00,2),(3,'2026-01-14',980.00,3);
/*!40000 ALTER TABLE `betaling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactpersoon`
--

DROP TABLE IF EXISTS `contactpersoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactpersoon` (
  `contactpersoon_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(200) NOT NULL,
  `telefoonnummer` char(20) NOT NULL,
  `voornaam` varchar(45) DEFAULT NULL,
  `achternaam` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`contactpersoon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactpersoon`
--

LOCK TABLES `contactpersoon` WRITE;
/*!40000 ALTER TABLE `contactpersoon` DISABLE KEYS */;
INSERT INTO `contactpersoon` VALUES (1,'peter@apotheek.nl','0612345671','Peter','Jansen'),(2,'marie@apotheek.nl','0612345672','Marie','de Vries'),(3,'klaas@apotheek.nl','0612345673','Klaas','Peters'),(4,'anna@apotheek.nl','0612345674','Anna','Smit'),(5,'rob@apotheek.nl','0612345675','Rob','Bakker'),(6,'lisette@apotheek.nl','0612345676','Lisette','Hendriks'),(7,'Niels@apotheek.nl','0634567890','Niels','Vissers'),(8,'Tom@apotheek.nl','0645678901','Tom','de Boer'),(9,'Sanne@apotheek.nl','0667890123','Sanne','samuels');
/*!40000 ALTER TABLE `contactpersoon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distributiehoek`
--

DROP TABLE IF EXISTS `distributiehoek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distributiehoek` (
  `distributie_id` int NOT NULL AUTO_INCREMENT,
  `verpakt_op` datetime DEFAULT NULL,
  `verzonden_op` datetime DEFAULT NULL,
  PRIMARY KEY (`distributie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distributiehoek`
--

LOCK TABLES `distributiehoek` WRITE;
/*!40000 ALTER TABLE `distributiehoek` DISABLE KEYS */;
INSERT INTO `distributiehoek` VALUES (1,'2026-01-10 09:00:00','2026-01-10 11:00:00'),(2,'2026-01-10 10:00:00','2026-01-10 12:00:00'),(3,'2026-01-11 09:30:00','2026-01-11 11:30:00');
/*!40000 ALTER TABLE `distributiehoek` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factuur`
--

DROP TABLE IF EXISTS `factuur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factuur` (
  `factuur_id` int NOT NULL AUTO_INCREMENT,
  `factuurdatum` date NOT NULL,
  `bedrag` decimal(10,2) NOT NULL,
  `vervaldatum` date DEFAULT NULL,
  `factuur_status` varchar(50) NOT NULL,
  PRIMARY KEY (`factuur_id`),
  KEY `fk_Factuur_Status1_idx` (`factuur_status`),
  CONSTRAINT `fk_Factuur_Status1` FOREIGN KEY (`factuur_status`) REFERENCES `factuur_status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factuur`
--

LOCK TABLES `factuur` WRITE;
/*!40000 ALTER TABLE `factuur` DISABLE KEYS */;
INSERT INTO `factuur` VALUES (1,'2026-01-10',1250.00,'2026-01-24','wordt verzameld'),(2,'2026-01-12',500.00,'2026-01-26','betaald'),(3,'2026-01-14',980.00,'2026-01-28','incasso'),(4,'2026-01-15',750.00,'2026-01-29','wordt verzameld'),(5,'2026-01-16',1200.00,'2026-01-30','betaald'),(6,'2026-01-17',560.00,'2026-01-31','incasso'),(7,'2026-01-18',850.00,'2026-02-01','open'),(8,'2026-01-19',1100.00,'2026-02-02','2e herinnering'),(9,'2026-01-20',600.00,'2026-02-03','incasso'),(10,'2026-01-21',950.00,'2026-02-04','open'),(11,'2026-01-22',1300.00,'2026-02-05','betaald'),(12,'2026-01-23',750.00,'2026-02-06','1e herinnering'),(13,'2026-01-24',1400.00,'2026-02-07','open'),(14,'2026-01-25',900.00,'2026-02-08','betaald'),(15,'2026-01-26',500.00,'2026-02-09','incasso'),(16,'2026-01-27',1250.00,'2026-02-10','open');
/*!40000 ALTER TABLE `factuur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factuur_status`
--

DROP TABLE IF EXISTS `factuur_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factuur_status` (
  `status` varchar(50) NOT NULL,
  `omschrijving` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factuur_status`
--

LOCK TABLES `factuur_status` WRITE;
/*!40000 ALTER TABLE `factuur_status` DISABLE KEYS */;
INSERT INTO `factuur_status` VALUES ('1e herinnering','Factuur 1e herinnering'),('2e herinnering','Factuur 2e herinnering'),('betaald','Factuur is betaald'),('incasso','Factuur wordt geïncasseerd'),('open','Factuur staat open'),('wordt verzameld','Factuur wordt voorbereid');
/*!40000 ALTER TABLE `factuur_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `klant`
--

DROP TABLE IF EXISTS `klant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `klant` (
  `klant_id` int NOT NULL AUTO_INCREMENT,
  `bedrijfsnaam` varchar(45) NOT NULL,
  `contactpersoon_id` int DEFAULT NULL,
  `adres_id` int NOT NULL,
  `factuuradres_id` int NOT NULL,
  `klantkorting` decimal(10,2) DEFAULT NULL,
  `status` enum('actief','geblokkeerd','potentieel') NOT NULL,
  `jaaromzet` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`klant_id`),
  KEY `fk_Klant_Adres_idx` (`adres_id`),
  KEY `fk_Klant_Adres1_idx` (`factuuradres_id`),
  KEY `fk_Klant_Contactpersoon1_idx` (`contactpersoon_id`),
  CONSTRAINT `fk_Klant_Adres` FOREIGN KEY (`adres_id`) REFERENCES `adres` (`adres_id`),
  CONSTRAINT `fk_Klant_Adres1` FOREIGN KEY (`factuuradres_id`) REFERENCES `adres` (`adres_id`),
  CONSTRAINT `fk_Klant_Contactpersoon1` FOREIGN KEY (`contactpersoon_id`) REFERENCES `contactpersoon` (`contactpersoon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klant`
--

LOCK TABLES `klant` WRITE;
/*!40000 ALTER TABLE `klant` DISABLE KEYS */;
INSERT INTO `klant` VALUES (1,'Apotheek Centraal',1,1,1,5.00,'actief',12000.00),(2,'Apotheek Zuid',2,2,2,10.00,'actief',18000.00),(3,'Apotheek Noord',3,3,3,5.00,'geblokkeerd',9000.00),(4,'Apotheek West',4,4,4,0.00,'potentieel',0.00),(5,'Apotheek Oost',5,5,5,5.00,'actief',15000.00),(6,'Apotheek Berg',6,6,6,10.00,'actief',22000.00),(7,'Apotheek Bos',NULL,7,7,5.00,'geblokkeerd',8000.00),(8,'Apotheek Valk',NULL,8,8,15.00,'actief',25000.00),(9,'Apotheek Lijster',NULL,9,9,0.00,'potentieel',0.00),(10,'Apotheek Eiken',NULL,10,10,5.00,'actief',12000.00),(11,'Apotheek Molen',NULL,11,11,5.00,'actief',13000.00),(12,'Apotheek Duin',NULL,12,12,10.00,'actief',21000.00),(13,'Apotheek Bergzicht',NULL,13,13,0.00,'potentieel',0.00),(14,'Apotheek Bloem',NULL,14,14,5.00,'actief',17000.00),(15,'Apotheek Rivier',NULL,15,15,15.00,'geblokkeerd',8000.00),(16,'Apotheek Valken',NULL,16,16,10.00,'actief',22000.00),(17,'Apotheek Lijverster',NULL,17,17,0.00,'potentieel',0.00),(18,'Apotheek Eikelen',NULL,18,18,5.00,'actief',12000.00),(19,'Apotheek Zand',NULL,19,19,5.00,'actief',14000.00),(20,'Apotheek Kastanje',NULL,20,20,10.00,'actief',20000.00);
/*!40000 ALTER TABLE `klant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `koerier_status`
--

DROP TABLE IF EXISTS `koerier_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `koerier_status` (
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `koerier_status`
--

LOCK TABLES `koerier_status` WRITE;
/*!40000 ALTER TABLE `koerier_status` DISABLE KEYS */;
INSERT INTO `koerier_status` VALUES ('beschikbaar'),('niet beschikbaar'),('onderweg'),('spoed');
/*!40000 ALTER TABLE `koerier_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leverancier`
--

DROP TABLE IF EXISTS `leverancier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leverancier` (
  `leverancier_id` int NOT NULL AUTO_INCREMENT,
  `adres_id` int NOT NULL,
  `contactpersoon_id` int NOT NULL,
  `naam` varchar(45) NOT NULL,
  `contactpersoon` varchar(100) DEFAULT NULL,
  `telefoonnummer` varchar(35) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `prijs` decimal(10,2) NOT NULL,
  `internetadres` varchar(200) NOT NULL,
  PRIMARY KEY (`leverancier_id`),
  KEY `fk_Leverancier_Adres1_idx` (`adres_id`),
  KEY `fk_Leverancier_Contactpersoon1_idx` (`contactpersoon_id`),
  CONSTRAINT `fk_Leverancier_Adres1` FOREIGN KEY (`adres_id`) REFERENCES `adres` (`adres_id`),
  CONSTRAINT `fk_Leverancier_Contactpersoon1` FOREIGN KEY (`contactpersoon_id`) REFERENCES `contactpersoon` (`contactpersoon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leverancier`
--

LOCK TABLES `leverancier` WRITE;
/*!40000 ALTER TABLE `leverancier` DISABLE KEYS */;
INSERT INTO `leverancier` VALUES (1,1,1,'MediSupply','John Doe','0611122233','john@medisupply.nl',10.50,'[www.medisupply.nl](http://www.medisupply.nl/)'),(2,2,2,'PharmaPlus','Linda Smith','0622233344','linda@pharmaplus.nl',12.00,'[www.pharmaplus.nl](http://www.pharmaplus.nl/)'),(3,3,3,'HealthCorp','Mark Johnson','0633344455','mark@healthcorp.nl',11.75,'[www.healthcorp.nl](http://www.healthcorp.nl/)'),(4,5,7,'EuroPharma BV','Erik Janssen','0619988771','erik@europharma.nl',11.20,'[www.europharma.nl](http://www.europharma.nl/)'),(5,8,4,'HealthLine NV','Sophie Meijer','0619988772','sophie@healthline.nl',10.90,'[www.healthline.nl](http://www.healthline.nl/)'),(6,6,6,'MediTrade Europe','Lucas van Dijk','0619988773','lucas@meditrade.eu',12.30,'[www.meditrade.eu](http://www.meditrade.eu/)'),(7,11,8,'PharmaLogistics','Nina Bakker','0619988774','nina@pharmalogistics.nl',11.80,'[www.pharmalogistics.nl](http://www.pharmalogistics.nl/)'),(8,12,5,'CareSupply Group','Tom Verhoeven','0619988775','tom@caresupply.nl',10.60,'[www.caresupply.nl](http://www.caresupply.nl/)'),(9,9,9,'GlobalMeds','Daniel Peters','0619988776','daniel@globalmeds.com',13.10,'[www.globalmeds.com](http://www.globalmeds.com/)');
/*!40000 ALTER TABLE `leverancier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leverbaarheid_status`
--

DROP TABLE IF EXISTS `leverbaarheid_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leverbaarheid_status` (
  `status` varchar(100) NOT NULL,
  `omschrijving` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leverbaarheid_status`
--

LOCK TABLES `leverbaarheid_status` WRITE;
/*!40000 ALTER TABLE `leverbaarheid_status` DISABLE KEYS */;
INSERT INTO `leverbaarheid_status` VALUES ('leverbaar','Product is beschikbaar'),('niet leverbaar','Product niet beschikbaar');
/*!40000 ALTER TABLE `leverbaarheid_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levering`
--

DROP TABLE IF EXISTS `levering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `levering` (
  `medewerker_id` int NOT NULL,
  `order_id` int NOT NULL,
  `datum` date DEFAULT NULL,
  `levering_status` varchar(50) NOT NULL,
  PRIMARY KEY (`medewerker_id`,`order_id`),
  KEY `fk_Levering_Order1_idx` (`order_id`),
  KEY `fk_Levering_Status1_idx` (`levering_status`),
  KEY `fk_Levering_Medewerker1_idx` (`medewerker_id`),
  CONSTRAINT `fk_Levering_Medewerker1` FOREIGN KEY (`medewerker_id`) REFERENCES `medewerker` (`medewerker_id`),
  CONSTRAINT `fk_Levering_Order1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  CONSTRAINT `fk_Levering_Status1` FOREIGN KEY (`levering_status`) REFERENCES `levering_status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levering`
--

LOCK TABLES `levering` WRITE;
/*!40000 ALTER TABLE `levering` DISABLE KEYS */;
INSERT INTO `levering` VALUES (1,1,'2026-01-10','afgeleverd'),(1,4,'2026-01-12','terug naar magazijn'),(2,2,'2026-01-10','afgeleverd'),(2,5,'2026-01-13','onderweg'),(3,3,'2026-01-11','wordt verzameld');
/*!40000 ALTER TABLE `levering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levering_status`
--

DROP TABLE IF EXISTS `levering_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `levering_status` (
  `status` varchar(50) NOT NULL,
  `omschrijving` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levering_status`
--

LOCK TABLES `levering_status` WRITE;
/*!40000 ALTER TABLE `levering_status` DISABLE KEYS */;
INSERT INTO `levering_status` VALUES ('afgeleverd','Order afgeleverd'),('onderweg','Order is onderweg'),('terug naar magazijn','Order terug de magazijn gestuurd'),('wordt verzameld','Order wordt verzameld');
/*!40000 ALTER TABLE `levering_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medewerker`
--

DROP TABLE IF EXISTS `medewerker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medewerker` (
  `medewerker_id` int NOT NULL AUTO_INCREMENT,
  `telefoonnummer` char(20) NOT NULL,
  `voornaam` varchar(45) DEFAULT NULL,
  `achternaam` varchar(45) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  `gebruikersnaam` varchar(100) NOT NULL,
  `wachtwoord` varchar(100) NOT NULL,
  `regio` varchar(50) DEFAULT NULL,
  `rol` varchar(50) NOT NULL,
  `koerier_status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`medewerker_id`),
  KEY `fk_Medewerker_Regio1_idx` (`regio`),
  KEY `fk_Medewerker_Rol1_idx` (`rol`),
  KEY `fk_Medewerker_Koerier_Status1_idx` (`koerier_status`),
  CONSTRAINT `fk_Medewerker_Koerier_Status1` FOREIGN KEY (`koerier_status`) REFERENCES `koerier_status` (`status`),
  CONSTRAINT `fk_Medewerker_Regio1` FOREIGN KEY (`regio`) REFERENCES `regio` (`regio`),
  CONSTRAINT `fk_Medewerker_Rol1` FOREIGN KEY (`rol`) REFERENCES `rol` (`rol`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medewerker`
--

LOCK TABLES `medewerker` WRITE;
/*!40000 ALTER TABLE `medewerker` DISABLE KEYS */;
INSERT INTO `medewerker` VALUES (1,'0612340001','Jan','Koster','jan@timaflu.nl','jkoster','wachtwoord','Noord','Koerier','beschikbaar'),(2,'0612340002','Sanne','de Boer','sanne@timaflu.nl','sdeboer','wachtwoord','Zuid','Koerier','beschikbaar'),(3,'0612340003','Ali','Visser','ali@timaflu.nl','avisser','wachtwoord','West','Koerier','beschikbaar'),(4,'0612340004','Eva','Jansen','eva@timaflu.nl','ejansen','wachtwoord',NULL,'Verkoop',NULL),(5,'0612340005','Tom','de Wit','tom@timaflu.nl','tdwit','wachtwoord',NULL,'Inkoop',NULL),(6,'0612340006','Linda','van Dijk','linda@timaflu.nl','lvandijk','wachtwoord',NULL,'Administratie',NULL),(7,'0612340008','Sophie','Meijer','sophie@timaflu.nl','smeijer','wachtwoord',NULL,'Acquisitie',NULL);
/*!40000 ALTER TABLE `medewerker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `klant_id` int NOT NULL,
  `orderdatum` date NOT NULL,
  `type` varchar(45) NOT NULL,
  `totaalbedrag` decimal(10,2) NOT NULL,
  `factuur_id` int DEFAULT NULL,
  `dagdeel` enum('ochtend (08:00 – 12:00)','middag (12:00 – 17:00)') NOT NULL,
  `order_status` varchar(45) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `fk_bestelling_Klant1_idx` (`klant_id`),
  KEY `fk_Order_Factuur1_idx` (`factuur_id`),
  KEY `fk_Order_Order_status1_idx` (`order_status`),
  CONSTRAINT `fk_bestelling_Klant1` FOREIGN KEY (`klant_id`) REFERENCES `klant` (`klant_id`),
  CONSTRAINT `fk_Order_Factuur1` FOREIGN KEY (`factuur_id`) REFERENCES `factuur` (`factuur_id`),
  CONSTRAINT `fk_Order_Order_status1` FOREIGN KEY (`order_status`) REFERENCES `order_status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,1,'2026-01-09','normaal',1250.00,1,'ochtend (08:00 – 12:00)','wordt verzameld'),(2,2,'2026-01-10','spoed',500.00,2,'middag (12:00 – 17:00)','afgeleverd'),(3,3,'2026-01-11','normaal',980.00,3,'ochtend (08:00 – 12:00)','backorder'),(4,4,'2026-01-12','normaal',1200.00,NULL,'middag (12:00 – 17:00)','wordt verzameld'),(5,5,'2026-01-13','normaal',1500.00,NULL,'ochtend (08:00 – 12:00)','verstuurd'),(6,1,'2026-01-15','normaal',750.00,4,'ochtend (08:00 – 12:00)','wordt verzameld'),(7,1,'2026-01-16','spoed',1200.00,5,'middag (12:00 – 17:00)','afgeleverd'),(8,2,'2026-01-17','normaal',560.00,6,'ochtend (08:00 – 12:00)','backorder'),(9,11,'2026-01-18','normaal',850.00,1,'ochtend (08:00 – 12:00)','wordt verzameld'),(10,11,'2026-01-19','spoed',1100.00,2,'middag (12:00 – 17:00)','afgeleverd'),(11,12,'2026-01-20','normaal',600.00,3,'ochtend (08:00 – 12:00)','backorder'),(12,12,'2026-01-21','normaal',950.00,4,'middag (12:00 – 17:00)','verstuurd'),(13,13,'2026-01-22','normaal',1300.00,5,'ochtend (08:00 – 12:00)','afgeleverd'),(14,13,'2026-01-23','spoed',750.00,6,'middag (12:00 – 17:00)','wordt verzameld'),(15,14,'2026-01-24','normaal',1400.00,7,'ochtend (08:00 – 12:00)','verstuurd'),(16,14,'2026-01-25','normaal',900.00,8,'middag (12:00 – 17:00)','afgeleverd'),(17,15,'2026-01-26','normaal',500.00,9,'ochtend (08:00 – 12:00)','backorder'),(18,15,'2026-01-27','spoed',1250.00,10,'middag (12:00 – 17:00)','wordt verzameld');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_status`
--

DROP TABLE IF EXISTS `order_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_status` (
  `status` varchar(45) NOT NULL,
  `omschrijving` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_status`
--

LOCK TABLES `order_status` WRITE;
/*!40000 ALTER TABLE `order_status` DISABLE KEYS */;
INSERT INTO `order_status` VALUES ('afgeleverd','Order afgeleverd'),('backorder','Product niet op voorraad'),('verstuurd','Order is onderweg'),('wordt verzameld','Order wordt verzameld');
/*!40000 ALTER TABLE `order_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderregel`
--

DROP TABLE IF EXISTS `orderregel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderregel` (
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `aantal` int NOT NULL,
  `prijs_per_product` decimal(10,2) NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`),
  KEY `fk_orderregel_bestelling1_idx` (`order_id`),
  KEY `fk_orderregel_medicijn1_idx` (`product_id`),
  CONSTRAINT `fk_orderregel_bestelling1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  CONSTRAINT `fk_orderregel_medicijn1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderregel`
--

LOCK TABLES `orderregel` WRITE;
/*!40000 ALTER TABLE `orderregel` DISABLE KEYS */;
INSERT INTO `orderregel` VALUES (1,1,100,2.50),(1,2,50,3.00),(2,3,20,5.00),(3,4,60,4.00),(4,5,30,3.50),(5,6,40,2.75),(5,7,50,4.50),(6,11,50,6.00),(6,12,30,4.50),(7,13,40,3.75),(7,14,100,2.00),(8,15,60,5.50);
/*!40000 ALTER TABLE `orderregel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picktask`
--

DROP TABLE IF EXISTS `picktask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `picktask` (
  `picktask_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `bak_id` int DEFAULT NULL,
  `distributiehoek` int NOT NULL,
  `robot_id` int NOT NULL,
  `gang` varchar(1) NOT NULL,
  PRIMARY KEY (`picktask_id`,`order_id`),
  KEY `fk_picktask_bestelling1_idx` (`order_id`),
  KEY `fk_picktask_verzamelbak1_idx` (`bak_id`),
  KEY `fk_Picktask_Distributiehoek1_idx` (`distributiehoek`),
  KEY `fk_Picktask_Robot_Magazijngang1_idx` (`robot_id`,`gang`),
  CONSTRAINT `fk_picktask_bestelling1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  CONSTRAINT `fk_Picktask_Distributiehoek1` FOREIGN KEY (`distributiehoek`) REFERENCES `distributiehoek` (`distributie_id`),
  CONSTRAINT `fk_Picktask_Robot_Magazijngang1` FOREIGN KEY (`robot_id`, `gang`) REFERENCES `robot_magazijngang` (`robot_id`, `gang`),
  CONSTRAINT `fk_picktask_verzamelbak1` FOREIGN KEY (`bak_id`) REFERENCES `verzamelbak` (`bak_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picktask`
--

LOCK TABLES `picktask` WRITE;
/*!40000 ALTER TABLE `picktask` DISABLE KEYS */;
INSERT INTO `picktask` VALUES (1,1,1,1,1,'A'),(2,2,2,2,2,'B'),(3,3,3,3,3,'C'),(4,4,4,1,4,'D'),(5,5,5,2,1,'A');
/*!40000 ALTER TABLE `picktask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `naam` varchar(100) NOT NULL,
  `omschrijving` varchar(500) DEFAULT NULL,
  `prijs` decimal(10,2) NOT NULL,
  `minimumvoorraad` int NOT NULL,
  `hoeveelheid` int NOT NULL,
  `verpakkingstype` varchar(45) DEFAULT NULL,
  `robot_id` int NOT NULL,
  `gang` varchar(1) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `fk_Product_Magazijngang1_idx` (`robot_id`,`gang`),
  CONSTRAINT `fk_Product_Magazijngang1` FOREIGN KEY (`robot_id`, `gang`) REFERENCES `robot_magazijngang` (`robot_id`, `gang`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Paracetamol 500mg','Pijnstiller',2.50,50,200,'doos',1,'A'),(2,'Ibuprofen 200mg','Ontstekingsremmer',3.00,40,100,'doos',2,'B'),(3,'Amoxicilline 250mg','Antibioticum',5.00,30,50,'strip',3,'C'),(4,'Cetirizine 10mg','Anti-allergie',4.00,30,120,'doos',5,'E'),(5,'Omeprazol 20mg','Maagbescherming',3.50,25,80,'strip',2,'B'),(6,'Simvastatine 10mg','Cholesterol',2.75,20,60,'doos',3,'C'),(7,'Paracetamol 1000mg','Pijnstiller',4.50,50,150,'doos',1,'A'),(8,'Ibuprofen 400mg','Ontstekingsremmer',5.50,40,90,'doos',2,'B'),(9,'Amoxicilline 500mg','Antibioticum',7.00,30,70,'strip',6,'F'),(10,'Lorazepam 1mg','Slaapmiddel',6.50,20,40,'strip',8,'h'),(11,'Cefalexine 500mg','Antibioticum',6.00,20,100,'strip',1,'A'),(12,'Metformine 500mg','Diabetes',4.50,30,150,'doos',2,'B'),(13,'Salbutamol 100mcg','Astma',3.75,25,80,'inhaler',3,'C'),(14,'Aspirine 100mg','Pijnstiller',2.00,50,200,'doos',1,'A'),(15,'Prednison 5mg','Ontstekingsremmer',5.50,20,60,'strip',2,'B'),(16,'Furosemide 40mg','Diureticum',3.00,15,90,'doos',3,'C'),(17,'Diazepam 5mg','Slaapmiddel',4.00,20,50,'strip',4,'D'),(18,'Levothyroxine 50mcg','Hormoon',4.75,25,100,'doos',1,'A'),(19,'Amoxicilline 125mg','Antibioticum',2.50,30,70,'strip',2,'B'),(20,'Omeprazol 40mg','Maagbescherming',5.00,25,90,'strip',8,'H'),(21,'Loratadine 10mg','Anti-allergie',4.50,30,120,'doos',7,'G'),(22,'Simvastatine 20mg','Cholesterol',3.25,20,18,'doos',6,'F'),(23,'Ibuprofen 600mg','Ontstekingsremmer',5.75,40,25,'doos',5,'E'),(24,'Paracetamol 750mg','Pijnstiller',3.50,60,300,'doos',7,'G'),(25,'Clarithromycine 500mg','Antibioticum',7.50,30,9,'strip',4,'D');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productleverancier`
--

DROP TABLE IF EXISTS `productleverancier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productleverancier` (
  `product_id` int NOT NULL,
  `leverancier_id` int NOT NULL,
  `prijs` decimal(10,2) NOT NULL,
  `leverbaarheid_status` varchar(100) NOT NULL,
  PRIMARY KEY (`leverancier_id`,`product_id`),
  KEY `fk_Product_has_Leverancier_Leverancier1_idx` (`leverancier_id`),
  KEY `fk_Product_has_Leverancier_Product1_idx` (`product_id`),
  KEY `fk_Leverbaarheid_Status_idx` (`leverbaarheid_status`),
  CONSTRAINT `fk_Leverbaarheid_Status` FOREIGN KEY (`leverbaarheid_status`) REFERENCES `leverbaarheid_status` (`status`),
  CONSTRAINT `fk_Product_has_Leverancier_Leverancier1` FOREIGN KEY (`leverancier_id`) REFERENCES `leverancier` (`leverancier_id`),
  CONSTRAINT `fk_Product_has_Leverancier_Product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productleverancier`
--

LOCK TABLES `productleverancier` WRITE;
/*!40000 ALTER TABLE `productleverancier` DISABLE KEYS */;
INSERT INTO `productleverancier` VALUES (1,1,10.50,'leverbaar'),(2,1,10.50,'leverbaar'),(6,1,13.00,'leverbaar'),(9,1,15.00,'leverbaar'),(3,2,12.00,'leverbaar'),(4,2,11.50,'leverbaar'),(7,2,12.80,'leverbaar'),(10,2,16.50,'leverbaar'),(5,3,12.50,'niet leverbaar'),(8,3,14.00,'leverbaar');
/*!40000 ALTER TABLE `productleverancier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regio`
--

DROP TABLE IF EXISTS `regio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regio` (
  `regio` varchar(50) NOT NULL,
  `omschrijving` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`regio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regio`
--

LOCK TABLES `regio` WRITE;
/*!40000 ALTER TABLE `regio` DISABLE KEYS */;
INSERT INTO `regio` VALUES ('Noord','Noord regio'),('West','West regio'),('Zuid','Zuid regio');
/*!40000 ALTER TABLE `regio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robot_magazijngang`
--

DROP TABLE IF EXISTS `robot_magazijngang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `robot_magazijngang` (
  `robot_id` int NOT NULL,
  `gang` varchar(1) NOT NULL,
  `robot_status` varchar(30) NOT NULL,
  PRIMARY KEY (`robot_id`,`gang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robot_magazijngang`
--

LOCK TABLES `robot_magazijngang` WRITE;
/*!40000 ALTER TABLE `robot_magazijngang` DISABLE KEYS */;
INSERT INTO `robot_magazijngang` VALUES (1,'A','klaar'),(2,'B','klaar'),(3,'C','klaar'),(4,'D','klaar'),(5,'E','klaar'),(6,'F','klaar'),(7,'G','klaar'),(8,'H','klaar');
/*!40000 ALTER TABLE `robot_magazijngang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `rol` varchar(50) NOT NULL,
  `omschrijving` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES ('Acquisitie','Acquisitie medewerker'),('Administratie','Administratief medewerker'),('Inkoop','Bestelt producten'),('Koerier','Bezorgt orders'),('Verkoop','Verkoopmedewerker');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verzamelbak`
--

DROP TABLE IF EXISTS `verzamelbak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `verzamelbak` (
  `bak_id` int NOT NULL AUTO_INCREMENT,
  `barcode` varchar(75) NOT NULL,
  `capaciteit` varchar(50) NOT NULL,
  PRIMARY KEY (`bak_id`),
  UNIQUE KEY `barcode_UNIQUE` (`barcode`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verzamelbak`
--

LOCK TABLES `verzamelbak` WRITE;
/*!40000 ALTER TABLE `verzamelbak` DISABLE KEYS */;
INSERT INTO `verzamelbak` VALUES (1,'VB001','50kg'),(2,'VB002','40kg'),(3,'VB003','60kg'),(4,'VB004','55kg'),(5,'VB005','45kg');
/*!40000 ALTER TABLE `verzamelbak` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-15 21:38:39
