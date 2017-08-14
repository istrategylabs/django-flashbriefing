import datetime
import json
import random

import pytest
from flashbriefing.models import Feed, Item


@pytest.mark.django_db
def test_jsonfeed_single(client):
    feed = Feed.objects.create(title='FEED')
    Item.objects.create(
        feed=feed, title='ITEM', audio_content='/audio.mp3',
        published_date=datetime.datetime.utcnow())
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    assert isinstance(data, dict)


@pytest.mark.django_db
def test_jsonfeed_multiple(client):
    feed = Feed.objects.create(title='FEED')
    Item.objects.create(
        feed=feed, title='ITEM-1', published_date=datetime.datetime.utcnow())
    Item.objects.create(
        feed=feed, title='ITEM-2', published_date=datetime.datetime.utcnow())
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    assert isinstance(data, list)


@pytest.mark.django_db
def test_jsonfeed(client):
    feed = Feed.objects.create(title='FEED')
    resp = client.get('/briefings/feeds/{}.json'.format(feed.uuid))
    assert resp.status_code == 200
    assert resp['Content-Type'] == 'application/json'


@pytest.mark.django_db
def test_rssfeed(client):
    feed = Feed.objects.create(title='FEED')
    resp = client.get('/briefings/feeds/{}.rss'.format(feed.uuid))
    assert resp.status_code == 404


@pytest.mark.django_db
def test_published_date(client):
    feed = Feed.objects.create(title='FEED')
    Item.objects.create(
        feed=feed, title='ITEM-1',
        published_date=datetime.datetime(2017, 1, 1, 16, 20, 0))
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    assert data['updateDate'] == '2017-01-01T16:20:00.0Z'


@pytest.mark.django_db
def test_max_5(client):
    feed = Feed.objects.create(title='FEED')
    for i in range(10):
        Item.objects.create(
            feed=feed, title='ITEM-{}'.format(i),
            published_date=datetime.datetime(2017, 1, i + 1, 16, 20, 0))
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    assert len(data) == 5


@pytest.mark.django_db
def test_feed_order(client):
    feed = Feed.objects.create(title='FEED')
    for i in range(10):
        day = random.randint(1, 30)
        Item.objects.create(
            feed=feed, title='ITEM-{}'.format(i),
            published_date=datetime.datetime(2017, 1, day, 16, 20, 0))
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    dates = [d['updateDate'] for d in data]
    assert dates == sorted(dates, reverse=True)


@pytest.mark.django_db
def test_no_markup(client):
    feed = Feed.objects.create(title='FEED')
    Item.objects.create(
        feed=feed, title='ITEM-1',
        text_content='a <div>b</div>',
        published_date=datetime.datetime(2017, 1, 1, 16, 20, 0))
    resp = client.get(feed.get_absolute_url())
    data = resp.json() if hasattr(resp, 'json') else json.loads(resp.content)
    assert data['mainText'] == 'a b'
