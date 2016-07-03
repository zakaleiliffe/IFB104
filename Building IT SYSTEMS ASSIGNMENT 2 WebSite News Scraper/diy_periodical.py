

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 9499776
#    Student name: Tom Stark
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  Do-It-Yourself Periodical
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design and development to produce a
#  useful application for browsing the latest news in an area of your
#  own choice.  See the instruction sheet accompanying
#  this file for full details.
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import a constructor for converting byte data to character strings 
from StringIO import StringIO

# Import the Python Imaging Library module (comment this line out
# if you do not intend to use PIL in your solution)
from PIL import Image, ImageTk



##### DEVELOP YOUR SOLUTION HERE #####

## Python Imaging Library is a prerequisite module for this program, please download it to run the program properly   

##TO MARKER - I HAVE BEEN FIXING THE WEIRD HTML TAGS THAT COME UP IN THE SUMMARIES AND TITLES OF THE ARTICLES AS I GET THEM.
##BECAUSE I CAN'T FIND A LIST OF ALL POSSIBLE TAGS ON THE INTERNET, I CAN'T WRITE CODE TO COVER THEM ALL AS DIFFERENT TAGS
##CORRISPOND WITH DIFFERENT CHARACTERS. BECAUSE OF THIS MY FILTERS TO REMOVE THESE TAGS ARE QUITE LONG. IF ANY TAGS COME UP
##IT'S BECAUSE I DID NOT GET THAT PARTICULAR SCENARIO WHEN TESTING MY PAGES SO I COULDN'T UPDATE MY CODE TO FIX IT. I HOPE
##WHEN MARKING THIS EVERYTHING DISPLAYS FINE. :)

##TAGS FIXED SO FAR
# ' (opening)            &#8217;
# ' (closing)            &#8216;
# - (emdash)             &#8212;
# html tags             <i> </i> <b> </b>
# & (and character)      &amp;

#Making the GUI front end

the_window = Tk()
the_window.title('News Today - National News')
##
##
##
###Creating the Name of the Periodical and putting it in the window
labelfornewstoday = Label(the_window, text = 'News Today',font = ('Times', 48), fg = 'Gray')
labelfornewstoday.grid(row=0, columnspan=4)
##
##Creating the picture to be displayed on the opening page

#Converting the jpg file so tkinter can display it in a label
url= "http://f.tqn.com/y/journalism/1/L/T/7/-/-/169808021.jpg"
opentheurl = urlopen(url).read()
convert = StringIO(opentheurl)
opening = Image.open(convert)
print opening.size  #Original size
size = width, height = opening.size
##
newsize = (400, 250)
opening = opening.resize(newsize) 
print opening.size  #New size
##
newspaper = ImageTk.PhotoImage(opening)
##
##
#Create a Label and put the newspaper image into the label and then into the window
newspaperlabel = Label(the_window, image = newspaper)
newspaperlabel.grid(row=3,columnspan=4, padx=60, pady=20)

#Headling that is replaced 
headline = Label(the_window, text = [], font = ('Times', 20), fg = 'Black')
headline.grid(row=2,columnspan=4)

#Summary that is replaced
summary = Label(the_window, text = [], font = ('Times', 10), fg = 'Black', wraplength=500, justify=LEFT)
summary.grid(row=4,columnspan=4)

#Source URL that is replaced
source_url = Label(the_window, text = [], font = ('Times', 8), fg = 'Black')
source_url.grid(row=5,columnspan=4)

#Date that will be replaced
date_label = Label(the_window, text = [], font = ('Times', 15), fg = 'Black')
date_label.grid(row=1,columnspan=4)




#Making the Pages that change depending on results of regular expression

