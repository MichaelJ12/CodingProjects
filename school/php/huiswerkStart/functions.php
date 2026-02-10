<?php

function parseUrlParams($paramValues, $isInt = true)
{
    $paramItems = null;
    if (isset(parse_url($_SERVER["REQUEST_URI"])['query'])) {
        $urlParams = parse_url($_SERVER["REQUEST_URI"])['query'];
        parse_str($urlParams, $queryParams);

        foreach ($paramValues as $paramValue) {
            if ($isInt) {
                $paramItems[$paramValue] = isset($queryParams[$paramValue]) ? (int) $queryParams[$paramValue] : null;
            } else {
                $paramItems[$paramValue] = isset($queryParams[$paramValue]) ? $queryParams[$paramValue] : null;
            }
        }
    }
    return $paramItems;
}

function dd($value)
{
    echo '<pre>';
    var_dump($value);
    echo '</pre>';
    die();
}
