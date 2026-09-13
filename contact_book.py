def contact_book():
    k = []

    while True:
        print("\n" + "=" * 35)
        print("        CONTACT BOOK")
        print("=" * 35)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        print("=" * 35)

        i = input("Enter your choice (1-5): ")

        if i == "5":
            print("\nThank you for using Contact Book!")
            break

        if i == "1":
            while True:
                m = input("Enter contact (type 'exit' to stop): ")

                if m == "exit":
                    break

                k.append(m)
                print("Contact added successfully.")

        if i == "2":
            f = input("Enter the contact you want to search: ")

            found = False

            for u in k:
                if u == f:
                    print("Contact found!")
                    found = True
                    break

            if found == False:
                print("Contact not found.")

        if i == "3":
            print("\nAll Contacts:")
            print(k)

        if i == "4":
            h = input("Enter the contact you want to delete: ")

            if h in k:
                k.remove(h)
                print("Contact deleted:", h)
            else:
                print("Contact not found.")

            print("Current contacts:", k)


contact_book()
