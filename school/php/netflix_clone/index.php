<?php
include 'items.index.php';

?>
<?php

function getRandomMovie()
{
    $t = $GLOBALS['movies'];
    $rand_movies = array_rand($t, 1);
    
    return $t[$rand_movies];
}


$randomMovie = getRandomMovie();
include 'view.index.php';

function getMoviesByGenre($genre) {
    $movies = $GLOBALS['movies'];

    return array_filter($movies, function($movie) use ($genre) {
        return str_contains($movie['genre'], $genre);
    });

}

$genres = ['Adventure', 'Drama', 'Biography en Crime'];

function getNewestMovies() {}
