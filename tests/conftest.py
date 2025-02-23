import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker ()

def pytest_addoption(parser):
    parser.addoption(
        "--num_records",
        action="store",
        default=0,
        type=int,
        help="Number of records to generate"
    )

def pytest_configure(config):
    num_records = config.getoption("--num_records")
    if num_records:
        print(f"Generating {num_records} records...")
        # Example: generate a list of dictionaries as dummy records
        records = [{"id": i, "value": f"record {i}"} for i in range(num_records)]
        # Store generated records on the config for later use in tests
        config._generated_records = records

@pytest.fixture
def records(request):
    # Access the generated records (empty list if none generated)
    return getattr(request.config, "_generated_records", [])
 