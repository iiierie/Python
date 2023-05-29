from  datetime import timedelta as td, datetime as dt
import time , arts
blocked_websites = []
redirect = "127.0.0.1"
host_path = "C:/Windows/System32/drivers/etc/hosts"

def view_blocked_sites():
    print("Blocked Sites:")
    for site in blocked_websites:
        print("- "+site)

def block():
    total_hours = int(input("For how many hours would you like to block these sites? "))
    ini_date = dt.now()
    end_date = ini_date + td(hours=total_hours)
    if ini_date < end_date:
        #need to block the site
        print("Blocking!")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for i in blocked_websites:
                if i not in content:
                    host_file.write(redirect + " "+ i + "\n")
            time.sleep(3)

def block_site_helper():
    site = input("Enter a site in the form of www.xyz.com to block: ")
    if site not in blocked_websites:
        blocked_websites.append(site)
        block()
        print(f"{site} has been blocked.")
    else:
        print(f"{site} is already blocked.")


def unblock_site_helper():
    site = input("Which site to unblock?  ")
    if site in blocked_websites:
        unblock();
        blocked_websites.remove(site)
        print(f"{site} has been unblocked.")
    else:
        print(f"{site} is not currently blocked at all.")



def unblock():
    with open(host_path, "r+") as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        for lines in content:
            if not any(redirect + " " + website + "\n" == lines for website in blocked_websites):
                host_file.write(lines)
        host_file.truncate()

def main():
    while True:
        print(arts.welcome)
        print("Menu:")
        print("1. View all blocked sites")
        print("2. Block a site")
        print("3. Unblock a site")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_blocked_sites()
        elif choice == "2":
            block_site_helper()
        elif choice == "3":
            unblock_site_helper()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        time.sleep(1)

    print("Exiting the program.")




main()