<?php

$uri = parse_url($_SERVER['REQUEST_URI'])['path'];

$routes = [
    '/' => 'view/view.index.php',
    '/movies' => 'controller/movies.php',
];

if (array_key_exists($uri, $routes)) {
    require $routes[$uri];
}
