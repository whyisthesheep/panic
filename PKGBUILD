pkgname=panic
pkgver=1.1
pkgrel=2
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"
    install -Dm755 panic "$pkgdir/usr/bin/panic"
}
