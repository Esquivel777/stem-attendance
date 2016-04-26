__author__ = 'student'
# Comments look like this
import time
import pickle

present = [] # creates a list called present that can append information in it

with open('students.p', 'rb') as p_file: # using pickle a roster is create to save the data
        roster = pickle.load(p_file)
        
while True: # starts a loop
    try:
        s_id = input('Scan student id or enter Q to quit: ')
        if s_id in ['q', 'Q']: # gives option to end loop
            mark_absent = input('Mark missing students absent? (y/[n]) ')
            if mark_absent in ['y', 'Y']: # seconds option is added if absent
                for key, data in roster.items():
                    if data['name'] not in present: # makes a new entry if a person is absent
                        roster[key]['absent'].append(time.strftime("%m/%d")) # enters date when absent 
                with open('students.p', 'wb') as p_file:
                    pickle.dump(roster, p_file) # anything added to the p_file will be added to the new entry to keep track
            break

        else:
            present.append(roster[s_id]['name']) # gives option to enter id
            roster[s_id]['present'].append(time.strftime("%m/%d at %I/%M")) # added a time stamp 
            print('%s checked in on %s' % (roster[s_id]['name'], time.strftime("%m/%d at %I:%M"))) # prints when id is entered
    except KeyError:
        print("Invalid ID number") # if nothing matches what is entered there will be an error message
