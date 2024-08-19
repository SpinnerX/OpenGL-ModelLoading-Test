from conan import ConanFile
# [requires]
# zlib/1.2.11
# glfw/3.4
# fmt/10.2.1
# spdlog/1.14.1
# glad/0.1.36
# assimp/5.4.1
# imgui/cci.20230105+1.89.2.docking
# [generators]
# CMakeDeps
# CMakeToolchain
# [layout]
# cmake_layout

class Engine3DRecipe(ConanFile):
    settings = "os", "arch", "build_type", "arch"

    # Requirements our project has
    def requirements(self):
        self.requires("spdlog/1.11.0")

