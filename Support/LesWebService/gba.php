<?php
header('Content-Type: application/json; charset=utf-8');

$entries = file_get_contents('bronnen.json');
if ($entries === false) {
    http_response_code(500);
}

$objects = json_decode($entries, true);
$timer = rand(0,1);
sleep($timer);
$outobj['persoon'] = array_slice($objects, rand(0, count($objects) - 1),1, false)[0];
$outobj['_meta'] = 'Request took '.$timer . ' seconds';
print json_encode($outobj);
