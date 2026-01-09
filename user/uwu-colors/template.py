pkgname = "uwu-colors"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Simple language server to colorize hex color strings"
license = "Unlicense"
url = "https://github.com/q60/uwu_colors"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "558e2a4d13775b81727a41ba9bb157dd8d0f52449845b0386cbb9a474708920d"


def post_install(self):
    self.install_license("license")
