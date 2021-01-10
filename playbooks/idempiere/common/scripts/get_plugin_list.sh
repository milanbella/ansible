#!/usr/bin/expect -f
spawn telnet localhost 12612
expect "osgi>"
send ss\r
expect "osgi>"
close
