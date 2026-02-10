<?php
require 'functions.php';
// require 'router.php';

$dbhost = 'localhost';
$dbname = 'netflix';
$dbport = '3306';
$dbuser = 'root';
$dbpass = '';

$dns = "mysql:host=localhost;port=3306;dbname=netflix;charset=utf8mb4";

$pdo = new PDO($dns, $dbuser, $dbpass);

$stmt = $pdo->prepare("select * from netflix.movies");
$stmt->execute();

$posts = $stmt->fetchAll();

dd($posts);
