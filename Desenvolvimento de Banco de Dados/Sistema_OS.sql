CREATE DATABASE  IF NOT EXISTS `sistema_os` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sistema_os`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: sistema_os
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(30) NOT NULL DEFAULT '',
  `CPF_CNPJ` bigint NOT NULL,
  `Endereco` varchar(50) NOT NULL DEFAULT '',
  `Cep` decimal(8,0) NOT NULL,
  `Data_Cadastro` date DEFAULT NULL,
  `Telefone` int NOT NULL,
  `Contrato` enum('Não','Sim') NOT NULL DEFAULT 'Não',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'André Santos',2147483647,'Algum Lugar, 47',8912345,'2020-08-17',0,'Não'),(2,'João Silva',2147483647,'Cafundó, 76',8954321,'2020-08-20',0,'Sim');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem`
--

DROP TABLE IF EXISTS `ordem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordem` (
  `nOS` int NOT NULL AUTO_INCREMENT,
  `Cliente_id` int NOT NULL,
  `Equipamento` varchar(30) NOT NULL DEFAULT '',
  `Defeito` varchar(50) NOT NULL DEFAULT '',
  `Laudo` text,
  `Serviço` varchar(50) NOT NULL DEFAULT '',
  `Valor` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`nOS`),
  KEY `FK_cliente` (`Cliente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem`
--

LOCK TABLES `ordem` WRITE;
/*!40000 ALTER TABLE `ordem` DISABLE KEYS */;
INSERT INTO `ordem` VALUES (1,1,'Computador','Não Liga','Fonte com defeito','Troca da Fonte',100.00),(2,1,'Roteador','Não acessa rede','Configuração incorreta','Reconfiguração',30.00),(3,2,'Computador','Formatação','Durante processo apresentou defeito no HD','Troca do HD e Formatação',530.00);
/*!40000 ALTER TABLE `ordem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-19 21:12:18

