<?php

function getRandomMovie()
{
    $GLOBALS['movies'];
    $rand_movies = array_rand($movies, 3);
    echo $movies[$rand_movies[0]];
    echo $movies[$rand_movies[1]];
}

function getMoviesByGenre($genre) {}

function getNewestMovies() {}
