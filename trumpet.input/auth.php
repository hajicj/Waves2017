<?php

require "vendor/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

define("CONSUMER_KEY", "Ofyur5Kd5ze4r8saxkeQa3HTx");
define("CONSUMER_SECRET", "kMwOhAzlyYMxLmteNHbjhg6YiZKkWj3RlGAvicLIjUUsaffpyr");

$access_token = "200202652-3hi7m2yJzmWPCS6TAZBf1f6QJ1UlopUO7B0LzkXw";
$access_token_secret = "6ULNn4MtbTXJeScaDfFSYYPRKRj1fCm0x8p8a8tr8pogr";

$connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, $access_token, $access_token_secret);
$content = $connection->get("account/verify_credentials");

$statuses = $connection->get("statuses/user_timeline", ["count" => 200, "screen_name" => 
"realdonaldtrump", "exclude_replies" => true]);

file_put_contents("cache/tweets_realdonaldtrump.json", json_encode($statuses));