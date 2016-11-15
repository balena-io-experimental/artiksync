#!/usr/bin/env python

from time import sleep

target = 5
max = 10

for x in range(0, max):
  print ("Testing %d" % x)
  if x == target:
    print "Hit the target!"

while True:
  sleep(5)
