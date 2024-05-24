cmake_minimum_required(VERSION 3.15)
project(OpenGL-ModelLoading C CXX)

set(CMAKE_CXX_STANDARD 20)

find_package(ZLIB REQUIRED)
find_package(glfw3 REQUIRED)
find_package(glad REQUIRED)
find_package(assimp REQUIRED)

add_executable(${PROJECT_NAME} src/main.cpp)

# file(COPY backpack/ DESTINATION build)

target_link_libraries(${PROJECT_NAME}
    ZLIB::ZLIB
    glfw
    glad::glad
    assimp::assimp
)
