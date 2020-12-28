#Replace "./" with specified location if required
filesDir=`ls ./*.doc`


#Searches all .doc files and converts to PDF
for eachDoc in $filesDir
do
   echo $eachDoc
   lowriter --headless --convert-to pdf "$eachDoc"
done

#Uncomment to delete all the converted .doc files 
for deletable in $filesDir
do
   find . -name "*.doc" -type f -delete
done
