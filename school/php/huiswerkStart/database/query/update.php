<?php

$updateMovie = 
    "UPDATE movies 
    SET fav = :fav 
    WHERE (id = :id);
    ";
?>