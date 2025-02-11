# basic tests of the site.
import os


def test_front(client):
    response = client.get("/")
    print(response.data)
    assert b"hello world" in response.data
