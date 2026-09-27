#!/usr/bin/env python3
"""Build a small, fictional watch catalog for testing Meta Commerce Manager."""

import csv
import html
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE_URL = os.environ.get(
    "BOREAL_CATALOG_BASE_URL", "https://gaonuk.github.io/boreal-demo-catalog"
).rstrip("/")

PRODUCTS = [
    {
        "id": "BD-COSTA-38",
        "slug": "costa-38",
        "title": "Boreal Demo Costa 38",
        "description": "Reloj conceptual de 38 mm con esfera marfil, caja plateada y correa de cuero color camel. Producto ficticio para pruebas de catálogo.",
        "price": "129990 CLP",
        "image": "costa-38.png",
        "details": "Esfera marfil · Caja plateada · Correa camel",
    },
    {
        "id": "BD-AZUL-40",
        "slug": "azul-40",
        "title": "Boreal Demo Azul 40",
        "description": "Reloj conceptual de 40 mm con esfera azul marino y brazalete de acero cepillado. Producto ficticio para pruebas de catálogo.",
        "price": "159990 CLP",
        "image": "azul-40.png",
        "details": "Esfera azul · Caja de acero · Brazalete de acero",
    },
    {
        "id": "BD-BOSQUE-36",
        "slug": "bosque-36",
        "title": "Boreal Demo Bosque 36",
        "description": "Reloj conceptual de 36 mm con esfera verde bosque, caja color oro rosa y correa oliva. Producto ficticio para pruebas de catálogo.",
        "price": "139990 CLP",
        "image": "bosque-36.png",
        "details": "Esfera verde · Caja oro rosa · Correa oliva",
    },
]

CSV_FIELDS = [
    "id",
    "title",
    "description",
    "availability",
    "condition",
    "price",
    "link",
    "image_link",
    "brand",
    "google_product_category",
]

STYLES = """
:root { color-scheme: light; font-family: Arial, Helvetica, sans-serif; color: #1f2b2a; background: #f3f1eb; }
* { box-sizing: border-box; }
body { margin: 0; }
header { padding: 20px max(24px, calc((100vw - 1100px) / 2)); background: #172d2c; color: #fff; display: flex; align-items: center; justify-content: space-between; gap: 20px; }
header a { color: inherit; text-decoration: none; }
.brand { font-family: Georgia, serif; font-size: 24px; letter-spacing: .05em; }
.tag { font-size: 12px; letter-spacing: .09em; text-transform: uppercase; color: #bbd3c3; }
main { max-width: 1100px; margin: auto; padding: 60px 24px 90px; }
h1, h2 { font-family: Georgia, serif; font-weight: normal; }
h1 { font-size: clamp(38px, 6vw, 68px); line-height: 1.04; margin: 0 0 18px; }
.intro { color: #5d6b68; max-width: 650px; font-size: 18px; line-height: 1.6; }
.notice { border-left: 3px solid #8a9d8f; padding: 12px 18px; background: #e8ece6; font-size: 14px; line-height: 1.5; margin: 28px 0 44px; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.card { color: inherit; text-decoration: none; background: #fff; border: 1px solid #e0dfd8; }
.card img { display: block; width: 100%; aspect-ratio: 1; object-fit: cover; }
.card div { padding: 18px 20px 22px; }
.card h2 { font-size: 24px; margin: 0 0 10px; }
.card p { margin: 0 0 12px; color: #5d6b68; }
.price { font-weight: 700; }
.product { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, .82fr); gap: 55px; align-items: center; }
.product img { width: 100%; border: 1px solid #e0dfd8; }
.product h1 { font-size: clamp(36px, 5vw, 56px); }
.product p { line-height: 1.65; }
.back { display: inline-block; margin-bottom: 28px; color: #425f55; }
.sku { color: #788580; font-size: 13px; letter-spacing: .08em; }
footer { border-top: 1px solid #d9ddd5; padding: 24px; text-align: center; color: #667570; font-size: 13px; }
@media (max-width: 720px) { .grid { grid-template-columns: 1fr; } .product { grid-template-columns: 1fr; gap: 30px; } header { padding: 20px 24px; } main { padding-top: 42px; } }
""".strip()


def page(title, content, root_prefix=""):
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Boreal Demo</title><link rel="stylesheet" href="{root_prefix}style.css"></head>
<body><header><a class="brand" href="{root_prefix}index.html">BOREAL DEMO</a><span class="tag">Catálogo de prueba</span></header>
<main>{content}</main><footer>Marca y productos ficticios para pruebas privadas de integración. No se aceptan compras.</footer></body></html>
"""


def main():
    (ROOT / "style.css").write_text(STYLES + "\n", encoding="utf-8")
    cards = []
    for product in PRODUCTS:
        cards.append(
            f'<a class="card" href="products/{product["slug"]}.html"><img src="assets/{product["image"]}" alt="{html.escape(product["title"])}">'
            f'<div><h2>{html.escape(product["title"])}</h2><p>{html.escape(product["details"])}</p>'
            f'<span class="price">{html.escape(product["price"])}</span></div></a>'
        )
        content = (
            '<a class="back" href="../index.html">← Volver al catálogo</a>'
            f'<div class="product"><img src="../assets/{product["image"]}" alt="{html.escape(product["title"])}">'
            f'<div><p class="sku">{html.escape(product["id"])}</p><h1>{html.escape(product["title"])}</h1>'
            f'<p>{html.escape(product["description"])}</p><p>{html.escape(product["details"])}</p>'
            f'<p class="price">Precio ilustrativo: {html.escape(product["price"])}</p>'
            '<div class="notice">Este es un producto conceptual para probar el catálogo y los mensajes de WhatsApp. No está a la venta.</div>'
            '</div></div>'
        )
        (ROOT / "products" / f"{product['slug']}.html").write_text(
            page(product["title"], content, "../"), encoding="utf-8"
        )

    index = (
        '<h1>Relojes para explorar<br>la integración.</h1>'
        '<p class="intro">Tres modelos conceptuales para probar la carga de productos y el catálogo de WhatsApp.</p>'
        '<div class="notice">Este sitio es una demostración técnica. Los relojes y sus precios son ficticios; no se aceptan compras.</div>'
        f'<section class="grid">{"".join(cards)}</section>'
    )
    (ROOT / "index.html").write_text(page("Catálogo", index), encoding="utf-8")

    with (ROOT / "catalogo-boreal-demo.csv").open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for product in PRODUCTS:
            writer.writerow(
                {
                    "id": product["id"],
                    "title": product["title"],
                    "description": product["description"],
                    "availability": "in stock",
                    "condition": "new",
                    "price": product["price"],
                    "link": f"{BASE_URL}/products/{product['slug']}.html",
                    "image_link": f"{BASE_URL}/assets/{product['image']}",
                    "brand": "Boreal Demo",
                    "google_product_category": "Apparel & Accessories > Jewelry > Watches",
                }
            )


if __name__ == "__main__":
    main()
