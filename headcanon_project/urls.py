"""
URL configuration for headcanon_project.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://headcanongenerator.world/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')

def sitemap_xml(request):
    from datetime import date
    today = date.today().isoformat()
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://headcanongenerator.world/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/what-is-headcanon/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/canon-vs-headcanon/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/headcanon-examples/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/random-headcanon-generator/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/character-headcanon-generator/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/anime-headcanon-generator/</loc>
        <lastmod>2024-12-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/ship-headcanon-generator/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/about/</loc>
        <lastmod>2024-12-24</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/privacy/</loc>
        <lastmod>2024-12-24</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/terms/</loc>
        <lastmod>2024-12-24</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/contact/</loc>
        <lastmod>2024-12-24</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.4</priority>
    </url>
</urlset>
"""
    return HttpResponse(content, content_type='application/xml')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generator.urls')),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]
