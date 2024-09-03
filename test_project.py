
# import statements
from project import pick_major
from project import enter_grades
from project import activities
from project import awards
from project import supp_essays
from project import rec_letters
from project import decision_time

# tests the student's major
def test_pick_major():
    assert pick_major("engineering") == 25
    assert pick_major(" business") == 45
    assert pick_major("MEDICINCE") == 60
    assert pick_major("ART ") == 75
    assert pick_major("computer science") == "Not valid"

# tests the student's semester grades
def test_enter_grades():
    assert enter_grades("100, 97, 93, 94, 99, 92, 95") == 98
    assert enter_grades("81, 69, 84, 78, 88, 74, 53") == 45
    assert enter_grades("101, 94, 86, 94, 116, 75, 81") == "Not valid"
    assert enter_grades("96, 75, 87, 90, 76") == "Not valid"

# tests the student's activities/extracurriculars
def test_activities():
    assert activities("10", "15", "40") == 75
    assert activities("5", "6", "20") == 30
    assert activities("15", "20", "16") == "Not valid"
    assert activities("4", "200", "52") == "Not valid"
    assert activities("7", "25", "100") == "Not valid"
# tests the student's awards
def test_awards():
    assert awards("10") == 100
    assert awards("20") == "Not valid"

# tests the student's supplemental essays
def test_supp_essays():
    assert supp_essays("90%") == 90
    assert supp_essays("80") == "Not valid"
    assert supp_essays("hello%") == "Not valid"

# tests the student's letters of recommendation
def test_rec_letters():
    assert rec_letters("2", "90%") == 75
    assert rec_letters("4", "100%") == "Not valid"
    assert rec_letters("3", "75") == "Not valid"


# tests the student's decision cycle
def test_decision_time():
    assert decision_time("regular decision") == 75
    assert decision_time("Early decision") == 85
    assert decision_time("ED") == 85
    assert decision_time("early action") == "Not valid"

