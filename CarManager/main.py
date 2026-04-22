from SQL import schema
from SQL import init_db

init_db.get_connection()


# START OF THE PROJECT CREATING THE TABLES
def startup():
    print("Checking status...")

    # Handles the tables creation.
    schema.create_tables()
    print("Database ready, have fun!")


# FUNCTION RESPONSIBLE TO HANDLE THE ADDITIONS TO THE DATABASE.
def add_owner(ownerName, ownerAge, carMaker, carModel, carColor, carPrice):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "INSERT INTO CarManager(owner_name, owner_age, car_maker, car_model, car_color, car_price) VALUES (?, ?, ?, ?, ?, ?)"
    values = (ownerName, ownerAge, carMaker, carModel, carColor, carPrice)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("\nOwner added successfully")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"\nDatabase error {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE NAMES VALUES TO THE DATABASE BASED ON THE ID.
def update_owner_name(ownerId, owner_new_name):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET owner_name = ? WHERE owner_id = ?"
    values = (owner_new_name, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Owner name successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE AGE VALUES TO THE DATABASE BASED ON THE ID.
def update_owner_age(ownerId, owner_new_age):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET owner_age = ? WHERE owner_id = ?"
    values = (owner_new_age, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Owner age successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE CARMAKERS VALUES TO THE DATABASE BASED ON THE ID.
def update_car_maker(ownerId, new_car_maker):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET car_maker = ? WHERE owner_id = ?"
    values = (new_car_maker, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Car maker successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE CARMODEL VALUES TO THE DATABSE BASED ON THE ID.
def update_car_model(ownerId, new_car_model):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET car_model = ? WHERE owner_id = ?"
    values = (new_car_model, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Car model successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE CARCOLOR VALUES TO THE DATABASE ON THE ID.
def update_car_color(ownerId, new_car_color):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET car_color = ? WHERE owner_id = ?"
    values = (new_car_color, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Car color successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO UPDATE THE CARPRICE VALUES TO THE DATABASE ON THE ID.
def update_car_price(ownerId, new_car_price):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "UPDATE CarManager SET car_price = ? WHERE owner_id = ?"
    values = (new_car_price, ownerId)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Car price successfully updated. ")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO DELETE VALUES BASED ON THE ID.
def delete_owner(ownerId):
    conec = init_db.get_connection()
    cursor = conec.cursor()

    # Responsible for getting the inside database values and assigning with new ones, each ? represents a placeholder.
    sqlV = "DELETE FROM CarManager WHERE owner_id = ?"
    values = (ownerId,)

    # A safer approach to execute and store the values
    try:
        cursor.execute(sqlV, values)
        conec.commit()
        print("Owner successfully deleted")
    # It will show any errors, giving the specific problem to make it easier to fix.
    except Exception as e:
        print(f"\nDatabase error {e}")
    finally:
        conec.close()


# FUNCTION RESPONSIBLE TO RUN THE CODE, TO MAKE IT ALL WORK.
def run_menu():
    print("---CAR MANAGER---")

    # Main Loop, it'll run until you decide to stop.
    while True:
        print("\n[1] Add an owner")
        print("[2] Delete an owner (Per ID)")
        print("[3] Update.")
        print("[4] Exit")

        userChoice = input("\nChoose an option. ")

        # Prompt Handling based of 'User Choice' as a Char.
        if userChoice == '1':
            try:
                ownN = input("Enter the Owner Name: ")
                ownA = int(input("Enter the Owner Age: "))
                carM = input("Enter the Car Brand: ")
                carMo = input("Enter the Car Model: ")
                carC = input("Enteer the Car Color: ")
                carP = float(input("Enter the Car Price: ").replace(".", ""))

                add_owner(ownN, ownA, carM, carMo, carC, carP)

            # This will make sure you only write the correct input based on the type, otherwise that data won't be stored.
            except ValueError:
                print("Error: Age must be a number and Price must be a decimal. ")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif userChoice == '2':
            try:
                ownI = int(input("Enter the Owner ID: "))
                delete_owner(ownI)

            except ValueError:
                print("Error, the ID must be an integer.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        # User Update based on their ID.
        elif userChoice == '3':
            oId = input("Owner ID to Update: ")

            print("[1] Edit name. ")
            print("[2] Edit age. ")
            print("[3] Edit maker. ")
            print("[4] Edit model. ")
            print("[5] Edit color. ")
            print("[6] Edit price. ")

            scn_choice = input("What would you like to Update? ")

            # Same Prompt Handling, but since it has too many conditions, the match-case approach seemed the best.
            match scn_choice:
                case '1':
                    try:
                        ownerN = input("New name: ")
                        update_owner_name(oId, ownerN)
                    except ValueError:
                        print("Must be a string.")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                case '2':
                    try:
                        ownerA = int(input("New age: "))
                        update_owner_age(oId, ownerA)
                    except ValueError:
                        print("Age must be an integer. ")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                case '3':
                    try:
                        carMk = input("New maker: ")
                        update_car_maker(oId, carMk)
                    except ValueError:
                        print("Maker must be a string. ")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                case '4':
                    try:
                        carMod = input("New model: ")
                        update_car_model(oId, carMod)
                    except ValueError:
                        print("Model must be a string. ")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                case '5':
                    try:
                        carCo = input("New color: ")
                        update_car_color(oId, carCo)
                    except ValueError:
                        print("Color must be a string. ")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                case '6':
                    try:
                        carPr = float(input("New price: ").replace(".", ""))
                        update_car_price(oId, carPr)
                    except ValueError:
                        print("Price must be a decimal. ")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")
                # This will ensure if you type any number different from the cases, it will return a false input.
                case _: return "\nInvalid Input."

        # This will end the program.
        elif userChoice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid input.")


# Responsible to make the code run.
if __name__ == "__main__":
    startup()
    run_menu()
