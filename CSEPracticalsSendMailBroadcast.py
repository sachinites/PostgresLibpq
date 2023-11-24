# To use this program, install the below python module 
# pip install psycopg2 panda openpyxl

#!/usr/bin/env python

import psycopg2
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

referral_links = [
    # Multi Threading Courses
    {"Category" : "POSIX Multithreading (pthreads)", "title": "Part A - Multithreading & Thread Synchronization in C/C++", "url": "https://www.udemy.com/course/advanced-skt-prog/?referralCode=725CE8057ADE6506EF95", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},
    {"Category" : "POSIX Multithreading (pthreads)", "title": "Part B (ADV) Multithreading Design Patterns in C/C++", "url": "https://www.udemy.com/course/tcpipstack_b/?referralCode=210EED3DDB079FA45AAF", "TOC" : ['Chapter4', 'Chapter5', 'Chapter6']},

    {"Category" : "POSIX Multithreading (pthreads)", "title": "Asynchronous Programming Design Patterns - C/C++", "url": "https://www.udemy.com/course/eventloop/?referralCode=BA6B2C04D5A51A8F9345", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    # Linux System Programming Courses
    {"Category" : "Linux System Programming Courses", "title": "Linux System Programming Techniques & Concepts", "url": "https://www.udemy.com/course/advance-programming-concepts/?referralCode=7B563B2B3364A8F05774", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "Linux Inter-Process Communication (IPC) from Scratch in C", "url": "https://www.udemy.com/course/linuxipc/?referralCode=699CE15DDDB84667B2F4", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "System C/C++ Course on Linux Timers Implementation & Design", "url": "https://www.udemy.com/course/wheeltimers/?referralCode=0A869289160EFB73389A", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "Operating System Project - Develop Heap Memory Manager in C", "url": "https://www.udemy.com/course/os-project-lmm/?referralCode=300551829F89C8F3E7C2", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "Linux Kernel Programming - IPC b/w Userspace and KernelSpace", "url": "https://www.udemy.com/course/netlinksockets/?referralCode=8410B4DC605FD98DF663", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "Coding Project - Programming Finite State Machines", "url": "https://www.udemy.com/course/fsmproject/?referralCode=4459915D346008C5CEF1", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "System C Project - Write a Garbage Collector from Scratch", "url": "https://www.udemy.com/course/memory-leak-detector/?referralCode=B856D6ED36421F49BA2C", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Linux System Programming Courses", "title": "Build Remote Procedure Calls (RPC) - from scratch in C", "url": "https://www.udemy.com/course/linuxrpc/?referralCode=013BBA060BEDDE9240AC", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},
    
    {"Category" : "Linux System Programming Courses", "title": "Writing Parsers in C++ ( for MathExpressions / SQL etc )", "url": "https://www.udemy.com/course/parserdev/?referralCode=3666C4152A902D6899F7", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    # Networking Projects
    {"Category" : "Networking Coding Projects", "title": "Part A - Networking Projects - Implement TCP/IP Stack in C", "url": "https://www.udemy.com/course/tcpipstack/?referralCode=83CF8FB4DE8E4C0D42E4", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},
    {"Category" : "Networking Coding Projects", "title": "Part B - Networking Projects - Implement TCP/IP Stack in C", "url": "https://www.udemy.com/course/tcpipstack_b/?referralCode=210EED3DDB079FA45AAF", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Networking Coding Projects", "title": "Part A - Networking Project - Protocol Development from Scratch", "url": "https://www.udemy.com/course/nwdev_from_scratch/?referralCode=35963EC2AB12547279AE", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},
    {"Category" : "Networking Coding Projects", "title": "Part B - Networking Project - Protocol Development from Scratch", "url": "https://www.udemy.com/course/nw_proto_dev_partb/?referralCode=807B0866BA3FC49F46ED", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Networking Coding Projects", "title": "Advanced TCP/IP Socket Programming in C/C++ ( Posix )", "url": "https://www.udemy.com/course/advanced-skt-prog/?referralCode=725CE8057ADE6506EF95", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    #Networking Theory
    {"Category" : "Networking Theory", "title": "Network Concepts and Programming from Scratch - Academic LvL", "url": "https://www.udemy.com/course/network-programming-from-scratch/?referralCode=8429AB9086AAC85C586E", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Networking Theory", "title": "Master Class: TCP/IP Mechanics from Scratch to Expert", "url": "https://www.udemy.com/course/tcpmasterclass/?referralCode=A61E6BAB1B4E25E5A097", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']}

]

free_links = [

# Free Courses
    {"Category" : "Free", "title": "Integrate CLI interface to your C/C++ Projects Quickly", "url": "https://www.udemy.com/course/clilibrary/?couponCode=323D22C67EF1030BD71E", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Free", "title": "Understanding Domain Name System (passwd : dnsfreecourse)", "url": "https://www.udemy.com/course/dnsguide/", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Free", "title": "C/C++ : Start Using Timer Library in Just 30 Minutes ! (passwd : timerlib)", "url": "https://www.udemy.com/course/30min_timer_lib_tutorial/", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Free", "title": "Learn Writing GNU Makefile in 30 minutes ! (passwd : gnupasswd)", "url": "https://www.udemy.com/course/gnu-makefile/?referralCode=02A712D6E4F4CCA34893", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']},

    {"Category" : "Free", "title": "Network Security - Implement L3 Routing Table & ACL in C/C++ (Send us Invitation)", "url": "https://www.udemy.com/course/access-control-list/?referralCode=FB4D938136F3D2FE2D31", "TOC" : ['Chapter1', 'Chapter2', 'Chapter3']}

]

utube_playlist_links = [

    {"Category" : "Networking Dev", "title": "L3 Routing Table Data Structure", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ58FBJobXN-KJ5YCi8KNgSO", "TOC" : []},

    {"Category" : "Networking Dev", "title": "Construction of L3 Routing Table", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ4avtTCCzmGeXSrTz-pH7x2", "TOC" : []},

    {"Category" : "Multi-Threading", "title": "Recursive Mutexes", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ6hO79_Vw79HP7ju4SoSGKn", "TOC" : []},

    {"Category" : "Multi-Threading",  "title": "Thread Cancellation", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ7D1O3nCep-3sx9gMosLCcc", "TOC" : []},

    {"Category" : "Multi-Threading",  "title": "Posix Threading", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ5MlzhfYEVS3vtBqRd6Xznt", "TOC" : []},

    {"Category" : "Operating System", "title": "Heap Memory Management", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ6XzyEsmrv34qwSap98TYXf", "TOC" : []},

    {"Category" : "Multi-Threading",  "title": "Semaphores", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ6XuFzsCbP84MNtH_I78Tth", "TOC" : []},

    {"Category" : "Linux System Programming", "title": "Linux Timers", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ65fDDtjgKvc2RFqA78OykW", "TOC" : []},

    {"Category" : "Data Structure",  "title": "Offset Based LinkedList", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ5aHJn8qW3x4NCuVcdNhhRD", "TOC" : []},

    {"Category" : "Linux System Programming", "title": "IPC - Unix Domain Sockets", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ67Mru9fNUUb3BThF9dIZOA", "TOC" : []},

    {"Category" : "Operating System", "title": "Stack Memory Management", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ751TwsaWnppSSs93BJDgqR", "TOC" : []},

    {"Category" : "Multi-Threading",  "title": "Thread Pools", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ6Kd8U-B9GtWvD5RABWoWci", "TOC" : []},

    {"Category" : "Operating System",  "title": "Select System Call", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ5MYm41p33sNEObe1S-g-cQ", "TOC" : []},

    {"Category" : "Multi-Threading",  "title": "Implement Thread Safe CRUD Operations", "url": "https://www.youtube.com/playlist?list=PLN9r3gitIiJ6kRQ0CPO02gEON10n5N66C", "TOC" : []},

    {"Category" : "Linux System Programming", "title": "Implement Device Drivers From Scratch", "url": "https://www.youtube.com/playlist?list=PLlrqp8hxLfoqSIQFrGbAM5lv5uAnZBB61", "TOC" : []}
]

def generate_html_with_links(links):
    html_links = ""
    for link in links:
        html_links += f'<p>&nbsp;&nbsp;&nbsp;&nbsp;<a href="{link["url"]}">{link["Category"]} : {link["title"]}</a></p>'
        if (0 and len(link["TOC"])):
            html_links += f"""
            <details>
                <summary>Table of Contents</summary>"""
            for toc in link["TOC"]:
                html_links +=   f"""
                <ul>  <li>{toc}</li>  </ul>
            </details>"""
    return html_links


def read_emails_from_sqldb():

    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    
    # Retrieve email addresses from the table
    #cursor.execute("SELECT email FROM students where name in ('Abhishek Sagar', 'Shivani Nigam')" )
    cursor.execute("SELECT email FROM students" )
    email_records = cursor.fetchall()
    
    email_addresses = [record[0] for record in email_records]
    
    cursor.close()
    conn.close()
    return email_addresses



def prepare_generic_advt_msg():

    msg = MIMEMultipart()

    html = f"""\
    <!DOCTYPE html>
    <html>

    <head>

    </head>

    <body>
        <h1>Hi, Greetings from CSEPracticals.</h1>
        <h2>Here we offer 21 Courses on System Programming, Operating Systems, and Networking with Projects.</h2>
        <h3>Courses: visit <a href="https://www.csepracticals.com">www.csepracticals.com</a></h3>

    <h2><b>Paid Courses </b></h2>
        """
    html += generate_html_with_links(referral_links)
    html += f"""<h2> </b>Free Courses </b></h2> """
    html += generate_html_with_links(free_links)

    html += f"""\
     <br><br>
    <h2>How to get access?</h2>
    <h3>You can purchase and get lifetime access to all the Courses for as little as $65. Click <a href="https://pages.razorpay.com/pl_L0ByDzv3MVixu1/view">here</a> to avail the offer. Access will be given on Udemy only </h3>
    <br><br><br>
    <h2> Free Resources </h2>
    <h3> Free Life time access to Collection to all Ebooks, PPTs, PDFs, and other resources on System and Networking Programming </h3>
    <h3><a href="https://payhip.com/b/lZmKM">  Free Resources (Sign Up Required) </a></h3>
    <br><br><br>
    <h2> Subscribe to Our <a href="https://www.youtube.com/@CSEPracticals/">Youtube Channel</a> </h3>
    <h3> Youtube Playlists </h4>
    """
    html += generate_html_with_links(utube_playlist_links)

    html += f"""\
    <h4>Thanks, Team CSEPracticals</h4>
    <h4>Join our telegram grp : telecsepracticals</h4>
    <h4> email : csepracticals@gmail.com </h4>
    <h4> Website : <a href="https://www.csepracticals.com">www.csepracticals.com</a></h4>
        </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))
    return msg




def send_email(sender_email, sender_password, subject, recipient_email_list, msg):

    msg['Subject'] = subject
    msg['From'] = sender_email
    bcc_recipients = ', '.join(recipient_email_list)
    msg['Bcc'] = bcc_recipients

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.close()
        print("Email sent successfully to " +  str(len(recipient_email_list)) + " recipients")
        print ("Recipients : ", bcc_recipients)
    except Exception as e:
        print("Failed to send email, exception : ", str(e))


#email_addresses = ['sachinites@gmail.com']
email_addresses = read_emails_from_sqldb()
sender_email = "csepracticals@gmail.com"
sender_password = "kcryywrjdlwjbxzj"
subject = "CSEPracticals 21 Courses on Networking, Projects, and System Programming."
msg = prepare_generic_advt_msg()

send_email(sender_email, sender_password, subject, email_addresses, msg)
