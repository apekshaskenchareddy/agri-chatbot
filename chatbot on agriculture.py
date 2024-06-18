class Crop:
     def __init__(self, name, description, temperature, soil, rainfall, growth_period):
        self.name = name
        self.description = description
        self.temperature = temperature
        self.soil = soil
        self.rainfall = rainfall
        self.growth_period = growth_period


def get_crop_info(crop_name):
    for crop in crops:
        if crop.name.lower() == crop_name.lower():
            return crop
    return None

print("Welcome to the Crop Information Chatbot!")

class Scheme:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

crops = [
    Crop("Wheat", "Wheat is a cereal crop...", "15°C - 25°C", "Well-drained loam soil...", "400 - 600 mm", "100 - 130 days"),
    Crop("Rice", "Rice is a staple food...", "20°C - 35°C", "Flooded or paddy fields...", "1000 - 3000 mm", "105 - 210 days"),
    Crop("Maize (Corn)","A versatile cereal used for food and feed...","20-30°C","Well-drained soil...","500-1000 mm","60-100 days"),
    Crop("Cotton"," Fiber used in textile production...","20-30°C","Well-drained loamy soil...","600-1000 mm","160-180 days"),
    Crop("Potato","Underground tuber used for food...","15-20°C","Sandy-loam soil...","500-1000 mm","70-120 days"),
    Crop("Soybean","Legume used for oil and protein...","20-30°C","Well-drained loamy soil...","600-1000 mm","80-150 days"),
    Crop("Sugarcane","Source of sugar and ethanol production...","20-35°C","Well-drained fertile soil...","1000-2000 mm","10-24 months"),
    Crop("Coffee","Source of coffee beans...","18-25°C","Well-drained, acidic soil...","1500-2500 mm","3-4 years to mature"),
    Crop("Tomato","Edible fruit used in various dishes...","15-30°C","Well-drained, loamy soil...","500-1000 mm","60-85 days"),
    Crop("Grapes","Berries used for making wine and raisins....","15-25°C","Well-drained, sandy-loam soil...","600-1000 mm","3-5 years to mature"),
]

schemes = ["PLEDGE LOAN SCHEME","RAITHA SANJEEVINI"]
contacts = ["08182-250236","08183-226173,08182-226174"]

def agriculture_chatbot():
    while True:
        print("\nSelect an option:")
        print("1. Crop Information Chatbot")
        print("2. Agriculture Information Chatbot")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            crop_name = input("Enter the name of a crop (or 'quit' to exit): ")
            if crop_name.lower() == "quit":
                print("Goodbye!")
                break
            crop_info = get_crop_info(crop_name)
            if crop_info:
                print("\nCrop:", crop_info.name)
                print("Description:", crop_info.description)
                print("Temperature:", crop_info.temperature)
                print("Soil:", crop_info.soil)
                print("Rainfall:", crop_info.rainfall)
                print("Growth Period:", crop_info.growth_period)
            else:
                print("Crop information not available.")
        
        elif choice == "2":
            while True:
                print("\nSelect an option:")
                print("1. Add Scheme")
                print("2. Add Contact")
                print("3. Display Schemes")
                print("4. Display Contacts")
                print("5. Back to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    name = input("Enter scheme name:PLEDGE LOAN SCHEME,RAITHA SANJEEVINI")
                    description = input("Enter scheme description:farmers can store their agricultural produce in the godowns of regulated markets for a maximum period of six months and can avail pledge loan up to a maximum of Rs. 2.00 lakhs,This is an Accident Insurance Scheme implemented by the Board from 1996. Under this scheme, a farmer who meets with an accidental death or permanent disabilities by production or marketing operations the following amount of compensation grant by the Board")
                    scheme = Scheme(name, description)
                    schemes.append(scheme)
                    print("Scheme added successfully!")

                elif sub_choice == "2":
                    name = input("Enter contact name:Deputy Director,Secretary,Manager ")
                    phone = input("Enter contact phone:08182-250236,08183-226173,08182-226174 ")
                    email = input("Enter contact email:ddamsmg@gmail.com,apmcsagar@gmail.com,shimogaapmc@gmail.com  ")
                    contact = Contact(name, phone, email)
                    contacts.append(contact)
                    print("Contact added successfully!")

                elif sub_choice == "3":
                    print("\nSchemes: 1.PLEDGE LOAN SCHEME, 2.RAITHA SANJEEVINI")
                    schemes = [
                        "farmers can store their agricultural produce in the godowns of regulated markets for a maximum period of six months and can avail pledge loan up to a maximum of Rs. 2.00 lakhs",
                        "This is an Accident Insurance Scheme implemented by the Board from 1996. Under this scheme, a farmer who meets with an accidental death or permanent disabilities by production or marketing operations the following amount of compensation grant by the Board."
                        ]
                    for idx, scheme in enumerate(schemes, start=1):
                        print(f"{idx}. {scheme}")
                elif sub_choice == "4":
                    print("\nContacts: 08182-250236, 08183-226173,08183-226174")
                    contacts = [
                        ("Deputy Director", "08182-250236", "ddamsmg@gmail.com"),
                        ("Secretary", "08183-226173", "apmcsagar@gmail.com"),
                        ("Manager", "08183-226174", "shimogaapmc@gmail.com")
                         ]
                    for idx, (name, phone, email) in enumerate(contacts, start=1):
                        print(f"{idx}. Name: {name}")
                        print(f"   Phone: {phone}")
                        print(f"   Email: {email}")

                elif sub_choice == "5":
                    print("Returning to main menu.")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

print("Welcome to the Main Menu!")
agriculture_chatbot()
