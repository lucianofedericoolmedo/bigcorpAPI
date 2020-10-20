from __future__ import unicode_literals
from django.db import models
from django.db.models import Q


class AnimalManager(models.Manager):
    def search_only_name(self, search):
        return self.filter(name__icontains=search)
    
    def search_only_race(self, search):
        return self.filter(race__icontains=search)
    
    def search_only_species(self, search):
        return self.filter(species__name__icontains=search)
    
    def search_only_name_and_race(self, search):
        return self.filter(Q(name__contains=search) |
            Q(race__contains=search))
    
    def search_only_race_and_species(self, search):
        return self.filter(Q(race__contains=search) |
            Q(species__name__contains=search))
    
    def search_only_name_and_species(self, search):
        return self.filter(Q(name__contains=search) |
            Q(species__name__contains=search))
    
    def search_only_name_race_and_species(self, search):
        return self.filter(Q(name__contains=search) | Q(race__contains=search) |
            Q(species__name__contains=search))