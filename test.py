
import pytest
from myRESTfulTodoList import app


class TestClass(object):

    def setup_class(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def teardown_class(self):
        pass

    def test_query_all(self):
        response = self.app.get('/api/tasks/')
        print(str(response.data, encoding='utf-8'))
        assert 200 == response.status_code

    def test_insert(self):
        response = self.app.post('/api/tasks/')
        assert 403 == response.status_code

        data = '{"id":1, "content": "test_insert"}'
        response = self.app.post('/api/tasks/', data=data)
        assert 403 == response.status_code


    def test_query_by_id(self):
        response = self.app.get('/api/tasks/1')
        assert 200 == response.status_code

    def test_delete_by_id(self):
        response = self.app.delete('/api/tasks/2')
        assert 200 == response.status_code


if __name__ =="__main__":
    pytest.main(['test.py','-s'])
