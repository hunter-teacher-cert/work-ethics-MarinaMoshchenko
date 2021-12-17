import random


def create_plane(rows,cols): #creates a board (seating chart) for the plane 
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = [] #list of lists, list of rows
    for r in range(rows): #ex. [win, avail, avail, avail, win]
        s = ["win"]+["avail"]*(cols-2)+["win"] #creates a list for each row with win seats at sides and avail all seats in between
        plane.append(s) #adds row, creates list of seats 
    return plane

def get_number_economy_sold(economy_sold): #number of economy tickets sold passed as a parameter
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0 
    for v in economy_sold.values(): #traverse through all values (from dictionary key-value pairs) of economy sold tickets 
        sold = sold + v #and adds them up
    return sold #returns the number of economy tickets sold


def get_avail_seats(plane,economy_sold): #plane - list of lists; economy_sold - dictionary Last Name - number of tickets sold
    """
    Parameters: plane : a list of lists representing plane
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane: #for number of rows in the plane list of lists
        for c in r: #for number of columns in each row of the plane 
            if c == "avail" or c == "win":
                avail = avail + 1 #adds up all seats in a plane
    avail = avail - get_number_economy_sold(economy_sold) #subtracts number of sold tickets
    return avail #returns namber of seats (tickets) available for sale 

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0]) #number of rows times number of columns in plane seating chart

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature (displays all items (x) in a row as a string of length x?)
        s = s + " ".join(r) #joins a string of seats
        s = s + "\n" #adds a line break
    return s



def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane) #number of rows in list of lists
    cols = len(plane[0]) #number of columns in row 0

    
    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold) #number of seats available for sale

    # exit if we have no more seats
    if seats < 1:
        return plane #print the seating chart as it currently is


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30: #70% chance 
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order: #traverse through each row
            if plane[row][0] == "win": #if left window seat in a plane is available
                plane[row][0] = name #assign left seat to a passenger's name
                return plane #seating chart with new assignment
            elif plane[row][len(plane[0])-1] == "win": #if right window seat in a plane is available
                plane[row][len(plane[0])-1] = name #assign right seat to a passenger's name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False #available seat is not found
    while not(found_seat): #random search probably becouse the plane needs to be filled with passangers through out all the space for better operation (not in the front only, or back only, gravity)
        r_row = random.randrange(0,rows) #random row
        r_col = random.randrange(0,cols) #random column
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail": #if a seat available,
            plane[r_row][r_col] = name #assign it to a passenger
            found_seat = True #available seat is found
    return plane #return seating chart with new assignment


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but 
    just does the random assignment. 

    We use this when we're ready to assign the economy seats after most 
    of the economy plus seats are sold

 
    """
    rows = len(plane) #number of row in a seating chart
    cols = len(plane[0]) #number of columns in row 0 os seating chart

    found_seat = False #available seat is not found
    while not(found_seat): 
        r_row = random.randrange(0,rows) #random row
        r_col = random.randrange(0,cols) #random column
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail": #if a seat available,
            plane[r_row][r_col] = name #assign it to a passenger
            found_seat = True #available seat is found
    return plane #return seating chart with new assignment


def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane) #total number of seats in a plane
    seats_avail = seats_avail - get_number_economy_sold(economy_sold) #subtract number of sold seats/tickets

    if seats_avail >= number: #if number of available seats is greater of equal to the numeer of seats requated by a passenger
        economy_sold[name]=number #add pair 'Passenger;s last name-number of tickets' to a dictionary economy_sold
    return economy_sold #return dictionary 


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """

    
    economy_sold={} #creates an object key-value pairs: 'Pasenger's last name : number of tickets sold'
    total_seats = get_total_seats(plane) #calculates the total number of seats (avail and sold)
    


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3 #no more than 3 family members can be placed together
    while total_seats > 0: #while there are more then 0 seat available
        r = random.randrange(100) #generate random number 1-100
        if r > 30: #70% chance that the customer tries to purchase a window seat
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number) #assigns a name ep-number to sold economy plus seats
            ep_number = ep_number + 1 #increments the number of ep tickets sold
            total_seats = get_avail_seats(plane,economy_sold) #recalculates the number of available seats
        else: #generates random number between 2 and 3 (2 or 3) and assigns u-number to it
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1 #increments the number of unassigned seats

        
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for name in economy_sold.keys(): #for passengers last names in dictionary economy_sold; key in key-value pairs
        #if economy_sold[name] > 0: #line does not refer to the pairs in the dictionary (Last name with 0 tickets sold)
        #for i in range(economy_sold[name]): #for numbers in dictionary economy_sold; value in key-value pairs
            plane = seat_economy(plane,economy_sold,name) #generates a seating chart with newly assigned seats


    return plane
    
    
    
def main():
    plane = create_plane(10,5) #generates the list of 10 rows and 5 columns
    plane = fill_plane(plane) #
    print(get_plane_string(plane)) #printable version of seating chart
if __name__=="__main__": #special variable; whether we want to run the script
    main()