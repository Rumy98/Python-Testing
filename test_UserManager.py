import pytest
from UserManager import UserManager
#
@pytest.fixture

def user_manager():
   return UserManager()

#user_manager=UserManager()

def test_user_manager(user_manager):
    assert user_manager.add_user("john doe","johndoe@gmail.com")==True
    assert user_manager.get_user("john doe")=="johndoe@gmail.com"
    
def test_add_duplicate_user(user_manager):
    user_manager.add_user("john doe","johndoe@gmail".com)
    with pytest.raises(ValueError):
        user_manager.add_user("john doe","doe@gmail.com")

    