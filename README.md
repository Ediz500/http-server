# Basit HTTP Sunucusu

Bu proje Python kullanılarak sıfırdan geliştirilmiş bir HTTP sunucusudur.

## Özellikler

- `GET` isteği ile statik dosya sunumu (`/static`)
- `GET /api/hello` ile JSON çıktısı
- MIME tipi yönetimi
- Çoklu bağlantı desteği (threading)

## Kullanım

```bash
docker build -t http-server .
docker run -p 8080:8080 http-server
```
