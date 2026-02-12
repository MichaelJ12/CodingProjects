<?php

$selectAllMovies = 
    "SELECT 
        m.id, 
        m.title, 
        m.year, 
        GROUP_CONCAT(g.genre ORDER BY g.genre SEPARATOR ', ') AS genre,
        m.image,
        m.fav
    FROM movies m
    JOIN movie_genres mg ON m.id = mg.id_movie
    JOIN genres g ON mg.id_genre = g.genre
    GROUP BY m.id, m.title, m.year, m.image
    ORDER BY m.id;";


$selectMovie =
    "SELECT 
        m.id,
        m.title, 
        m.year, 
        GROUP_CONCAT(g.genre ORDER BY g.genre SEPARATOR ', ') AS genre,
        m.image,
        m.fav
    FROM movies m
    JOIN movie_genres mg ON m.id = mg.id_movie
    JOIN genres g ON mg.id_genre = g.genre
    WHERE m.id = :id
    GROUP BY m.id, m.title, m.year, m.image;";

$selectMenuItems = "SELECT * FROM menu;";

?>