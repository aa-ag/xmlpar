use strict;
use warnings;

use XML::Simple;

my $xml = q{[...]};

my $data = XMLin($xml)

print $data -> {[...]}, "\n"