from times import compute_overlap_time, time_range
from pytest import raises
import pytest

# It is a convention to name test function starting with 'test_'

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_overlap():
    '''
    Doing a basic functionality check for overlap function
    Does it find the overlap of 2 normally configured timestamps
    '''
    large = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_several_int():
    '''
    Testing overlap function when several intervals are created
    '''
    t1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    t2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(t1,t2) == t2


def test_adjacent():
    '''
    Testing two time ranges that end exactly at the same time when the other starts.
    '''
    t1 = time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00")
    t2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    expected = []
    assert compute_overlap_time(t1,t2)==expected

# Ensure that your main code stops this. Modify time_range to produce an error (ValueError) with a meaningful message when a "backwards" time_range is passed to it - this is called input validation.
# Write a test that tries to generate a time range for a date going backwards.
# Use pytest.raises to check for that error in the test.
# Commit, push and link to this issue (including Answers UCL-COMP0233-24-25/RSE-Classwork#13).
# What other similar tests could we add?

def test_time_range_inputs():
    '''
    a negative test for the time_range function 
    to make sure that it throws an error when the start time is after the end time.
    '''
    t_start = "2010-01-12 10:45:00"
    t_end = "2010-01-12 10:00:00"
    with raises(ValueError):
        time_range(t_start, t_end)

# You will need the test function to accept parameters, for example time_range_1,time_range_2 and expected, 
# let the parametrize decorator 
# know about it as its first argument and pass a list of tuples of length 3 with the values for each test.

# Parametrizing the test
@pytest.mark.parametrize("first_range, second_range, expected", 
                        # Test 1
                        [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
                        [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
                        ),
                        
                        # Test 2
                        (time_range("2010-01-12 10:45:00", "2010-01-12 12:00:00"), 
                        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00"), 
                        []
                        ),

                        # Test 3
                        (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60), 
                         time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), 
                        [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
                        )
                        ]
                        )
                        

def test_eval(first_range, second_range, expected):
    assert compute_overlap_time(first_range, second_range) == expected


        