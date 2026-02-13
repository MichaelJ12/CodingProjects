<nav>
    <ul>
        <?php $homeclass = isset($selectedGenre) ? "not-selected" : "selected"; ?>
        <li><a href="/" class="<?= $homeclass ?>">Home</a></li>   
        <?php foreach ($genres as $genre): ?>  
            <?php $class = $selectedGenre === $genre['menuitem'] ? "selected" : "not-selected"; ?>
            <li><a href="/?genre=<?= $genre['menuitem'] ?>" class="<?= $class ?>"><?= $genre['menuitem'] ?></a></li>
        <?php endforeach; ?>
    </ul>
</nav>