pkgname=panic
pkgver=1.0
pkgrel=1
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

source=("https://github.com/whyisthesheep/panic/releases/download/$pkgver/panic-$pkgver.tar.gz")
sha256sums=("2e669433e98a0636456701c67ff6ab6bd3d0e57b85ebc44d6ca7762633c357eb")

package() {
	cd "$srcdir"
    
    install -Dm755 panic.py "$pkgdir/usr/bin/panic.py"

    install -Dm755 panic "$pkgdir/usr/bin/panic"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
