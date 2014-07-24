import os

def populate():
    #Add Users
    thea_user = add_user(username="thea",
        email="thea@thea.com",
        first_name="thea",
        last_name="cacatian")

    marc_user = add_user(username="marc",
        email="marc@marc.com",
        first_name="marc",
        last_name="francisco")

    marc_inst = add_inst(user=marc_user,
        birthdate="1994-01-25",
        contact_number="")

    arah_user = add_user(username="arah",
        email="arah@arah.com",
        first_name="arah",
        last_name="jamandra")

    kate_user = add_user(username="kate",
        email="kate@kate.com",
        first_name="kate",
        last_name="manabat")

    #Add Facilitator
    add_faci(user=thea_user,
        birthdate="1994-01-29",
        contact_number="+639327944979")

    #Add Instructor
    add_inst(user=marc_user,
        birthdate="1994-01-25",
        contact_number="")

    #Add Registrar
    add_reg(user=arah_user,
        birthdate="1995-07-25",
        contact_number="")

    #Add Student
    add_std(user=kate_user,
        birthdate="1993-09-20",
        contact_number="")

    #Add Event
    add_evt(name="Basic Programming using C",
        event_code="Prog C 101",
        instructor=marc_inst,
        start_date="2014-08-01",
        end_date="2014-08-01",
        start_time="09:00:00",
        end_time="15:00:00")

    #Add Location
    add_loc(room="1",
        floor="2",
        bldg="3",
        street_address="4",
        town_or_city="5",
        province="6",
        country="7")

    #Add LS Info
    add_lsinfo(name="The Free Riders",
        shortname="TFR",
        address="Anywhere the wind blows, it doesn't really matter")


def add_user(username, email, first_name, last_name):
    u = User.objects.get_or_create(username=username, email=email, first_name=first_name, last_name=last_name)[0]
    return u

def add_faci(user, birthdate, contact_number):
    f = Facilitator.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return f

def add_inst(user, birthdate, contact_number):
    i = Instructor.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return i

def add_reg(user, birthdate, contact_number):
    f = Registrar.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return f

def add_std(user, birthdate, contact_number):
    i = Student.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return i

def add_evt(name, event_code, instructor, start_date, end_date, start_time, end_time):
    i = Event.objects.get_or_create(name=name, event_code=event_code, instructor=instructor, start_date=start_date,
        end_date=end_date, start_time=start_time, end_time=end_time)[0]
    return i

def add_loc(room, floor, bldg, street_address, town_or_city, province, country):
    l = Location.objects.get_or_create(room=room, floor=floor, bldg=bldg, street_address=street_address, town_or_city=town_or_city,
        province=province, country=country)[0]
    return l

def add_lsinfo(name, shortname, address):
    l = LSInfo.objects.get_or_create(name=name, shortname=shortname, address=address)[0]
    return l

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learningsystem.settings')
    from django.contrib.auth.models import User
    from facilitator.models import *
    from instructor.models import *
    from registrar.models import *
    from student.models import *
    populate()