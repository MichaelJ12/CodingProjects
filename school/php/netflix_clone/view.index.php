<!DOCTYPE html>
<html lang="nl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Netflix | Week 1</title>
</head>

<body>

    <h1>Netflix - week j1</h1>
    <section class="special">
        <image src="<?= $randomMovie["image"] ?>" class="full-image"></image>
        <div class="full-image-text">
            <h3><?= $randomMovie["title"] ?></h3>
            <p><?= $randomMovie["year"] ?></p>
            <p><?= $randomMovie["genre"] ?></p>
        </div>
    </section>
    <!-- een terugkerende rij -->
    <?php
    foreach ($genres as $genre):
        $movies2 = getMoviesByGenre($genre);
    ?>
        <section class="movierow">

            <h2><?= $genre ?></h2>
            <div class="moviecontainer">

                <?php foreach ($movies2 as $movie): ?>
                    <div class="movieitem">
                        <image src="<?= $movie["image"] ?>"></image>
                        <h3><?= $movie["title"] ?></h3>
                        <p><?= $movie["year"] ?></p>
                        <p><?= $movie["genre"] ?></p>

                    </div>

                <?php endforeach; ?>


            </div>
        </section>
    <?php endforeach; ?>
    <!-- einde terugkerende rij -->
</body>

</html>