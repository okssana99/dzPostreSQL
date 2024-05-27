from typing import List, Dict
import csv

class Phone:
    def __init__(self):
        self._incoming_calls: int = 0

    def set_number(self, number: str):
        self.number: str = number

    def get_number(self) -> str:
        return self.number

    def set_incoming_calls_count(self, count: int):
        self._incoming_calls = count

    def get_incoming_calls_count(self) -> int:
        return self._incoming_calls

    def receive_call(self):
        self._incoming_calls += 1

phone1: Phone = Phone()
phone1.set_number("123456789")
phone2: Phone = Phone()
phone2.set_number("555555555")
phone3: Phone = Phone()
phone3.set_number("112233445")

phone1.receive_call()
phone1.receive_call()
phone2.receive_call()
phone3.receive_call()
phone3.receive_call()
phone3.receive_call()


def save_calls_to_csv(phones: List['Phone'], filename: str):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames: List[str] = ['Phone Number', 'Incoming Calls']
        writer: csv.DictWriter[Dict[str, str]] = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for phone in phones:
            writer.writerow({'Phone Number': phone.get_number(), 'Incoming Calls': str(phone.get_incoming_calls_count())})

def total_incoming_calls(phones: List['Phone']) -> int:
    total_calls: int = 0
    for phone in phones:
        total_calls += phone.get_incoming_calls_count()
    return total_calls

phones: List['Phone'] = [phone1, phone2, phone3]
print("Total incoming calls:", total_incoming_calls(phones))

save_calls_to_csv(phones, 'incoming_calls.csv')
