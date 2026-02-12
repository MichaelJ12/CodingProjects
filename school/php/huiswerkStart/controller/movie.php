<?php
require "database/query/select.php";
require "database/query/update.php";



$config = require('config.php');
$db = new Database($config['database']);

$id = getUrlParams("id");
$fav = getUrlParams("fav");

if ($fav !== null) {
    $favourite = $db->query($updateMovie, [":id" => $id, ":fav" => $fav]);    
}

// $movie = $db->query($updateMovie)->fetch();
$movie = $db->query($selectMovie, [":id" => $id])->fetch();


// $movie = $db->query($updateMovie, [":id" => $id])->fetch();

require "view/view.movie.php";
?>