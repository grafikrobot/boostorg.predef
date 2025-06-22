from conan import ConanFile
from conan.tools.scm import Git


class Pkg(ConanFile):
    name = "boost_predef"

    # Metadata
    homepage = "https://www.boost.org/library/latest/predef/"
    description = "This library defines a set of compiler, architecture, operating system, library, and other version numbers from the information it can gather of C, C++, Objective C, and Objective C++ predefined macros or those defined in generally available headers."
    topics = ("boost", "preprocessor", "miscellaneous")
    license = "BSL-1.0"
    url = "https://github.com/boostorg/predef"

    # Requirements
    # python_requires = "b2/[>=5.3.3.1]"

    # Folders and layout
    # no_copy_source = True

    # Internal
    _header_only = True

    # @property
    # def b2(self):
    #     if not hasattr(self, "_b2") or not self._b2:
    #         self._b2 = self.python_requires["b2"].B2(self)
    #     return self._b2

    def package_id(self):
        if self._header_only:
            self.info.clear()

    # def layout(self):
    #     # self.b2.layout(header_only=self._header_only)
    #     pass

    # def generate(self):
    #     self.b2.generate(header_only=self._header_only)

    def export(self):
        git = Git(self, self.recipe_folder)
        git.coordinates_to_conandata()

    def source(self):
        git = Git(self, self.recipe_folder)
        git.checkout_from_conandata_coordinates()

    # def package(self):
    #     self.b2.install(target=["install"])

    def package_info(self):
        if self._header_only:
            self.cpp_info.bindirs = []
            self.cpp_info.libdirs = []