def technology():
    print "Technology info"
    
    #Open and read the technology page as a string
    url_technology = 'http://www.news.com.au/technology'
    technology_page = urlopen(url_technology).read()

    #Find the date    
    page_date = findall('tmstamp": "(.+)"', technology_page)[0]
    print page_date
    #Remove time thing off the date
    page_date_fixed = re.sub('\s\d+:\d+:\d+.\d+', "", page_date)
    print page_date_fixed

    #Find the Title of the article
    title_of_first_article = findall('<h4 class="heading">\s*<a href=".* >(.+)</a>', technology_page)[0]
    print title_of_first_article


    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe_title = re.sub('(&#8217;)', "'", title_of_first_article)
    print fix_apostrophe_title

    #Removing weird html tags (fix & character)
    fix_and_character_title = re.sub('(&amp;)', "&", fix_apostrophe_title)
    print fix_and_character_title

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character_title)
    print fix_html_tags

    #Removing weird html tags (fix other apostrophe tag)
    fix_other_apostrophe_title = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe_title

    #Removing weird html tags (fix emdash)
    title_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe_title)
    print title_filtered

    #Find picture for story
    technology_picture_url = findall('<img src="(.+)"\salt', technology_page)[0]
    print technology_picture_url

    #convert the picture
    imageread = urlopen(technology_picture_url).read()
    convert_bytes = StringIO(imageread)
    opening = Image.open(convert_bytes)
    #Change size of picture 
    print opening.size #original size
    size = width, height = opening.size
    ##
    newsize = (400, 250)
    opening = opening.resize(newsize)
    print opening.size #New size
    techimg = ImageTk.PhotoImage(opening)

    #Replace the current picture with image from article
    newspaperlabel.image = techimg
    newspaperlabel.configure(image=techimg)

    #Find the summary for the current top story
    technology_summary_first_article = findall('<p class="standfirst">\s+(.+)\s+<span', technology_page)[0]
    print technology_summary_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe = re.sub('(&#8217;)', "'", technology_summary_first_article)
    print fix_apostrophe

    #Removing weird html tags (fix & character)
    fix_and_character = re.sub('(&amp;)', "&", fix_apostrophe)
    print fix_and_character

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character)
    print fix_html_tags

    #Removing weird html tags (fix apostrophe tag)
    fix_other_apostrophe = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe

    #Removing weird html tags (fix apostrophe tag AND emdash)
    summary_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe)
    print summary_filtered 

    #Find the url of the original source of this data
    technology_url_source = findall('url:(.+)    -->', technology_page)[0]
    print technology_url_source

    #Putting above information in the GUI
    
    #Replace the current Date with the on in the webpage
    date_label.text = page_date_fixed
    date_label.configure(text=page_date_fixed)

    #Replace the current short summary
    summary.text = summary_filtered
    summary.configure(text=summary_filtered)
    
    #Replace the current title with title from article
    headline.text = title_filtered
    headline.configure(text=title_filtered)

    #Replace the current source URL with the one from the webpage
    source_url.text = technology_url_source
    source_url.configure(text=technology_url_source)


def sport():
    print "Sport info"
    
    #Open and read the sport page as a string
    url_sport = 'http://www.news.com.au/sport'
    sport_page = urlopen(url_sport).read()

    #Find the date    
    page_date = findall('tmstamp": "(.+)"', sport_page)[0]
    print page_date
    #Remove time thing off the date
    page_date_fixed = re.sub('\s\d+:\d+:\d+.\d+', "", page_date)
    print page_date_fixed

    #Find the Title of the article
    title_of_first_article = findall('<h4 class="heading">\s*<a href=".* >(.+)</a>', sport_page)[0]
    print title_of_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe_title = re.sub('(&#8217;)', "'", title_of_first_article)
    print fix_apostrophe_title

    #Removing weird html tags (fix & character)
    fix_and_character_title = re.sub('(&amp;)', "&", fix_apostrophe_title)
    print fix_and_character_title

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character_title)
    print fix_html_tags

    #Removing weird html tags (fix other apostrophe tag)
    fix_other_apostrophe_title = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe_title

    #Removing weird html tags (fix apostrophes tag AND emdash)
    title_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe_title)
    print title_filtered

    #Find picture for story
    sport_picture_url = findall('<img src="(.+)"\salt', sport_page)[0]
    print sport_picture_url

    #convert the picture
    imageread = urlopen(sport_picture_url).read()
    convert_bytes = StringIO(imageread)
    opening = Image.open(convert_bytes)
    #Change size of picture 
    print opening.size #original size
    size = width, height = opening.size
    ##
    newsize = (400, 250)
    opening = opening.resize(newsize)
    print opening.size #New size
    sportimg = ImageTk.PhotoImage(opening)
    #Replace the current picture with image from article
    newspaperlabel.image = sportimg
    newspaperlabel.configure(image=sportimg)

    #Find the summary for the current top story
    sport_summary_first_article = findall('<p class="standfirst">\s+(.+)\s+<span', sport_page)[0]
    print sport_summary_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe = re.sub('(&#8217;)', "'", sport_summary_first_article)
    print fix_apostrophe

    #Removing weird html tags (fix & character)
    fix_and_character = re.sub('(&amp;)', "&", fix_apostrophe)
    print fix_and_character

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character)
    print fix_html_tags 
    
    #Removing weird html tags (fix apostrophe tag)
    fix_other_apostrophe = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe

    #Removing weird html tags (fix apostrophe tag AND emdash)
    summary_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe)
    print summary_filtered 


    #Find the url of the original source of this data
    sport_url_source = findall('url:(.+)    -->', sport_page)[0]
    print sport_url_source

    #Putting the above information in the GUI

    #Replace the current Date with the on in the webpage
    date_label.text = page_date_fixed
    date_label.configure(text=page_date_fixed)
    
    #Replace the current short summary
    summary.text = summary_filtered
    summary.configure(text=summary_filtered)
    
    #Replace the current title with title from article
    headline.text = title_filtered 
    headline.configure(text=title_filtered)

    #Replace the current source URL with the one from the webpage
    source_url.text = sport_url_source
    source_url.configure(text=sport_url_source)


