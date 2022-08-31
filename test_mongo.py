import pytest
from myMongo import Mongo

list = ['ofek','yuval','alon','dan']

def test_round_insertion():
    db = Mongo()
    list = ['ofek','yuval','alon','dan']
    db.insert_round(list)
    ans = db.get_recent_round()
    print(ans)
    assert ans['queue'] == list
    list = ['yuval','gavri','ofek']
    db.insert_round(['yuval','gavri','ofek'])
    ans = db.get_recent_round()
    print(ans)
    assert ans['queue'] == list 

def test_get_users():
    db = Mongo()
    print(f"\ndata for the input keva:\n ------\n {db.get_users('keva')}")
    print(f"data for the input sadir:\n ------\n {db.get_users('sadir')}")

def test_get_round():
    db = Mongo()
    lst = ['sample','sample2','sample3']
    db.insert_round(lst)
    assert lst == db.get_recent_round()['queue']
    assert lst == db.get_round(2022, 8, 31)['queue']
    
    #by date