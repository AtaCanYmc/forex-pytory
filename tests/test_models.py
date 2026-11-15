from forex_pytory.core.models import EconomicEvent


def test_economic_event_creation():
    event = EconomicEvent(
        id="12345",
        time="8:30am",
        currency="USD",
        event="CPI m/m",
        forecast="0.3%",
        actual="0.2%",
        previous="0.4%",
        impact="high",
    )
    assert event.id == "12345"
    assert event.time == "8:30am"
    assert event.currency == "USD"
    assert event.event == "CPI m/m"
    assert event.impact == "high"


def test_economic_event_alias_population():
    data = {
        "ID": "67890",
        "Time": "10:00am",
        "Currency": "EUR",
        "Event": "ECB Press Conference",
        "Forecast": None,
        "Actual": None,
        "Previous": None,
        "Impact": "medium",
    }
    event = EconomicEvent.model_validate(data)
    assert event.id == "67890"
    assert event.currency == "EUR"
    assert event.impact == "medium"
    dumped = event.model_dump(by_alias=True)
    assert dumped["ID"] == "67890"
    assert dumped["Currency"] == "EUR"
