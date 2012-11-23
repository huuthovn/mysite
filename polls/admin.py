<<<<<<< HEAD
from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, { 'fields': ['question'] }),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')

=======
from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields':['question']}),
                 ('Date Information',{'fields':['pub_date'], 'classes': ['collapse']}),
                 ]

>>>>>>> d8871be3ecf852411f7eb57494ce796405c86f63
admin.site.register(Poll, PollAdmin)