from django.contrib.syndication.views import Feed

class Blog(Feed):
    title = 'Latest Blog Entries'
    link = 'http://blog.lightcastletech.com/feed'
    description = 'Latest entries'

    def items(self):
        return Blog.new#['poop', 'django', 'goes', 'word']#get_items("/blogs")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
