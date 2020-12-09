#!/usr/bin/perl
use LWP::Simple;

$xml = get "https://w1.weather.gov/xml/current_obs/KORD.xml";

@lines = split(/\n/, $xml);

foreach $line (@lines) {
    if ($line =~ /<([^>]+)>([^<]*)<\/([^>]+)>/) {
        print "$1: $2\n";
    }
}