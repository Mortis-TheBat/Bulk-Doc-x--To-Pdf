# Bulk-Docx-To-Pdf
Converts all .docx or .doc to PDF!

**Converting .docx files **
Use Python script for converting docx files

**Converting .doc files **
For .doc files, you need a Linux environment.
We will use removeSpaces.sh to convert (say) "James Bond.doc" to "James_Bond.doc". It is always recommended not to haev spaces between files (:
After removing the spaces, we execute the convertToPdf.sh to convert our doc files to PDF

Make the file executable using-
```chmod +x removeSpaces.sh``` and ```chmod +x converToPdf.sh```

Execute it using-
```./removeSpaces.sh``` and ```./converToPdf.sh```

(Don't forget to change to the direcotry where the script is!)

