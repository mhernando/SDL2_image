# CMakeLists.txt

# Copyright (C) 2007-2013 Glenn Randers-Pehrson

# This code is released under the libpng license.
# For conditions of distribution and use, see the disclaimer
# and license in png.h

#############BIICODE MACROS###################
include(${CMAKE_HOME_DIRECTORY}/biicode.cmake)
INIT_BIICODE_BLOCK()
#############################################

cmake_minimum_required(VERSION 2.6)
set(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS true)


# COMMAND LINE OPTIONS


# OUR SOURCES
IF(APPLE)
	SET(IMAGEIO_SOURCE IMG_imageio.m)
ENDIF()

set(sdl2image_sources IMG.c			
	IMG_bmp.c		
	IMG_gif.c		
	IMG_jpg.c		
	IMG_lbm.c		
	IMG_pcx.c		
	IMG_png.c		
	IMG_pnm.c		
	IMG_tga.c		
	IMG_tif.c		
	IMG_xcf.c		
	IMG_xpm.c		
	IMG_xv.c		
	IMG_webp.c		
	${IMAGEIO_SOURCE}	
	miniz.h
)
macro(set_option _NAME _DESC _DEFLT)
  option(${_NAME} ${_DESC} ${_DEFLT})
  if(${_NAME})
	ADD_DEFINITIONS(-D${_NAME})
  endif()
endmacro()

set_option(LOAD_JPG  "Include Jpeg support" ON)
set_option(LOAD_TIF  "Include tif support" ON)
set_option(LOAD_WEBP  "Include webp support" ON)
set_option(LOAD_PNG  "Include png support" ON)
set_option(LOAD_BMP  "Include bmp support" ON)
set_option(LOAD_GIF  "Include gif support" ON)
set_option(LOAD_LBM  "Include lbm support" ON)
set_option(LOAD_PCX  "Include pcx support" ON)
set_option(LOAD_PNM  "Include pnm support" ON)
set_option(LOAD_TGA  "Include tga support" ON)
set_option(LOAD_XCF  "Include xcf support" ON)
set_option(LOAD_XPM  "Include xpm support" ON)
set_option(LOAD_XV  "Include xv support" ON)
ADD_DEFINITIONS(-DLOAD_JPG)


if(MSVC)
  add_definitions(-D_CRT_SECURE_NO_DEPRECATE)
endif(MSVC)

##############################################################
BII_FILTER_LIB_SRC(sdl2image_sources) 
ADD_BIICODE_TARGETS()
##############################################################

