<?php
require 'items.index.php';

$newestMovies = getNewestMovies();

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

function getNewestMovies()
{
    $sortedMovies = $GLOBALS['movies'];

    usort($sortedMovies, 'descYear');

    $result = array_slice($sortedMovies, 0, 5);
    return $result;
}

function descYear($a, $b)
{
    if ($a["year"] === $b["year"]) {
        return 0;
    }
    return ($a["year"] > $b["year"]) ? -1 : 1;
}
