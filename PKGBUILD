pkgname=panic
pkgver=1.1
pkgrel=2
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

source=("https://github.com/whyisthesheep/panic/releases/download/$pkgver/panic-$pkgver.tar.gz")
sha256sums=("d651463fa767491cf90a3c00167557dd942371e1b4f1c3a7ad9eeaa4841ad5e5")

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"
    install -Dm755 panic "$pkgdir/usr/bin/panic"
}
