import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
@pytest.fixture
def resposta_index(client):
    return client.get(reverse('core:index'))

def test_status_code(resposta_index):
    assert resposta_index.status_code == 200

def test_form_presente(resposta_index):
    assertContains(resposta_index, f'<form action="{reverse("core:index")}" method="POST" enctype="multipart/form-data"')

def test_btn_submit_presente(resposta_index):
    assertContains(resposta_index, '<button type="submit"')