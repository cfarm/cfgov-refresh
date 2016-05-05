from itertools import chain

from .. import forms
from .util import get_secondary_nav_items
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from ..models import base, molecules, organisms
from ref import choices_for_page_type
from ..models import CFGOVPage
from ..models.learn_page import AbstractFilterPage


class FilterableListMixin(object):
    # Returns a queryset of AbstractFilterPages
    def get_page_set(self, form, hostname):
        return AbstractFilterPage.objects.live_shared(hostname).child_of(
            self).filter(form.generate_query()).distinct().order_by('-date_published')


    # Returns a form class to use for the filterable list
    def get_form_class(self):
        return forms.FilterableListForm


    def get_context(self, request, *args, **kwargs):
        context = super(FilterableListMixin, self).get_context(request, *args, **kwargs)
        context['get_secondary_nav_items'] = get_secondary_nav_items

        context['forms'] = []
        form_class = self.specific.get_form_class()
        form_specific_filters = self.get_form_specific_filter_data(form_class, request.GET)
        forms = [form_class(form_specific_filters[filters_id], parent=self, hostname=request.site.hostname)
                 for filters_id in form_specific_filters.keys()]
        for form in forms:
            if form.is_valid():
                paginator = Paginator(self.get_page_set(form, request.site.hostname), self.per_page_limit())
                self = request.GET.get('page')

                # Get the page number in the request and get the page from the
                # paginator to serve.
                try:
                    posts = paginator.page(self)
                except PageNotAnInteger:
                    posts = paginator.page(1)
                except EmptyPage:
                    posts = paginator.page(paginator.num_pages)

                context.update({'posts': posts})
            context['forms'].append(form)
        return context


    # Transform each GET parameter key from unique ID for the form in the
    # request and assign it to a dictionary under the form ID from where it
    # came from.
    def get_form_specific_filter_data(self, form_class, request_dict):
        filters_data = {}
        # Find every form existing on the page and assign a dictionary with its
        # number as the key.
        for i, block in enumerate(self.content):
            if 'filter_controls' in block.block_type:
                filters_data[i] = {}

        # For each form ID dictionary, find all the fields for it. Assign the
        # select fields to lists and append them for each selection. Return the
        # dictionary of normalized field names with their respective data.
        for i in filters_data.keys():
            for field in form_class.declared_fields:
                request_field_name = 'filter' + str(i) + '_' + field
                if field in ['categories', 'topics', 'authors']:
                    filters_data[i][field] = \
                        request_dict.getlist(request_field_name, [])
                else:
                    filters_data[i][field] = \
                        request_dict.get(request_field_name, '')
        return filters_data


    def has_active_filters(self, request, index):
        active_filters = False;
        form_class = self.get_form_class()
        forms_data = self.get_form_specific_filter_data(form_class, request.GET)
        if forms_data:
            for filters in forms_data[index].values():
                for value in filters:
                    if value:
                        active_filters = True

        return active_filters


    def per_page_limit(self):
        return 10
