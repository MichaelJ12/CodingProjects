<?php

require "database/query/select.php";


    $config = require('config.php');
    $db = new Database($config['database']);

    $t = $db->query($selectAllMovies)->fetchAll();
    $genres = $db->query($selectMenuItems)->fetchAll();

    
    $GLOBALS['movies'] = $t;

    $randomMovie = getRandomMovie();
    $newestMovies = getNewestMovies();

    function getRandomMovie(){
        $key = array_rand($GLOBALS["movies"]);
    	$value = $GLOBALS["movies"][$key];
        return $value;
    }
    
    function getMoviesByGenre($genre){
        
        return array_filter($GLOBALS["movies"], function($movie) use ($genre){
            return $movie = str_contains($movie["genre"], $genre);
        });

    }

    function getNewestMovies(){
        $sortedMovies = $GLOBALS["movies"];
        usort($sortedMovies, "descYear");
        
        //get top 5
        $output = array_slice($sortedMovies, 0, 5);
        return $output;
    }

    function descYear($a, $b)
    {
        if ($a["year"] == $b["year"]) {
            return 0;
        }
        return ($a["year"] > $b["year"]) ? -1 : 1;
    }

    

require "view/view.index.php";