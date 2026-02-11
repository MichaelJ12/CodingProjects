<nav>
    <ul>
        
        <li><a href="/" class="selected">Home</a></li>   
        <?php foreach ($genres as $genre): ?>  
            <li><a href="#" class="not-selected"><?= $genre['menuitem'] ?></a></li>
        <?php endforeach; ?>
    </ul>
</nav>