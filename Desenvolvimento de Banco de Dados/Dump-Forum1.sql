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
  `Nome` varchar(30) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `CPF` bigint unsigned NOT NULL,
  `Endereco` varchar(50) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `Cep` decimal(8,0) NOT NULL,
  `Data_Cadastro` date DEFAULT NULL,
  `Telefone` int unsigned NOT NULL,
  `Contrato` enum('Não','Sim') COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'Não',
  PRIMARY KEY (`id`),
  UNIQUE KEY `CPF` (`CPF`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'André Santos',12345678910,'Algum Lugar, 47',89123145,'2020-07-17',999999999,'Não'),(2,'João Silva',10987654321,'Cafundó, 76',89543321,'2020-07-20',999999998,'Sim'),(3,'Luiz Souza',10101550554,'Carajas,60',89258403,'2020-07-25',999999997,'Sim'),(4,'Barbara Dias',10101608535,'Carajas,150',89258403,'2020-08-22',999999996,'Não'),(5,'Joana Moreira',10109088084,'Itu,30',89259025,'2020-08-24',999999995,'Não');
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
  `Equipamento` varchar(30) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `Defeito` varchar(50) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `Laudo` text COLLATE utf8mb4_general_ci,
  `Serviço` varchar(50) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `Valor` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`nOS`),
  KEY `FK_cliente` (`Cliente_id`),
  CONSTRAINT `FK_cliente` FOREIGN KEY (`Cliente_id`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem`
--

LOCK TABLES `ordem` WRITE;
/*!40000 ALTER TABLE `ordem` DISABLE KEYS */;
INSERT INTO `ordem` VALUES (1,1,'Computador','Não Liga','Fonte com defeito','Troca da Fonte',100.00),(2,2,'Roteador','Não acessa rede','Configuração incorreta','Reconfiguração',30.00),(3,2,'Computador','Formatação c/ BKP','Efetuado serviço solicitado','Formatação com Backup',100.00),(4,4,'Notebook','Formatação c/ BKP Linux','Efetuado serviço solicitado','Formatação com Backup',100.00),(5,3,'Notebook','Formatação s/ BKP','Efetuado serviço solicitado','Formatação Sem Backup',70.00);
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

-- Dump completed on 2020-08-31 12:02:00
