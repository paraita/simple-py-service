#!/usr/bin/env python

from __future__ import print_function
import Pyro4
from time import sleep
from random import randint

SIZE_10MB = 10000000
requests_list = []

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class LineCounter(object):

    def get_nb_lines(self, content):
        requests_list.append(1)
        alloc_10MB = "a" * SIZE_10MB
        sleep(randint(2, 30))
        if content:
            print("content present: {0}".format(content))
            print("request_list size: {0}".format(len(requests_list)))
            requests_list.pop()
            return {'count': len(content.split('\n'))}
        else:
            print("no content !")
            requests_list.pop()
            return {'count': 0}

    def get_load(self):
        return {'requests_in_progress': len(requests_list)}

def main():
    Pyro4.Daemon.serveSimple(
        {
            LineCounter: "example.LineCounter"
        },
        host="0.0.0.0",
        port=5000,
        ns = False)

if __name__=="__main__":
    main()
