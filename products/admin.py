from django.contrib import admin

from .models import Book, Category, Subcategory, Author, Publisher, BookImage


class BookInline(admin.StackedInline):
    model = Book
    classes = ['collapse']
    extra = 0


class CategoryInline(admin.TabularInline):
    model = Category
    classes = ['collapse']
    extra = 0


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    classes = ['collapse']
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_help_text = "You can search for ISBN, book's title and description or author's name"
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ['isbn', 'title', 'author', 'publisher', 'price', 'main_image']}),

        ('Categories', {
            'fields': [('category', 'subcategory'), ]}),

        ('Details', {
            'fields': ['cover', 'dimensions',
                       'year', 'pages', 'available_count',
                       'description', ]}),
        ('Other', {
            'fields': ['slug',]
        })
    )
    list_display = ('isbn', 'title', 'author', 'category',
                    'price', 'available_count', 'year', 'rating')
    list_display_links = ('isbn', 'title')
    list_filter = ('author__full_name', 'category__name', 'subcategory__name', 'publisher__name', 'year',
                   'cover')

    search_fields = ('isbn', 'title', 'author__full_name', 'description', 'publisher__name')


class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 50
    prepopulated_fields = {'slug': ('full_name',)}
    fieldsets = (
        (None, {
            'fields': ['full_name', 'country', 'description']
        }),
        ('Lifetime', {
            'fields': ['birth_date', 'death_date'],
        }),
        ('Other', {
            'fields': ['slug',]
        })
    )
    inlines = (BookInline,)
    list_display = ('id', 'full_name', 'country', 'rating')
    list_filter = ('country', 'rating')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name',)
    search_help_text = "You can search for author's name"


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    search_help_text = "You can search for category's name"
    inlines = (SubcategoryInline, BookInline)


class SubcategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'category')
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    inlines = (BookInline,)
    search_fields = ('name',)
    search_help_text = "You can search for subcategory's name"


class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug')
    list_display = ('id', 'name', 'rating')
    list_display_links = ('id', 'name')
    list_filter = ('rating', 'rating')
    search_fields = ('name',)
    search_help_text = "You can search for publisher's name"


class BookImageAdmin(admin.ModelAdmin):
    fields = ('book', 'image')
    list_display = ('id', 'book', 'image')
    list_filter = ('book__title', )
    search_fields = ('book__title', 'book__isbn')
    search_help_text = "You can search for book's title or isbn"


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(BookImage, BookImageAdmin)
