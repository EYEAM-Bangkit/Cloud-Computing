# Cloud SQL Setup

### Create Database
```sql
CREATE DATABASE database_name;
```

### Create Table Animal
``` sql
CREATE TABLE `animal` (
  `namapopuler` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `namailmiah` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `foto` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `kingdom` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `phylum` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `genus` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `class` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `order` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `family` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `deskripsi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `persebaran` varchar(1224) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `habitat` varchar(190) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `conserv` varchar(325) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `threats` varchar(224) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `populasi` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `iucn` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

### Insert Data Into Table Animal
```sql
INSERT INTO `animal` (`namapopuler`, `namailmiah`, `foto`, `kingdom`, `phylum`, `genus`, `class`, `order`, `family`, `deskripsi`, `persebaran`, `habitat`, `conserv`, `threats`, `populasi`, `iucn`) VALUES
('Komodo Dragon', 'Varanus komodoensis', '', 'Animalia', 'Chordata', 'Varanus', 'Mammalia', 'Squamata', 'Varanidae', 'Komodo Dragon Varanus komodoensis has most recently been assessed for The IUCN Red List of Threatened Species in 2019. Varanus komodoensis is listed as Endangered under criteria C1.', 'Indonesia (Lesser Sunda Is.)', 'Forest, Savanna, Marine Intertidal', 'Occurs in at least one protected area : Yes\r\nSuccessfully reintroduced or introduced benignly : Yes\r\nSubject to ex-situ conservation : Yes', 'Tourism & recreation areas\r\nHunting & trapping terrestrial animals', 'Stable', 'Endangered');
```

### Add Primary Key
```sql
ALTER TABLE `animal`
  ADD PRIMARY KEY (`namailmiah`);
COMMIT;
```

***

### Create Table Logs
```sql
CREATE TABLE `logs` (
  `eventid` varchar(128) NOT NULL,
  `userid` varchar(128) DEFAULT NULL,
  `animal` varchar(30) DEFAULT NULL,
  `logtime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

### Add Primary Key
```sql
ALTER TABLE `logs`
  ADD PRIMARY KEY (`eventid`);
COMMIT;
```
















a
