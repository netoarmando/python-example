import hello
import os


def test_says_world():
    assert hello.say_what() == 'world'


def test_var_env():
    travis_env = os.environ.get('TRAVIS')
    print('TRAVIS VAR:', travis_env)
    assert travis_env == 'true'
