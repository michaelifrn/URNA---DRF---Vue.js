from django.contrib import admin
from .models import Candidate, Vote, Voters

admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Voters)
