# Install script for directory: /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/thermo/basics

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/count")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/count" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/count")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/count")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/count")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/complexdefect")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/complexdefect" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/complexdefect")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/complexdefect")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/complexdefect")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/energy")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/energy" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/energy")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/energy")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/energy")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/mfe")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/mfe" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/mfe")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/mfe")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/mfe")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/pairs")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pairs" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pairs")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pairs")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pairs")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/pfunc")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pfunc" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pfunc")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pfunc")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/pfunc")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/prob")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/prob" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/prob")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/prob")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/prob")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/subopt")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/subopt" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/subopt")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/subopt")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/subopt")
    endif()
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/bin/sample")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/sample" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/sample")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/sample")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/sample")
    endif()
  endif()
endif()

