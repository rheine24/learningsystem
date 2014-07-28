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

    thea_faci = add_faci(user=thea_user,
        birthdate="1994-01-29",
        contact_number="+639327944979")

    #Add Instructor
    add_inst(user=marc_user,
        birthdate="1994-01-25",
        contact_number="")

    marc_inst = add_inst(user=marc_user,
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

    #Add Frequency
    nvr_frq = add_frq(description="Never")

    add_frq(description="Never")
    add_frq(description="Weekly")
    add_frq(description="Monthly")

    #Add Event
    add_evt(name="Basic Programming using C",
        event_code="Prog C 101",
        instructor=marc_inst,
        start_date="2014-08-01",
        end_date="2014-08-01",
        start_time="09:00:00",
        end_time="15:00:00",
        frequency=nvr_frq)

    prgc_evt = add_evt(name="Basic Programming using C",
        event_code="Prog C 101",
        instructor=marc_inst,
        start_date="2014-08-01",
        end_date="2014-08-01",
        start_time="09:00:00",
        end_time="15:00:00",
        frequency=nvr_frq)

    #Add Location
    add_loc(room="304",
        floor="3rd",
        bldg="Vidal Tan Hall",
        street_address="Quirino Avenue corner Velasquez Street, University of the Philippines Diliman",
        town_or_city="Diliman, Quezon City",
        province="Metro Manila",
        country="Philippines")

    vdh_loc = add_loc(room="304",
        floor="3rd",
        bldg="Vidal Tan Hall",
        street_address="Quirino Avenue corner Velasquez Street, University of the Philippines Diliman",
        town_or_city="Diliman, Quezon City",
        province="Metro Manila",
        country="Philippines")

    #Add FaciLocEvent
    add_fle(facilitator=thea_faci,
        location=vdh_loc,
        event=prgc_evt,
        date="2014-08-07",
        time="09:01:00")

    #Add LS Info
    add_lsinfo(name="The Free Riders",
        shortname="TFR",
        address="Anywhere the wind blows, it doesn't really matter",
        logo="lslogo/avatar5.png")


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
    r = Registrar.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return r

def add_std(user, birthdate, contact_number):
    s = Student.objects.get_or_create(user=user, birthdate=birthdate, contact_number=contact_number)[0]
    return s

def add_evt(name, event_code, instructor, start_date, end_date, start_time, end_time, frequency):
    e = Event.objects.get_or_create(name=name, event_code=event_code, instructor=instructor, start_date=start_date,
        end_date=end_date, start_time=start_time, end_time=end_time, frequency=frequency)[0]
    return e

def add_frq(description):
    fr = Frequency.objects.get_or_create(description=description)[0]
    return fr

def add_loc(room, floor, bldg, street_address, town_or_city, province, country):
    l = Location.objects.get_or_create(room=room, floor=floor, bldg=bldg, street_address=street_address, town_or_city=town_or_city,
        province=province, country=country)[0]
    return l

def add_fle(facilitator, location, event, date, time):
    fle = FaciLocEvent.objects.get_or_create(facilitator=facilitator, location=location, event=event, date=date, time=time)[0]
    return fle

def add_lsinfo(name, shortname, address, logo):
    ls = LSInfo.objects.get_or_create(name=name, shortname=shortname, address=address, logo=logo)[0]
    return ls

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learningsystem.settings')
    from django.contrib.auth.models import User
    from facilitator.models import *
    from instructor.models import *
    from registrar.models import *
    from student.models import *
    populate()