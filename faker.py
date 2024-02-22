import time
from datetime import datetime

from faker import Faker
import json

fake = Faker()

def generate_fake_data():
    data = {"id": fake.uuid4(),"name": fake.name(),"address": {"street": fake.street_address(),"city": fake.city(),"state": fake.state_abbr(),"postalCode": fake.zipcode()},"email": fake.email(),"phone": fake.phone_number(),"coordinates": {"latitude": float(fake.latitude()),"longitude": float(fake.longitude())}}
    return data

if __name__ == "__main__":

    curr_time = datetime.now()

    while (datetime.now() - curr_time).seconds < 500:
        generated_data = generate_fake_data();
        json_data = json.dumps(generated_data)

        time.sleep(1)

        with open("fake_data.json", "a") as json_file:
            json_file.write(json_data + ',\n')


    print("Fake data has been generated and saved to fake_data.json.")