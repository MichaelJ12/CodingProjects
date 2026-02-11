<?php

$uri = parse_url($_SERVER['REQUEST_URI'])['path'];

$routes = [
    '/' => 'controller/index.php',
    '/movie' => 'controller/movie.php',
];

if (array_key_exists($uri, $routes)) {
    require $routes[$uri];
}
