# simple-py-service

Simple container acting as a service-to-go placeholder for python scripts.

Just run the following command:
```
docker run --rm -it -p 5000:5000 -e SERVICE=SCRIPT_NAME paraita/simple-py-service:latest
```

Don't forget to replace `SCRIPT_NAME` by the name of the script you want to run:

* pyro_linecounter
* pyro_wordcounter

There is some documentation in the `examples` folder.

