# Maintainer: Victor Roest <victor@xirion.net>
pkgname=dice-roller
pkgver=61841c1
pkgrel=1
pkgdesc="A python dice rolling application using standard dice notation"
url="https://git.xirion.net/victor/dice-roller"
depends=('python')
makedepends=('git' 'python')
arch=('i686' 'x86_64')
conflicts('')
provides=('dice-roller')
source=(git://git.xirion.net/victor/dice-roller.git)
sha256sums=('SKIP')

pkgver() {
    cd ${pkgname}
    git rev-parse --short HEAD
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir"
}
