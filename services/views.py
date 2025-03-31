from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ServiceCategory, ServiceProvider

# Create your views here.
def services(request):
    return render(request, 'services/services.html')

def service_provider(request, provider_id):
    provider = get_object_or_404(ServiceProvider, id=provider_id)
    context = {
        'service_provider': provider,
        'services': provider.services_offered.split(',') if provider.services_offered else []
    }
    return render(request, 'services/service_provider.html', context)

def service_list(request):
    # Get all categories and districts for the filter dropdowns
    categories = ServiceCategory.objects.all()
    districts = ServiceProvider.DISTRICT_CHOICES

    # Get filter parameters from the request
    category_id = request.GET.get('category')
    district = request.GET.get('district')
    search_query = request.GET.get('search', '')

    # Start with all providers
    providers = ServiceProvider.objects.all()

    # Apply filters
    if category_id:
        providers = providers.filter(category_id=category_id)
    
    if district:
        providers = providers.filter(district=district)
    
    if search_query:
        providers = providers.filter(
            Q(shop_name__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(services_offered__icontains=search_query)|
            Q(description__icontains=search_query) 
        )

    # Add pagination
    paginator = Paginator(providers, 3)  # Show 3 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'providers': page_obj,
        'categories': categories,
        'districts': districts,
        'selected_category': category_id,
        'selected_district': district,
        'search_query': search_query,
    }
    
    return render(request, 'services/service_list.html', context)