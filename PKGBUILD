pkgname=panic
pkgver=1.0
pkgrel=1
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

source=("https://github.com/whyisthesheep/panic/releases/download/$pkgver/panic-$pkgver.tar.gz")
sha256sums=("7fef59f7743f45c12732f5bbc903a0db2bf655522eb3bdc8f1a11208a597d6a1")

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"

    install -Dm755 panic "$pkgdir/usr/bin/panic"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
