import app
import pytest
import requests
import json
from threading import Thread
from common import Base


@pytest.fixture(scope="module", autouse=True)
def setup():
    # Start running mock server in a separate thread.
    # Daemon threads automatically shut down when the main process exits.
    mock_server_thread = Thread(target=app.init_api)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()


def test_JPY_To_USD_1000000():
    testdata = json.dumps(
        {"source": "JPY", "target": "USD", "amount": 1000000})
    rtn = requests.post(url='http://localhost:5000/transfer',
                        data=testdata, headers=Base.getheader())
    print(f'====>status code: {rtn.status_code},{json.loads(rtn.content)}')
    assert rtn.status_code == 200
    expect_content = {"Result": "8,850.00", "Reason": ""}
    assert json.loads(rtn.content) == expect_content
