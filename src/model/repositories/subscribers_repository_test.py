import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subcriber_info = {
        "name": "Caio Vitor",
        "email": "caiovitorlchaves@email.com",
        "evento_id": 11
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subcriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "caiovitorlchaves@email.com"
    evento_id = 11

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print("O inscrito buscado foi o:", resp.nome)

@pytest.mark.skip("Select in DB")
def test_ranking():
    evento_id = 11
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()

    for elem in resp:
        print(f"Link: {elem.link}, Total de Inscritos: {elem.Total}")