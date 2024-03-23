## Copyright 2020 Intel Corporation
## SPDX-License-Identifier: Apache-2.0

set(SUBPROJECT_NAME ispc-v1.14.1)

set(SUBPROJECT_PATH ${INSTALL_DIR_ABSOLUTE})

if (APPLE)
  set(ISPC_SUFFIX "macOS.tar.gz")
elseif(WIN32)
  set(ISPC_SUFFIX "windows.zip")
else()
  set(ISPC_SUFFIX "linux.tar.gz")
endif()

set(ISPC_URL "https://github.com/ispc/ispc/releases/download/v1.14.1/ispc-v1.14.1-${ISPC_SUFFIX}")

ExternalProject_Add(ispc
  PREFIX ${SUBPROJECT_NAME}
  STAMP_DIR ${SUBPROJECT_NAME}/stamp
  SOURCE_DIR ${SUBPROJECT_NAME}/src
  BINARY_DIR ${SUBPROJECT_NAME}
  URL ${ISPC_URL}
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND "${CMAKE_COMMAND}" -E copy_if_different
    <SOURCE_DIR>/bin/ispc${CMAKE_EXECUTABLE_SUFFIX}
    ${INSTALL_DIR_ABSOLUTE}/bin/ispc${CMAKE_EXECUTABLE_SUFFIX}
  BUILD_ALWAYS OFF
)

set(ISPC_PATH "${INSTALL_DIR_ABSOLUTE}/bin/ispc${CMAKE_EXECUTABLE_SUFFIX}")
