#Note:To ensure that the exact files desired are included in a build,
#it is required the user manually upload a single zipFile.  
#The zip file should be a *copy* of everything in "current".
#Note the metadata file must be in excel format.
#We hope to move off of Google Drive for data store one day soon.
#When that happens, we can potentially build a full pipeline at this stage.


#(1) Extract all shape boundaries (each row in the metadata file) 
#into the following hierarchy:
#geoBoundaries-2-0-0_init
###JPN
####ADM0
####ADM1