<?php
require 'items.index.php';


function getRandomMovie()
{
    $t = $GLOBALS['movies'];
    $rand_movies = array_rand($t, 1);

    return $t[$rand_movies];
}


$randomMovie = getRandomMovie();


function getMoviesByGenre($genre)
{
    $movies = $GLOBALS['movies'];

    return array_filter($movies, function ($movie) use ($genre) {
        return str_contains($movie['genre'], $genre);
    });
}

$genres = ['Adventure', 'Drama', 'Biography', 'Crime'];

require 'view.index.php';

function getNewestMovies() {}
