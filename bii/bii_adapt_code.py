import os
import fileinput
#estos van con ifndef

define_equivalence={"SDL.h":"latinga/sdl2/include/SDL.h",
"SDL_version.h":"latinga/sdl2/include/SDL_version.h",
"begin_code.h":"latinga/sdl2/include/begin_code.h",
"close_code.h":"latinga/sdl2/include/close_code.h>",
"SDL_error.h":"latinga/sdl2/include/SDL_error.h",
"SDL_video.h":"latinga/sdl2/include/SDL_video.h",
"SDL_endian.h":"latinga/sdl2/include/SDL_endian.h",
"jpeglib.h" : "jpeg/jpeg/jpeglib.h",
"png.h": "glenn/png/png.h",
"tiffio.h": "tiff/tiff/libtiff/tiffio.h",
"webp/decode.h": "google/libwebp/webp/decode.h"}

import sys

from tempfile import mkstemp
from shutil import move
from os import remove, close
import sys

def replace_includes(source_file_path):
    fh, target_file_path = mkstemp()
    target_file= open(target_file_path, 'w')
    source_file= open(source_file_path, 'r')
    for line in source_file:
    #check only the lines with includes
        if line.startswith("#include"):
            #replacing text
            for key in define_equivalence:
                line = line.replace(key, define_equivalence[key])
        target_file.write(line)
    target_file.close()
    close(fh)
    source_file.close()
    
    #move(target_file_path, "%s_out.txt"%source_file_path)
    remove(source_file_path)
    move(target_file_path, source_file_path)
    

    
def process_files(src_dir):
    
    for folder, subs, files in os.walk(src_dir):
        for filename in files:
            if filename.endswith(('.c','.h')):
                replace_includes(os.path.join(folder, filename))

if __name__ == '__main__':
   #process_files("test/")
   process_files("../")
   
