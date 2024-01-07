<?php

function HelloWorld()
{
    echo "Hello World!";
    $output = "App is ready on http://localhost:80";
    $fp = fopen('php://stdout', 'rw');
    fputs($fp, "$output\n");
}

HelloWorld();
