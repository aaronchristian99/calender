from Calender import Event

class GUI:
    _DATE_PRESCISION = ['year', 'month', 'day', 'hour']
    _DATE_DELIMETER = '/'
    # takes a list of events and displays them
    def printEvents(events: list[Event]):
        for event in events:
            print(event)

    # gets input in 'title', 'description', 'location', 'start_date', 'end_date' all in string
    # dates are stored in decending order with delimeter '_DATE_DELIMETER'
    def getEventInput(self) -> tuple[str, str, str, str, str]:

        title = input("Enter title for event: ")

        description = input("Enter description for event: ")

        location = input("Enter location for event")

        start_date = []
        for parameter in self._DATE_PRESCISION:
            u_in = input(f"Enter the {parameter} for the start date: ")
            start_date.append(u_in)

        end_date = []
        for index, parameter in enumerate(self._DATE_PRESCISION):
            u_in = input(f"Enter the {parameter} for the end date (leave blank for the same as start date): ")
            if u_in == None:
                end_date.append(start_date[index])
            else:
                end_date.append(u_in)
                
        for parameter in start_date:
            date_string += parameter
            

        return title, description, location, start_date, end_date

