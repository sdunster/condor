from django.contrib import admin
from members.models import Rank, Qualification, Member, Unit

class RankAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'other_names')
    search_fields = ('surname', 'other_names')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

admin.site.register(Rank, RankAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Unit, UnitAdmin)