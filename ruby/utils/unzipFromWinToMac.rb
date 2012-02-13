require 'zip/zip'
require 'iconv'

# To unzip zipfile which zip in GBK to UTF-8.
#
# When you zip a file on Windows, it will encode in GBK default.
# Then you unzip it on Mac OSX which use unicode default, it will be wrong.
# This code is used to fix this problem:)
#
# @Author: jiang-bo
Zip::ZipInputStream::open(zipFile){
  |io|
  while(entry = io.get_next_entry)
    name=Iconv.iconv("UTF-8","GBK", entry.name)[0]

    puts "Extracting #{name}"
    if name.end_with?('/')
      Dir.mkdir(name.to_s)
    else
      entry.extract(name.to_s)
    end
  end
}
