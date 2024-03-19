pkgname=panic
pkgver=1.2
pkgrel=3
pkgdesc="The scariest AUR helper"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"
    install -Dm755 panic "$pkgdir/usr/bin/panic"
}
