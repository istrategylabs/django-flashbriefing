import datetime

import pytest
from flashbriefing.models import Feed, Item


@pytest.mark.django_db
def test_item_type_audio():
    feed = Feed.objects.create(title='FEED')
    item = Item.objects.create(
        feed=feed, title='ITEM', audio_content='/audio.mp3',
        published_date=datetime.datetime.utcnow())
    assert item.item_type == Item.TYPE_AUDIO


@pytest.mark.django_db
def test_item_type_text():
    feed = Feed.objects.create(title='FEED')
    item = Item.objects.create(
        feed=feed, title='ITEM', published_date=datetime.datetime.utcnow())
    assert item.item_type == Item.TYPE_TEXT
