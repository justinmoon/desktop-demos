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
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```

outputs to `dist/desktop.exe`

## enumerate

Creates binary that just prints output of HWI enumerate

### Linux:

```
pyinstaller enumerate.spec
./dist/enumerate
```

### Windows:

```
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```

## combined

This combines the `desktop.spec` and `enumerate.spec`: runs a flask app as desktop app which displays output of HWI enumerate. 

### Linux

```
pyinstaller combined.spec
./dist/combined
```

### Windows:

```
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```
