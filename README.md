# Desktop Demos

This repo contains 3 demos demonstrating how to build a native desktop app that displays a web view of a Flask server that can talk to Bitcoin hardware devices. The tricky part is getting the right dependencies installed in the `.spec` files so that all HWI dependencies are available inside the bundled binary.

## desktop

Runs a flask app as desktop app

### To run on Linux:

```
# build the binary
pyinstaller desktop.spec
# run the binary
./dist/desktop.spec
```

### To build for Windows:

```
# make sure docker is running
# pull docker container that can builds pyinstaller binaries for windows
docker pull cdrx/pyinstaller-windows
# build the binary inside ^^ docker container
docker run -v "$(pwd):/src/" --entrypoint /bin/sh cdrx/pyinstaller-windows -c "rm combined.spec enumerate.spec && /entrypoint.sh"
```

outputs to `dist/windows/desktop.exe`. [Don't yet know how to specify which .spec to use](https://github.com/cdrx/docker-pyinstaller/issues/63), so I tell the docker conatiner to delete the other ones before starting. 

## To build for Mac:

TODO

## enumerate

Creates binary that just prints output of HWI enumerate

### Linux:

```
pyinstaller enumerate.spec
./dist/enumerate
```

### Windows:

```
docker run -v "$(pwd):/src/" --entrypoint /bin/sh cdrx/pyinstaller-windows -c "rm combined.spec desktop.spec && /entrypoint.sh"
```

Outputs to `dist/windows/enumerate.exe`

### Mac:

TODO

## combined

This combines the `desktop.spec` and `enumerate.spec`: runs a flask app as desktop app which displays output of HWI enumerate. 

### Linux

```
pyinstaller combined.spec
./dist/combined
```

### Windows:

```
docker run -v "$(pwd):/src/" --entrypoint /bin/sh cdrx/pyinstaller-windows -c "rm enumerate.spec desktop.spec && /entrypoint.sh"
```

Outputs to `dist/windows/combined.exe`

### Mac:

TODO
