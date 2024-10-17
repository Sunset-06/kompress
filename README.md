# kompress
A very simple spring-boot api, which alllows you to compress and decompress files to and from .7z

There are only two endpoints, /compress and /decompress

## Why is it a spring-boot app?
Well why not?
I wanted to try out making an app that runs off of web infrastructure but actually is a native app.
To put it simply, its a gui that sends and recieves http requests. I planned  it on working somewhat similar to an electron app, if you know about it.

On starting the app, a local tomcat server is started on port 8080 of the user's device and then the ui then inteeracts with the server locally.

### To start the server, run these scripts
```
 mvn clean install

 mvn spring-boot:run
```

use ```mvn clean build``` to package the jar file.

### To test

You can use the test.rest file already included if you have the VSCode REST extension.
Alternatively use curl:

```bash
curl -X POST "http://localhost:8080/api/compress" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "filePath=/path/to/your/file&outputDir=/path/to/your/output.7z"
```

```bash
curl -X POST "http://localhost:8080/api/decompress" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "filePath=/path/to/your/output.7z&outputDir=/path/to/your/output/directory"
```

Ensure that the paths are correct.

### GUI
The ui was built in tkinter. It communicates with the rest api using the ```requests``` library. The ui files expect a theme called [Forest theme](https://github.com/rdbende/Forest-ttk-theme)

Transfer the jar file to the root of your python directory and package it with pyinstaller
```bash
pyinstaller starter.spec
```

Modify the spec file as you require.

It should work the way I packaged it, but I had dificulties running it. Weirdly enough it ran fine when the file was called from the command line. If you also have difficulties, I recommend doing the same.
