import pytest
from .eventos_repository import EventosRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
    event_name = "eventoTeste1"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Insert in DB")
def test_insert_eventos2():
    event_name = "eventoTeste2"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Insert in DB")
def test_insert_eventos3():
    event_name = "eventoTeste3"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Select in DB")
def test_select_event():
    event_name = "eventoTeste2"
    event_repo = EventosRepository()

    event = event_repo.select_event(event_name)
    print(event)
    print("O evento buscado foi o:", event.nome, "Com o ID:", event.id)