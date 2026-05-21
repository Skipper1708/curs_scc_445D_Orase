from app.lib.biblioteca_orase import descriere_bucuresti, populatie_bucuresti


def test_descriere_bucuresti():
    rezultat = descriere_bucuresti()
    assert "București" in rezultat
    assert "capitala României" in rezultat


def test_populatie_bucuresti():
    rezultat = populatie_bucuresti()
    assert "București" in rezultat
    assert "populație" in rezultat
