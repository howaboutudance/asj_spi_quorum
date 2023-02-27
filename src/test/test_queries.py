import pytest

@pytest.fixture
def meeting_list_fixture():

    sister_short_names = ["Metro", "Berna", "Paddleme"]
    meetings_dates = [datetime.datetime(2022, 11, 6), datetime.datetime(2022, 12, 4), 
                    datetime.datetime(2023, 1, 4), datetime.datetime(2023, 2, 6)]

    meetings_list = []
    add_meeting_entry = lambda sister_i, meeting_i : meetings_list.append({
        "sister_short_name":sister_short_names[sister_i],
        "meeting_date": meetings_dates[meeting_i])

    # all sisters went to dec and jan meeting
    [add_meeting_entry(x, y] for x in range(len(sister_short_names) for y in [1,2])]


    # only metro and berna went to november
    [add_meeting_entry(x, 0) for x in [0,1])


    # only metro and pads went to feb meeting
    [add_meeting_entry(x,3) for x in [0,2]]

def test_meeting_list_fixture(meeting_list_fixture):
    assert len(meeting_list_fixture) == 10

def test_active_status(meeting_list_fixture):
    pass