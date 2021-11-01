from studentvue import StudentVue

import datetime
import time

# the functions are written in the order that they are displayed on the webpage (assignments, grades, schedule)


def get_current_day():
    today = datetime.datetime.now()
    return today


# this gets the assignments for the next week

def get_days_next_week():

    next_week_num = (datetime.date.today() +
                     datetime.timedelta(weeks=1)).strftime("%V")
    WEEK = int(next_week_num) - 1
    today = datetime.date.today()
    current_year = today.year
    startdate = time.asctime(time.strptime(
        f'{current_year} {WEEK} 0', '%Y %W %w'))
    startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')
    dates = [today.strftime('%m/%d/%Y')]
    for i in range(0, 6):
        day = startdate + datetime.timedelta(days=i)
        dates.append(day.strftime('%m/%d/%Y'))
    return dates


def get_upcoming_assignments(user: StudentVue):

    dates_next_week = get_days_next_week()

    assignments = user.get_calendar(
    )["CalendarListing"]["EventLists"]["EventList"]
    dates_dict = {}
    dates_list = []
    for next_date in dates_next_week:
        dates_dict[next_date] = []
        for a in assignments:
            if a["@Date"] == next_date:
                dates_dict[next_date].append(a["@Title"])
    return dates_dict


# starting getting the courses

def get_courses(user: StudentVue):
    return user.get_gradebook()['Gradebook']['Courses']['Course']

# helper functions for the grade predictions


def get_assignments(user: StudentVue):
    courses = get_courses(user)
    # user.get_gradebook()['Gradebook']['Courses']['Course'][-1]["Marks"]["Mark"]["Assignments"]["Assignment"]
    # the -1 is the course number so -1 is the last lesson

    assignments = {}
    # getting all the assignments and attaching them to their class
    for index in range(0, len(courses)):
        key = courses[index]["@Title"]
        assignments[key] = user.get_gradebook(
        )['Gradebook']['Courses']['Course'][index]["Marks"]["Mark"]["Assignments"]["Assignment"]
    return assignments


def get_weighted_assignments(user: StudentVue):
    assignments = get_assignments(user)
    graded_assignments = {}
    for lesson_name in assignments.keys():
        lesson_grades_assignments = []
        for a in assignments[lesson_name]:
            if "summative" in a["@Type"].lower():
                lesson_grades_assignments.append(a)
        graded_assignments[lesson_name] = lesson_grades_assignments

    return graded_assignments


def grade_prediction(user: StudentVue):
    assignments = get_weighted_assignments(user)
    full_scores = {}

    for key in assignments.keys():
        earned_score = 0
        max_score = 0
        min_score = 0
        for a in assignments[key]:
            a = a["@Points"]
            # this is if it is not graded
            if '/' not in a:
                earned_points = total_points = float(a.split()[0])
                min_points = 0
            else:
                earned_points, total_points = a.split('/')
                earned_points = min_points = float(earned_points)
                total_points = float(total_points)

            earned_score += earned_points
            max_score += total_points
            min_score += min_points
            max_percent = round(earned_score / max_score * 100)
            min_percent = round(min_score / max_score * 100)
            percent_dict = {"max": max_percent, "min": min_percent}
            full_scores[key] = percent_dict

    return full_scores

# starting the schedule


def get_today_schedule(user: StudentVue):
    return user.get_schedule()["StudentClassSchedule"]["TodayScheduleInfoData"]["SchoolInfos"]


def is_holiday(user: StudentVue):
    today_schedule = get_today_schedule(user)
    return today_schedule == {}

# this function checks if it is a holiday and if it is then it return the user's whole schedule


def get_valid_schedule(user: StudentVue):
    today_holiday = is_holiday(user)
    if not today_holiday:
        schedule = get_today_schedule()
    else:
        schedule = user.get_schedule(
        )["StudentClassSchedule"]["ClassLists"]["ClassListing"]
    return schedule

# finish when school starts again because I can't get it right now
def get_current_lesson(user: StudentVue):
    if not is_holiday(user):
        schedule = get_valid_schedule(user)
    else:
        return None
