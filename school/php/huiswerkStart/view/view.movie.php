<?php

    require("partial/head.php");

    // if urlparam is empty, look at movieitem (from database).
    // if url param is filled (there has been an update) use the variable $fav.
    // This because the view is loaded before de update is done (async).
    // $isFavoriteDb = $movie["fav"] == 1; // from database
    // $isFavoriteUrl = $fav;
    // $isFavorite = isset($fav) ? $fav : $isFavoriteDb;

    $url;
    $buttonClass; 
    $buttonText;    

?>
    <div class="single-movie-container">
        <a href="/">< go home</a>
            <section class="single-movie-image">
                <image src="<?=  $movie['image'] ?>">
            </section>
            <section class="single-movie-info">
                <div>
                    <h1><?= $movie['title'] ?></h1>
                    <p><?= $movie['year'] ?></p>
                    <p><?= $movie["genre"] ?></p>
                </div>
                <div class="button-container">
                    <a class="button" href="#">bekijk film</a>
                    <a class="button "  href="">favoriet</a>
            </section>
    </div>
    
    
    <?php
   
?>