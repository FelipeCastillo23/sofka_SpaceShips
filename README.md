# sofka_SpaceShips
This is a project created to compete in the [Sofka](https://www.sofka.com.co) Training League technical challenge,
that can be found in the "reto-tecnico-training-desarrollo.pdf" file in the repo.

## Authors

- Felipe Castillo / [LinkedIn](https://www.linkedin.com/in/felipe-castillo-patino/) -[GitHub](https://github.com/FelipeCastillo23)
I'm a software junior developer taking my first steps in professional programming

## Running Tests

Download the 3 .py files in the repo, and execute SofkaSpaceStation.py
It will create a folder named "db" in the current directory, and execute de GUI for you to interact with the database.
If it is the first time it's running, it will also populate the database with examples
of the diferent types of ships that were included.

You can fill any of the fields acordingly to either:
    - Add: You can add a new entry in the database, when you select a type of ship new fields will
    appear acordingly, also the "Name" field is obligatory and cannot be repeated within the DB
    - Filter: You can filter and display the database filling the avilable fields, it will only return full
    coincidences, so keep that in mind. Any field that has the default value in it wont be considered
    in the filtering, if you forget to fill any field it will display the whole DB.
    - Clear: clear all the fields to their default value.


## Documentation

Here i'm going to define the abstraction and construction of the classes that were originaly 
intended for this project, and the reason of why it's only one used.

After reading the base [blog](https://moaramore.com/2016/05/14/clasificacion-de-las-naves-espaciales) 
it's clear that there are 3 diferent types of space ships: Shuttles, Not Tripulated and Trippulated
so i started getting the attributes from the specific data that is in the text, leading defining the
following objects:

Basic Space Ship (what they all have in common)
- Name - Name of the ship and primary identificator
- Type - Type of space ship (Basic, Shuttle, Not Tripulated, Tripulated)
- Country - Where it was fabricated
- Year - Year of inaguration, or first active
- Active - Currently in use or not
- Weight - Weight in tons
- Trust - Trust in tons
- Fuel - Kind of fuel that is used i.e. Liquid Hydrogen
- Function - Specific purpose of the ship

Shuttles (inherits all atributes from Basic)
- Load Weight - Weight of the load that the ship can carry in tons
- Height - Height of the ship in m
- Power - Power of the ship in kHp (i don't like that unit but it was the common one)

Not Tripulated (inherits all atributes from Basic)
- Speed - in km/s

Tripulated (inherits all atributes from Basic)
- Capacity - Number of crew on board
- Orbit height - Average distance from the earth in km from the surface

So the development started, i decided to use SQLite as database manager for it's lightweight
desing, and TKinter for the GUI as it felt just better as a challenge to learn and desing not 
just the code but also a friendly and usefull GUI. To really make progress (i had just the night
time for this, because of work) i decided to begin with just one type of ship, and then expand
the code for the other 3 types but there was no quick work arround the using and displaying of
three diferent tables, so for the sake of the project i decided to go with just one class and
one database table including all different 4 types of ships. 