def travel():
    print "travel info"
    
    #Open and read the sport page as a string
    url_travel = 'http://www.news.com.au/travel'
    travel_page = urlopen(url_travel).read()

    #Find the date    
    page_date = findall('tmstamp": "(.+)"', travel_page)[0]
    print page_date
    #Remove time thing off the date
    page_date_fixed = re.sub('\s\d+:\d+:\d+.\d+', "", page_date)
    print page_date_fixed

    #Find the Title of the article
    title_of_first_article = findall('<h4 class="heading">\s*<a href=".* >(.+)</a>', travel_page)[0]
    print title_of_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe_title = re.sub('(&#8217;)', "'", title_of_first_article)
    print fix_apostrophe_title

    #Removing weird html tags (fix & character)
    fix_and_character_title = re.sub('(&amp;)', "&", fix_apostrophe_title)
    print fix_and_character_title

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character_title)
    print fix_html_tags

    #Removing weird html tags (fix other apostrophe tag)
    fix_other_apostrophe_title = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe_title

    #Removing weird html tags (fix apostrophes tag AND emdash)
    title_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe_title)
    print title_filtered

    #Find picture for story
    travel_picture_url = findall('<img src="(.+)"\salt', travel_page)[0]
    print travel_picture_url

    #convert the picture
    imageread = urlopen(travel_picture_url).read()
    convert_bytes = StringIO(imageread)
    opening = Image.open(convert_bytes)
    #Change size of picture 
    print opening.size #original size
    size = width, height = opening.size
    ##
    newsize = (400, 250)
    opening = opening.resize(newsize)
    print opening.size #New size
    travelimg = ImageTk.PhotoImage(opening)
    #Replace the current picture with image from article
    newspaperlabel.image = travelimg
    newspaperlabel.configure(image=travelimg)

    #Find the summary for the current top story
    travel_summary_first_article = findall('<p class="standfirst">\s+(.+)\s+<span', travel_page)[0]
    print travel_summary_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe = re.sub('(&#8217;)', "'", travel_summary_first_article)
    print fix_apostrophe

    #Removing weird html tags (fix & character)
    fix_and_character = re.sub('(&amp;)', "&", fix_apostrophe)
    print fix_and_character

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character)
    print fix_html_tags

    #Removing weird html tags (fix apostrophe tag)
    fix_other_apostrophe = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe

    #Removing weird html tags (fix apostrophe tag AND emdash)
    summary_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe)
    print summary_filtered 

    #Find the url of the original source of this data
    travel_url_source = findall('url:(.+)    -->', travel_page)[0]
    print travel_url_source

    #Putting the above information in the GUI

    #Replace the current Date with the on in the webpage
    date_label.text = page_date_fixed
    date_label.configure(text=page_date_fixed)
    
    #Replace the current short summary
    summary.text = summary_filtered
    summary.configure(text=summary_filtered)

    #Replace the current title with title from article
    headline.text = title_filtered
    headline.configure(text=title_filtered)

    #Replace the current source URL with the one from the webpage
    source_url.text = travel_url_source
    source_url.configure(text=travel_url_source)



