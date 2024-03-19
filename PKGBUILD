pkgname=panic
pkgver=1.0
pkgrel=1
pkgdesc="AUR helper tool for managing packages"
arch=('any')
url="https://github.com/whyisthesheep/panic"
license=('GPL3')
depends=('python' 'auracle-git')

source=("https://github.com/whyisthesheep/panic/releases/download/$pkgver/panic-$pkgver.tar.gz")
sha256sums=("5c71f436a332790b3c0df6af636c58ebb432bf106e43b1fe4295392c3874c46c")

package() {
    cd "$srcdir/panic-$pkgver"
    
    install -Dm755 main.py "$pkgdir/usr/bin/panic"

    install -Dm755 panic "$pkgdir/usr/bin/panic"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
