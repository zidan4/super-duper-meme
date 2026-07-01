import os

root = input( "Search in: " )
name = input( "File name: " )

for path, _, files in os.walk( root ):
  if name in files:
    print( "Found at: ", + os.path.join( path, name ) )
    break
  else:
    print( "Not Found" )