<?php   
require("partial/head.php");
require("partial/nav.php"); ?>
    <h1>Netflix - week 2</h1>
    <form method="GET" action="/">
        <input tpye="text" name="search" placeholder="zoek een film..." value="<?= $searchQuery ?>">
        <button type="submit">Zoeken</button>
    </form>

    <section class="special">
        <a href="movie?id=<?= $randomMovie["id"]?>&fav=<?= $randomMovie["fav"]?>">
            <figure class="image-container"><image src="<?= $randomMovie["image"]?>" class="full-image"></image></figure>
            <div class="full-image-text">
                <h3><?= $randomMovie["title"]?></h3>
                <p><?= $randomMovie["year"]?></p>
                <p><?= $randomMovie["genre"]?></p>
            </div>
        </a>
    </section>
    <?php
   
    if (isset($selectedGenre)) {
            createMovieRow(getMoviesByGenre($selectedGenre), $selectedGenre);
    } else if (!empty($searchQuery)) {
        createMovieRow(getSearchedMovie($searchQuery), "Uitkomsten");
    } else {
        createMovieRow($favouriteMovies,"Favoriete Films");
        createMovieRow($newestMovies,"Nieuwste Films");
        foreach ($genres as $genre):
            createMovieRow(getMoviesByGenre($genre['menuitem']), $genre['menuitem']);
        endforeach;
    }
        

    require("partial/footer.php");
    function createMovieRow($movieSelection, $title){
        ?>
        <section class="movierow">
            <h2><?=$title?></h2>
            <div class="moviecontainer">
            <?php
                if(!$movieSelection){
                    echo "geen $title gevonden.";

                }else{
                    foreach ($movieSelection as $movie):?>
                    <a href="movie?id=<?= $movie["id"]?>&fav=<?= $movie["fav"]?>">
                        <div class="movieitem">
                            <figure class="image-container"><image src="<?= $movie["image"]?>"></image></figure>
                            <h3><?= $movie["title"]?></h3>
                            <p><?= $movie["year"]?></p>
                            <p><?= $movie["genre"]?></p>
                        </div>
                    </a>
            <?php   endforeach; 
                }
                
            ?>
            </div>
        </section>
        <?php
    }
?>