def finance():
    print "Finance info"
    
    #Open and read the sport page as a string
    url_finance = 'http://www.news.com.au/finance'
    finance_page = urlopen(url_finance).read()

    #Find the date    
    page_date = findall('tmstamp": "(.+)"', finance_page)[0]
    print page_date
    #Remove time thing off the date
    page_date_fixed = re.sub('\s\d+:\d+:\d+.\d+', "", page_date)
    print page_date_fixed

    #Find the Title of the article
    title_of_first_article = findall('<h4 class="heading">\s*<a href=".* >(.+)</a>', finance_page)[0]
    print title_of_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe_title = re.sub('(&#8217;)', "'", title_of_first_article)
    print fix_apostrophe_title

    #Removing weird html tags (fix & character)
    fix_and_character_title = re.sub('(&amp;)', "&", fix_apostrophe_title)
    print fix_and_character_title

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character_title)
    print fix_html_tags

    #Removing weird html tags (fix other apostrophe tag)
    fix_other_apostrophe_title = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe_title

    #Removing weird html tags (fix apostrophes tag AND emdash)
    title_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe_title)
    print title_filtered

    #Find picture for story
    finance_picture_url = findall('<img src="(.+)"\salt', finance_page)[0]
    print finance_picture_url

    #convert the picture
    imageread = urlopen(finance_picture_url).read()
    convert_bytes = StringIO(imageread)
    opening = Image.open(convert_bytes)
    #Change size of picture 
    print opening.size #original size
    size = width, height = opening.size
    ##
    newsize = (400, 250)
    opening = opening.resize(newsize)
    print opening.size #New size
    financeimg = ImageTk.PhotoImage(opening)
    #Replace the current picture with image from article
    newspaperlabel.image = financeimg
    newspaperlabel.configure(image=financeimg)

    #Find the summary for the current top story
    finance_summary_first_article = findall('<p class="standfirst">\s+(.+)\s+<span', finance_page)[0]
    print finance_summary_first_article

    #Removing weird html tags (fix apostrophe tag)
    fix_apostrophe = re.sub('(&#8217;)', "'", finance_summary_first_article)
    print fix_apostrophe

    #Removing weird html tags (fix & character)
    fix_and_character = re.sub('(&amp;)', "&", fix_apostrophe)
    print fix_and_character

    #Removing weird html tags (fix <i> </i> <b> </b>) #Information in these tags are links to videos, these will be removed
    fix_html_tags = re.sub('(<i>.+>)', "", fix_and_character)
    print fix_html_tags

    #Removing weird html tags (fix apostrophe tag)
    fix_other_apostrophe = re.sub('(&#8216;)', "'", fix_html_tags)
    print fix_other_apostrophe

    #Removing weird html tags (fix apostrophe tag AND emdash)
    summary_filtered = re.sub('(&#8212;)', "-", fix_other_apostrophe)
    print summary_filtered 

    #Find the url of the original source of this data
    finance_url_source = findall('url:(.+)    -->', finance_page)[0]
    print finance_url_source

    
    #Putting the above information in the GUI

    #Replace the current Date with the on in the webpage
    date_label.text = page_date_fixed
    date_label.configure(text=page_date_fixed)
    
    #Replace the current short summary
    summary.text = summary_filtered
    summary.configure(text=summary_filtered)
    
    #Replace the current title with title from article
    headline.text = title_filtered
    headline.configure(text=title_filtered)

    #Replace the current source URL with the one from the webpage
    source_url.text = finance_url_source
    source_url.configure(text=finance_url_source)

    
#Create all radio buttons and postion them at the bottom of the window
v = IntVar()
#one radio
radioone= Radiobutton(the_window, text="Technology",value = 'one', variable=v, command=technology)
radioone.grid(row=6,column=0)
#two radio
radiotwo= Radiobutton(the_window, text="Sport",value = 'two', variable=v, command=sport)
radiotwo.grid(row=6,column=1)
#three radio
radiothree= Radiobutton(the_window, text="Travel",value = 'three', variable=v, command=travel)
radiothree.grid(row=6,column=2)
#four radio
radiofour= Radiobutton(the_window, text="Finance",value = 'four', variable=v, command=finance)
radiofour.grid(row=6,column=3)


#starts the event loop 
the_window.mainloop()

#
#--------------------------------------------------------------------#
