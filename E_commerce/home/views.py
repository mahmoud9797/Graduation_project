import markdown
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Home view for the MerchFlow API
def home(request):
    # Define all API endpoints with names and URLs
    endpoints = [
        {"name": "Admin Panel", "url": "/admin/"},
        {"name": "Products API", "url": "/api/products/"},
        {"name": "Reviews API", "url": "/api/reviews/"},
        {"name": "Router API", "url": "/api/"},
        {"name": "Token Obtain Pair", "url": "/api/token/"},
        {"name": "Token Refresh", "url": "/api/token/refresh/"},
        {"name": "API Schema", "url": "/api/schema/"},
        {"name": "testing", "url": "/api/schema/docs/"},
        {"name": "DocUI", "url": "/api/schema/redoc/"},
        {"name": "Documentation", "url": "/docs"}
    ]

    # A description about the MerchFlow API
    description = (
        "Welcome to the MerchFlow API Documentation! MerchFlow is your all-in-one "
        "eCommerce engine, built to handle everything from user accounts to product "
        "management, order processing, and beyond. With a robust backend powered by "
        "Django, imagine effortlessly integrating your eCommerce operations into your "
        "application. Whether you're managing customer accounts, creating product catalogs, "
        "or automating order fulfillment, MerchFlow has you covered. Its clean, consistent "
        "API design makes it a breeze to get started, so you can focus on building amazing "
        "shopping experiences."
    )

    # Render the HTML template with the context data
    return render(request, "home.html", {"endpoints": endpoints, "description": description})


def documentation(request):
    # Load the README.md file
    readme_path = settings.BASE_DIR / "README.md"
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(content, extensions=["fenced_code", "codehilite", "tables"])

    # Render the HTML in the template
    return render(request, "documentation.html", {"content": html_content})
