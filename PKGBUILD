pkgname=panic
pkgver=1.1
pkgrel=2
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

source=("https://github.com/whyisthesheep/panic/releases/download/$pkgver/panic-$pkgver.tar.gz")
sha256sums=("a89e7350a230af4676ceac886d578bdcd242a1c13318818b5122de15e64ba2d6")

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"
    install -Dm755 panic "$pkgdir/usr/bin/panic"
}
