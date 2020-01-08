import sys

  #if(buildID == "current"):
  #  print("Because this is being executed against the 'current' folder")
  #  print("Only the QA/QC procedures will be implemented.  No full build will be")
  #  print("produced.")

#################
##Build stage 1 - individual shapes
#################
#(1) Extract all shape boundaries (each row in the metadata file) into the following hierarchy:
#geoBoundaries-2-0-0_init
###JPN
####ADM0
####ADM1

#(2) For each shapefile, run any final buffer 0 needed and standardize the schema of the attributes.
#shapeID - i.e., 'AFG-ADM1-2-0-0-B1' The boundary ID, followed bythe letter ‘B’ and a 
#unique in-teger for each shape which is amember of that boundary
#shapeName
#shapeGroup
#shapeYear
#shapeType

#(3) For each row, run final stage builds that normalize all rows in the metadatabase:
#A standardization for each row in the metadatabase, so they include:
#Boundary ID - ISO 3166-1 3 letter + geoBoundaries version.  If collision would occur, abbreviated source.
#Boundary ISO - 3 letter ISO
#Boundary Group - 3 letter ISO (if a country)
#Year - Year boundary is representative
#Boundary Type - type of boundary (i.e., "Administrative District Hierarchy Level 3")
#Source K - the sources
#License
#License Detail
#License Source
#Link to Source Data
#Last Updated - ISO 8601
#Download URL (the geoboundaries.org URL)

#(4) For each row, run final stage builds and generate products in new root folder:
#geoBoundaries-2-0-0
###JPN
####ADM0
#####geoBoundaries-2-0-0-JPN-ADM0.json
#####geoBoundaries-2-0-0-JPN-ADM0.pdf
#####geoBoundaries-2-0-0-JPN-ADM0.geojson
#####geoBoundaries-2-0-0-JPN-ADM0-shp.zip

#(5) For each group, build the "aggregate" zipfiles:
#geoBoundaries-2-0-0
##JPN
###geoBoundaries-2-0-0-JPN.zip
####ADM0
#####geoBoundaries-2-0-0-JPN-ADM0-all.zip

#6 Generate the "ALL" group
###ALL
####ADM0

#7 Generate the overall geoBoundaries-2-0-0.zip file.
#geoBoundaries-2-0-0
##geoBoundaries-2-0-0.zip

#8 Generate a CITATION AND USE.TXT document for inclusion in the top level.

#9 Upload to geoBoundaries.org, mirroring folder structure.