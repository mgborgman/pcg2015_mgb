from django.contrib.syndication.views import Feed
from mattborgman.models import Entry


class LatestPosts(Feed):
    title = "Matt's Blog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]

