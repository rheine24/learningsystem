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

    #Add Location
    add_loc(room="1",
        floor="2",
        bldg="3",
        street_address="4",
        town_or_city="5",
        province="6",
        country="7")


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

def add_loc(room, floor, bldg, street_address, town_or_city, province, country):
    l = Location.objects.get_or_create(room=room, floor=floor, bldg=bldg, street_address=street_address, town_or_city=town_or_city,
        province=province, country=country)[0]
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