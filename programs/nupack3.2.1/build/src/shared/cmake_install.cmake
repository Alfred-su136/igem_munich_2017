# Install script for directory: /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib/libnupackutils.a")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnupackutils.a" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnupackutils.a")
    execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/ranlib" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnupackutils.a")
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/nupack/shared" TYPE FILE FILES
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/constants.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/externals.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/functions.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/hash.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/mt19937ar.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/nupack_design_constants.h"
    "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/shared/structs.h"
    )
endif()

