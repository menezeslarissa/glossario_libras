create database librasdb;
use librasdb;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: librasdb
-- ------------------------------------------------------
-- Server version	5.7.9-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disciplina` (
  `discdir` char(5) NOT NULL,
  `discdescricao` varchar(100) NOT NULL,
  `discdtinclusao` datetime NOT NULL,
  PRIMARY KEY (`discdir`),
  UNIQUE KEY `discdir_UNIQUE` (`discdir`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
INSERT INTO `disciplina` VALUES ('BD','Banco de Dados','2018-11-27 15:26:43');
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sinal`
--

DROP TABLE IF EXISTS `sinal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sinal` (
  `idsinal` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sindescricao` varchar(100) NOT NULL,
  `sinconceito` varchar(300) NOT NULL,
  `sinarquivo` varchar(50) DEFAULT NULL,
  `sindiscdir` char(5) DEFAULT NULL,
  PRIMARY KEY (`idsinal`),
  UNIQUE KEY `idsinal_UNIQUE` (`idsinal`),
  UNIQUE KEY `sindescricao_UNIQUE` (`sindescricao`),
  UNIQUE KEY `sinconceito_UNIQUE` (`sinconceito`),
  KEY `sindiscdir` (`sindiscdir`),
  CONSTRAINT `sinal_ibfk_1` FOREIGN KEY (`sindiscdir`) REFERENCES `disciplina` (`discdir`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sinal`
--

LOCK TABLES `sinal` WRITE;
/*!40000 ALTER TABLE `sinal` DISABLE KEYS */;
INSERT INTO `sinal` VALUES (1,'Banco de dados','é um conjunto de dados relacionados e organizados, que pode ser informatizado ou não. Definimos “dado” como um fato que possui alguma relevância/significado e que pode ser registrado','bancodados','BD'),(70,'Integridade referencial','define que os valores de uma coluna pertencente a uma chave estrangeira (lado N) devem ser os valores existentes na chave primária da tabela referenciada (lado 1). ','integridadereferencial','BD'),(71,'SGBD','é um conjunto de programas que permite o acesso e manipulação de vários banco de dados, independente do tamanho (volume de dados).','sgbd','BD'),(72,'Entidade','é uma “coisa” do mundo real com existência independente (existência física e conceitual) e com identificação distinta. Conjunto de elementos com as mesmas características. Essa existência pode ser física (ex.: aluno, carro) ou conceitual (ex.: serviço, empresa).','entidade','BD'),(73,'Instância','é um item do conjunto (entidade ou relacionamento).','instancia','BD'),(74,'Atributo','define as propriedades específicas (características) que descrevem uma entidade. ','atributo','BD'),(75,'Atributo-chave','é o atributo que identifica um elemento de forma única no conjunto. ','atributochave','BD'),(76,'Valor nulo','é a ausência de informação.','valornulo','BD'),(77,'Atributo simples','é o atributo que não pode ser dividido em atributos menores, e seu valor já define a característica de forma completa.','atributosimples','BD'),(78,'Atributo composto','é o atributo que pode ser dividido em subpartes menores, que são atributos simples com significados diferentes. ','atributocomposto','BD'),(79,'Atributo multivalorado','é o atributo que possui um conjunto de valores diferentes e simultâneos.','atributomultivalorado','BD'),(80,'Atributo armazenado','é o atributo que deve existir fisicamente no Banco de Dados. ','atributoarmazenado','BD'),(81,'Atributo derivado','é determinado (calculado) a partir de um atributo armazenado.','atributoderivado','BD'),(82,'Relacionamento','é uma associação entre duas ou mais entidades. ','relacionamento','BD'),(83,'Auto-relacionamento','é uma associação entre elementos (instâncias) da mesma entidade. ','autorelacionamento','BD'),(84,'Entidade fraca','é uma entidade onde não é possivel definir um atributo-chave que atenda aos conceitos da identificação única de cada elemento, e portanto sua existência sempre será vinculada a uma outra entidade. ','entidadefraca','BD'),(85,'Regra de cardinalidade','é o número máximo de elementos (instâncias) de uma entidade B associados a um único elemento (instância) de uma entidade A. ','regracardinalidade','BD'),(86,'Relacionamento binário (Grau 2)','são duas entidades relacionadas.','relacionamentobinario','BD'),(87,'Relacionamento de cardinalidade N-1','Um curso pode ser cursado por N alunos, mas um aluno só pode cursar 1 curso.','relacionamentocardinalidaden1','BD'),(88,'Relacionamento de cardinalidade 1-1','um planeta (e somente um) possui um núcleo (e somente um).','relacionamentocardinalidade11','BD'),(89,'Relacionamento de cardinalidade M-N','um professor leciona em N cursos, e um curso é lecionado por M professores.','relacionamentocardinalidademn','BD'),(90,'Relacionamento ternário (Grau 3)','são três entidades relacionadas, e para definir a cardinalidade é preciso isolar um par de entidades e entender qual é a associação desse par com a entidade que sobrou. ','relacionamentoternario','BD'),(93,'Coluna/Campo','é o local onde os diferentes valores dos atributos de uma entidade podem ser armazenados. ','colunacampo','BD'),(94,'Registro ou linha','representa todos os dados de um elemento (instância) de uma entidade em particular. Cada linha formada por uma lista de colunas. Não precisam conter informações em todas as colunas, podendo assumir valores nulos quando for permitido. ','registrolinha','BD'),(95,'Chave primária','é uma coluna (ou combinação de colunas) que identifica unicamente um registro dentro de uma tabela. Não é possível haver dois registros com o mesmo valor de chave primária, e esse valor é obrigatório. ','chaveprimaria','BD'),(96,'Chave estrangeira','é uma coluna em uma tabela B associada (Relacionamento) a uma coluna da tabela A, onde na A essa coluna é chave primária. Esse mecanismo permite a representação de um relacionamento no SGBD. ','chaveestrangeira','BD'),(103,'Disjunção','define que as subclasses devem ser desvinculadas (não há interseção entre os conjuntos). Uma instância de um conjunto pode ser membro de no máximo 1 (uma) das subclasses da especialização.','disjuncao','BD'),(104,'Sobreposição','define que as subclasses não precisam ser desvinculadas (pode haver interseção entre os conjuntos), ou seja, a mesma instância pode ser um membro de mais de uma subclasse da especialização. ','sobreposicao','BD'),(105,'Tabela','é o local onde os dados são fisicamente armazenados. Um banco de dados pode conter várias tabelas. ','tabela','BD'),(106,'Agregação','é utilizada quando um relacionamento se transforma numa entidade que as vezes pode se associar a uma outra entidade. É um relacionamento opcional.','agregacao','BD'),(107,'Regra de participação','especifica se a existência de uma instância de uma entidade depende da mesma ser relacionada a uma instância de outra entidade através de algum tipo de relacionamento. ','regraparticipacao','BD'),(108,'Superclasse (Generalização)','é a abstração de características gerais. Um atributo da superclasse é uma característica que todas as subclasses vão possuir. Superclasses possuem uma ou mais subclasses.','superclasse','BD'),(109,'Subclasse (Especialização)','é a especialização de uma superclasse, onde delas herdam todas as suas características comuns e podem possuir atributos e relacionamentos específicos.','subclasse','BD');
/*!40000 ALTER TABLE `sinal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'librasdb'
--

--
-- Dumping routines for database 'librasdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-06 16:52:13
