package com.nilay.kompress;

import org.apache.commons.compress.archivers.ArchiveEntry;
import org.apache.commons.compress.archivers.sevenz.SevenZArchiveEntry;
import org.apache.commons.compress.archivers.sevenz.SevenZFile;
import org.apache.commons.compress.archivers.sevenz.SevenZOutputFile;
import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

@RestController
@RequestMapping("/api")
public class Controller {

    @PostMapping("/compress")
    public String compress(@RequestParam("filePath") String filePath, @RequestParam("outputPath") String outputPath) throws IOException {
        compressFile(filePath, outputPath);
        return "File compressed successfully!";
    }

    @PostMapping("/decompress")
    public String decompress(@RequestParam("filePath") String filePath, @RequestParam("outputDir") String outputDir) throws IOException {
        decompressFile(filePath, outputDir);
        return "File decompressed successfully!";
    }

    private void compressFile(String sourceFilePath, String outputFilePath) throws IOException {
        File sourceFile = new File(sourceFilePath);
        try (SevenZOutputFile sevenZOutput = new SevenZOutputFile(new File(outputFilePath));
             FileInputStream fis = new FileInputStream(sourceFile)) {
            
            SevenZArchiveEntry entry = sevenZOutput.createArchiveEntry(sourceFile, sourceFile.getName());
            sevenZOutput.putArchiveEntry(entry);

            byte[] buffer = new byte[1024];
            int len;
            while ((len = fis.read(buffer)) > 0) {
                sevenZOutput.write(buffer, 0, len);
            }

            sevenZOutput.closeArchiveEntry();
        }
    }

    private void decompressFile(String archiveFilePath, String outputDirPath) throws IOException {
        File archiveFile = new File(archiveFilePath);
        File outputDir = new File(outputDirPath);
        if (!outputDir.exists()) {
            outputDir.mkdirs();
        }

        try (SevenZFile sevenZFile = new SevenZFile(archiveFile)) {
            ArchiveEntry entry;
            while ((entry = sevenZFile.getNextEntry()) != null) {
                File outputFile = new File(outputDir, entry.getName());

                try (FileOutputStream fos = new FileOutputStream(outputFile)) {
                    byte[] buffer = new byte[1024];
                    int len;
                    while ((len = sevenZFile.read(buffer)) > 0) {
                        fos.write(buffer, 0, len);
                    }
                }
            }
        }
    }
}
