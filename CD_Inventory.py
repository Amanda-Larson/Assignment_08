#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# ALarson, 2021-Dec-04, added code for OOP functionality, completed all TODOs
# ALarson, 2021-Dec-05, cleaned up notes, docstrings, and historic remnants and
#                       tested for OOP functionality
#------------------------------------------#


import sys


# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    #---Fields---#
    cdID = None
    cdArtist = ''
    cdTitle = ''
    
    #---Constructor---#
    def __init__(self, idnum, title, artist):
        #---Attributes---#
        self.__cdID = idnum
        self.__cdTitle = title
        self.__cdArtist = artist
   
    #cdTitle
    @property
    def cdTitle(self):
        return self.__cdTitle
    
    @cdTitle.setter
    def cdTitle(self, title):
        if str(title).isnumeric():
            raise Exception('Title must be a string')
        else:
            return self.__title
    
    #cdArtist        
    @property
    def cdArtist(self):
        return self.__cdArtist
    
    @cdArtist.setter
    def cdArtist(self, artist):
        if str(artist).isnumeric():
            raise Exception('Artist must be a string')
        else:
            return self.__artist
        
        
        
        
# -- PROCESSING -- #


class DataProcessor:
    """The DataProcessor class processes the user data.
    
    properties: 
        
    methods:
        add_CD(idnum, title, artist) -> None
        delete_Row(intIDDel) -> None
        """
    @staticmethod
    def add_CD(idnum, title, artist):
        """Function to add a new user-defined CD to the table in-memory.
        
        Args: 
            intID: the CD ID number as provided by the user
            strTitle: the CD title as provided by the user
            stArtist: the CD artist as provided by the user
            
        Returns: 
            None.
        """
        
        cdLst = [idnum, title, artist]
        lstOfCDObjects.append(cdLst)
                
        
    @staticmethod    
    def delete_Row(intIDDel): 
        """ Function to delete row in table.
        
        Args:
            intIDDel: the ID of the CD to delete
        
        Returns: 
            None.
                    
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstOfCDObjects:
            intRowNr += 1
            if row[0] == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')


class FileProcessor:
    """Processing the data to and from text file
    
    properties:

    methods:
        write_file(file_name, table): -> None
        read_file(file_name, table): -> (a list of CD objects)

    """
    
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) one line in the file represents one object row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): lstOfCDObjects = 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        
        table.clear()  # this clears existing data and allows to load data from file
            
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                row = [int(data[0]), data[1], data[2]]
                table.append(row)
            objFile.close()
            return table 
        except IOError:
            print('Unable to open the file', file_name,'.'.strip(), 'Ending program.\n')
            input('\n Press Enter to exit.')
            sys.exit()
        except:
            print('Unknown Error')
        finally:
            objFile.close()

    
    @staticmethod
    def write_file(file_name, table):
        """Function to manage the saving of data to a text file.
        
        Saves/writes the data into a file identified by file_name from a 2D list of objects.
        
        
        Args: 
            file_name (string): name of file to be saved, presumably the same as has already been loaded in.
            table (list of objects): lstOfCDObjects = 2D data structure (list of objects) that holds the data during runtime
            
        Returns: 
            None.
            """
        try:
            objFile = open(strFileName, 'w')
            for eachobj in lstOfCDObjects:
                eachobj[0] = str(eachobj[0])
                objFile.write(','.join(eachobj) + '\n')
            objFile.close()
        except IOError:
            print('Unable to open/write to file.')
        finally:
            objFile.close()
            
            
            
# -- PRESENTATION (Input/Output) -- #

class IO:

    """Handling Input / Output
    
    properties: 
        
    
    methods: 
        print_menu() -> None
        menu_choice() -> None
        show_inventory -> None
        get_CD() -> a tuple of the user's input: strID, strTitle, stArtist
        
    """
    

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        try:
            choice = ' '
            while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
                choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            print()  # Add extra space for layout
            return choice
        except TypeError:
            print('Numbers aren\'t allowed, please choose a letter from the menu choices above.')


    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for eachCD in table:
            print(str(eachCD[0]) + '\t' + eachCD[1] + '\t' + 'by: ' + eachCD[2])
        print('======================================')


    @staticmethod
    def get_CD():
        """Function to get user input/information for the CD ID number, the CD title, and the CD artist.
        
        Args: None
            
        Returns:
            a tuple of the user's input: strID, strTitle, stArtist
        
        """
        
        while True:
            try:
                idnum = int(input('Enter ID: ').strip())
                strID = str(idnum)
                break                
            except ValueError:
                print('The ID must be a number. Please enter a numeric ID.')
            
           
            
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return strID, title, artist #returns a tuple
    
    
    
# -- Main Body of Script -- #

# 1.0 Load data from file into a list of CD objects on script start
print() #for spacing
print('Welcome to the CD Inventory Program \n')
lstOfCDObjects = FileProcessor.read_file(strFileName, lstOfCDObjects)
IO.show_inventory(lstOfCDObjects)

while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileProcessor.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, title, artist = IO.get_CD() #unpack and call at the same time
        # 3.3.2 Add item to the table
        idnum = int(strID)
        CD(idnum, title, artist)
        DataProcessor.add_CD(idnum, title, artist)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        #test for objects - for testing only
        #for cds in lstOfCDObjects:  
        #    objcd = CD(cds[0], cds[1], cds[2])
        #    print(objcd)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        while True:
            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
                break
            except ValueError:
                print('Please type an ID (number) to delete')
        # 3.5.2 search thru table and delete CD
        blnCDRemoved = False
        DataProcessor.delete_Row(intIDDel)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            FileProcessor.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')