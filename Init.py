from view.Menu_App import Menu_App

if __name__ == '__main__':
    print("Iniciando aplicación Hotel Saturday...")

    menu = Menu_App()

    try:
        menu.init_app()
    except KeyboardInterrupt:
        print("\nSaliendo por solicitud del usuario...")
        menu.exit_app()
    except Exception as e:
        print(f"\n❌ Ha ocurrido un error inesperado: {e}")
        if menu.db and hasattr(menu.db, 'connection') and menu.db.connection and menu.db.connection.is_connected():
            menu.db.disconnect()
    finally:
        print("Aplicación finalizada.")
