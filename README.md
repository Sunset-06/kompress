# kompress
A very simple spring-boot api, which alllows you to compress and decompress files to and from .7z

There are only two endpoints, /compress and /decompress

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
