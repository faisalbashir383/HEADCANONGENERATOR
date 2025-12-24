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
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://headcanongenerator.world/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/about/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/privacy/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/terms/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>https://headcanongenerator.world/contact/</loc>
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
