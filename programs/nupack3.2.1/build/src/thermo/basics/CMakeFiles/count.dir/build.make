# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.9.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.9.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build

# Include any dependencies generated for this target.
include src/thermo/basics/CMakeFiles/count.dir/depend.make

# Include the progress variables for this target.
include src/thermo/basics/CMakeFiles/count.dir/progress.make

# Include the compile flags for this target's objects.
include src/thermo/basics/CMakeFiles/count.dir/flags.make

src/thermo/basics/CMakeFiles/count.dir/count.c.o: src/thermo/basics/CMakeFiles/count.dir/flags.make
src/thermo/basics/CMakeFiles/count.dir/count.c.o: ../src/thermo/basics/count.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/thermo/basics/CMakeFiles/count.dir/count.c.o"
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/count.dir/count.c.o   -c /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/thermo/basics/count.c

src/thermo/basics/CMakeFiles/count.dir/count.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/count.dir/count.c.i"
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/thermo/basics/count.c > CMakeFiles/count.dir/count.c.i

src/thermo/basics/CMakeFiles/count.dir/count.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/count.dir/count.c.s"
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/thermo/basics/count.c -o CMakeFiles/count.dir/count.c.s

src/thermo/basics/CMakeFiles/count.dir/count.c.o.requires:

.PHONY : src/thermo/basics/CMakeFiles/count.dir/count.c.o.requires

src/thermo/basics/CMakeFiles/count.dir/count.c.o.provides: src/thermo/basics/CMakeFiles/count.dir/count.c.o.requires
	$(MAKE) -f src/thermo/basics/CMakeFiles/count.dir/build.make src/thermo/basics/CMakeFiles/count.dir/count.c.o.provides.build
.PHONY : src/thermo/basics/CMakeFiles/count.dir/count.c.o.provides

src/thermo/basics/CMakeFiles/count.dir/count.c.o.provides.build: src/thermo/basics/CMakeFiles/count.dir/count.c.o


# Object files for target count
count_OBJECTS = \
"CMakeFiles/count.dir/count.c.o"

# External object files for target count
count_EXTERNAL_OBJECTS =

bin/count: src/thermo/basics/CMakeFiles/count.dir/count.c.o
bin/count: src/thermo/basics/CMakeFiles/count.dir/build.make
bin/count: lib/libnupackpfunc.a
bin/count: lib/libnupackutils.a
bin/count: /usr/lib/libm.dylib
bin/count: src/thermo/basics/CMakeFiles/count.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../../../bin/count"
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/count.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/thermo/basics/CMakeFiles/count.dir/build: bin/count

.PHONY : src/thermo/basics/CMakeFiles/count.dir/build

src/thermo/basics/CMakeFiles/count.dir/requires: src/thermo/basics/CMakeFiles/count.dir/count.c.o.requires

.PHONY : src/thermo/basics/CMakeFiles/count.dir/requires

src/thermo/basics/CMakeFiles/count.dir/clean:
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics && $(CMAKE_COMMAND) -P CMakeFiles/count.dir/cmake_clean.cmake
.PHONY : src/thermo/basics/CMakeFiles/count.dir/clean

src/thermo/basics/CMakeFiles/count.dir/depend:
	cd /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1 /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/src/thermo/basics /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics /Users/sven/Desktop/IGEM/Program/progress/nupack/nupack3.2.1/build/src/thermo/basics/CMakeFiles/count.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/thermo/basics/CMakeFiles/count.dir/depend

