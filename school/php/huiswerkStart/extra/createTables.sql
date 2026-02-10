CREATE TABLE `genres` (
  `genre` varchar(45) NOT NULL,
  PRIMARY KEY (`genre`)
);
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `year` year NOT NULL,
  `image` varchar(45) NOT NULL,
  `fav` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
);
CREATE TABLE `movie_genres` (
  `id_movie` int NOT NULL,
  `id_genre` varchar(45) NOT NULL,
  PRIMARY KEY (`id_movie`,`id_genre`),
  KEY `fk_genre_idx` (`id_genre`),
  CONSTRAINT `fk_genre` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`genre`),
  CONSTRAINT `fk_movies` FOREIGN KEY (`id_movie`) REFERENCES `movies` (`id`)
);
CREATE TABLE `menu` (
  `menuitem` varchar(45) NOT NULL,
  PRIMARY KEY (`menuitem`)
);


