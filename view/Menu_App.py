



from domain.models.Guest import Guest
from domain.service.GuestService import GuestService
from application.GuestInput import GuestInput


class Menu_App:



    def __init__(self):
        self.guest = Guest(None, None,None,None,None,None,None,None,None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()


    def init_app(self):
        init = (int(input("Presione 1 para inicializar")))

        while init != 0:

            option = int(input("1. Login 2. registro 3. salir"))

            if option == 1:
                print("Login")
            elif option == 2:
                print("Registro")
                self.guest_input.register()
                self.guest_input.print_data()




