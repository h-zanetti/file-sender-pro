import pytest
from django.urls import reverse

@pytest.fixture
def resposta_index(client):
    return client.get(reverse('core:index'))

def test_status_code(resposta_index):
    assert resposta_index.status_code == 200
