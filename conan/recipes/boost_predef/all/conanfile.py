from conan import ConanFile
from conan.tools.scm import Git


class Pkg(ConanFile):
    name = "boost_predef"
    homepage = "https://www.boost.org/library/latest/predef/"
    description = "This library defines a set of compiler, architecture, operating system, library, and other version numbers from the information it can gather of C, C++, Objective C, and Objective C++ predefined macros or those defined in generally available headers."
    topics = ("boost", "preprocessor", "miscellaneous")
    license = "BSL-1.0"
    url = "https://github.com/boostorg/predef"

    tool_requires = "b2/>=5.3.3.1"

    def export(self):
        git = Git(self, self.recipe_folder)
        git.coordinates_to_conandata()

    def source(self):
        git = Git(self, self.recipe_folder)
        git.checkout_from_conandata_coordinates()
