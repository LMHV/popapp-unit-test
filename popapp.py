import unittest
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import time


class FindElements(unittest.TestCase):

    PATH_TO_DRIVER = 'C:/Users/lucho/Documents/ScriptsPythonFacultad/chromedriver.exe'
    PATH_TO_BROWSER = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
    NUEVO_PEDIDO_XPATH = '/html/body/app-root/div[2]/ng-component/div/div/div[1]/div[2]/atom-button/button'
    sheet_id = "1D8giXM4T4Egqs7a3wBfvTqo-Ih7AsL7ITp_D3NtFw-0"
    sheet_name = "Tipo Pedido"
    range = "A3:H54"

    URL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}&range={range}"
    URL = URL.replace(" ", "")

    def setUp(self):
        options = uc.ChromeOptions()
        options.user_data_dir = 'C:/Users/lucho/Documents/ScriptsPythonFacultad/profile'
        options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
        options.add_argument(
            '--no-first-run --no-service-autorun --password-store=basic')
        self.driver = uc.Chrome(options=options)
        self.driver.get(
            'https://test.popapp.io/ponline/pedidos/keyLeandroDrazic3/pendientes')
        wait = WebDriverWait(self.driver, 20)
        wait.until(Ec.visibility_of_element_located((By.XPATH, self.NUEVO_PEDIDO_XPATH)))

    def test_AgregarProducto(self):
        IDPAGE = 1884836248
        URL = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet_name}&range={self.range}&gid={IDPAGE}"
        URL = URL.replace(" ", "")

        driver = self.driver

        MOSTRADOR_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[1]/div[1]/img"
        ESTOYBUTTON_FULLXPATH = "/html/body/app-root/div[2]/ng-component/div/blur-message/div/atom-button/button"
        #INPUTNOMBRE_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[2]/atom-input/div/input"
        #INPUTDIRECCION_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[3]/atom-input/div/input"
        #INPUTTELEFONO_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[4]/atom-input/div/input"
        CONTINUARBUTTON_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[3]/atom-button/button"

        driver.find_element(By.XPATH, ESTOYBUTTON_FULLXPATH).click()
        driver.find_element(By.XPATH, self.NUEVO_PEDIDO_XPATH).click()

        driver.find_element(By.XPATH, MOSTRADOR_FULLXPATH).click()
        #INPUTNOMBRE = driver.find_element(By.XPATH, INPUTNOMBRE_FULLXPATH)
        #INPUTDIRECCION = driver.find_element(By.XPATH, INPUTDIRECCION_FULLXPATH)
        #INPUTTELEFONO = driver.find_element(By.XPATH, INPUTTELEFONO_FULLXPATH)

        driver.find_element(By.XPATH, CONTINUARBUTTON_FULLXPATH).click()

        driver.implicitly_wait(10)
        
        CsvFile = pd.read_csv(URL, sep=',', quotechar='"', na_filter=False)
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.max_rows', 50)
        pd.set_option('display.max_colwidth', 20)
        pd.set_option('display.width', 100)

        IDACTUAL = "CP1"

        #NOMBRE_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div[1]/div/p"
        #PRECIO_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div[1]/div/div/p"
        #FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div["
        BUTTON_FULLXPATH = "/div/div/atom-button/button"
        INPUTCANTIDAD_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/app-modal-agregar-producto/div[2]/div/div/form/div[1]/div[2]/div[1]/atom-input/div/input"
        BUTTON_AGREGARPEDIDO_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/app-modal-agregar-producto/div[2]/div/div/form/div[2]/atom-button/button"

        PrecioTotal = 0
        for index, row in CsvFile.iterrows():
            
            
            MAS_ELEMENTOS = True
            i = 0

            if(IDACTUAL != row['Id CP']):
                pass
                #Borrar cosas ingresadas y renovar valores

            while MAS_ELEMENTOS != False:
                i = i+1

                try:
                    NOMBREPRODUCTO = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div[" + str(i) + "]/div/p").text
                    if(NOMBREPRODUCTO == row['Productos']):

                        BUTTONPRODUCTO = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div[" + str(i) + "]" + BUTTON_FULLXPATH)
                        BUTTONPRODUCTO.click()

                        INPUTCANTIDAD = driver.find_element(By.XPATH, INPUTCANTIDAD_FULLXPATH)
                        INPUTCANTIDAD.clear()
                        INPUTCANTIDAD.send_keys(row['Cantidad'])

                        driver.find_element(By.XPATH, BUTTON_AGREGARPEDIDO_FULLXPATH).click()

                        LABEL_PRECIO = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[3]/div[2]/app-tablaproductos/div[" + str(i) + "]/div/div/p")
                        LABEL_PRECIO = LABEL_PRECIO.text
                        LABEL_PRECIO = LABEL_PRECIO[1:]
                        Precio = int(LABEL_PRECIO)
                        PrecioTotal = PrecioTotal + Precio


                except:
                    MAS_ELEMENTOS = False


    def test_TomarPedido(self):
        driver = self.driver

        ESTOYBUTTON_FULLXPATH = "/html/body/app-root/div[2]/ng-component/div/blur-message/div/atom-button/button"
        MOSTRADOR_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[1]/div[1]/img"
        DELIVERY_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[1]/div[2]/img"
        TAKEAWAY_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[1]/div[3]/img"
        INPUTNOMBRE_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[2]/atom-input/div/input"
        INPUTDIRECCION_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[3]/atom-input/div/input"
        INPUTTELEFONO_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[4]/atom-input/div/input"
        CONTINUARBUTTON_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[3]/atom-button/button"
        GOBACKBUTTON_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/app-cancelar-nuevopedido/div[2]/div/div/div[2]/div/atom-button[2]/button"
        ERRORTELEFONO_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[4]/small"
        ERRORDIRECCION_FULLXPATH = "/html/body/app-root/div[2]/ng-component/app-modal-tipoycliente/div[2]/div/div/div[2]/div[3]/small"
        NOMBRESIGPANTALLA_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[1]/div/div[2]/div[1]/strong"
        DIRECCIONSIGPANTALLA_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[1]/div/div[2]/div[1]/p[1]"
        TELEFONOSIGPANTALLA_FULLXPATH = "/html/body/app-root/div[2]/app-crear-pedido/app-nuevo-pedido-desktop/div/div/div/div[1]/div[1]/div/div[2]/div[1]/p[2]"


        # self.wait.until(Ec.visibility_of_element_located((By.XPATH, ESTOYBUTTON_FULLXPATH)))
        driver.find_element(By.XPATH, ESTOYBUTTON_FULLXPATH).click()
        driver.find_element(By.XPATH, self.NUEVO_PEDIDO_XPATH).click()

        CsvFile = pd.read_csv(self.URL, sep=',', quotechar='"', na_filter=False)
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.max_rows', 50)
        pd.set_option('display.max_colwidth', 20)
        pd.set_option('display.width', 100)

        for index, row in CsvFile.iterrows():
            MOSTRADORCHECKBOX = driver.find_element(By.XPATH, MOSTRADOR_FULLXPATH)
            DELIVERYCHECKBOX = driver.find_element(By.XPATH, DELIVERY_FULLXPATH)
            TAKEAWAYCHECKBOX = driver.find_element(By.XPATH, TAKEAWAY_FULLXPATH)
            INPUTNOMBRE = driver.find_element(By.XPATH, INPUTNOMBRE_FULLXPATH)
            INPUTDIRECCION = driver.find_element(By.XPATH, INPUTDIRECCION_FULLXPATH)
            INPUTTELEFONO = driver.find_element(By.XPATH, INPUTTELEFONO_FULLXPATH)
            CONTINUARBUTTON = driver.find_element(By.XPATH, CONTINUARBUTTON_FULLXPATH)
            time.sleep(1)

            # print("Checkbox: " + row['Checkbox'] + " Nombre: " + row['Nombre'])
            print("_________________________________")
            print(row['Id CP'])

            JS_ADD_TEXT_TO_INPUT = """
            var elm = arguments[0], txt = arguments[1];
            elm.value += txt;
            elm.dispatchEvent(new Event('input'));
            """


            if row['Checkbox'] == 'Mostrador':
                MOSTRADORCHECKBOX.click()
            elif row['Checkbox'] == 'Delivery':
                DELIVERYCHECKBOX.click()
            elif row['Checkbox'] == 'Take Away':
                TAKEAWAYCHECKBOX.click()

            if(row['Nombre'] != ""):
                driver.execute_script(JS_ADD_TEXT_TO_INPUT, INPUTNOMBRE, row['Nombre'])
                #INPUTNOMBRE.send_keys(row['Nombre'])
            if(row['Direccion'] != ""):
                INPUTDIRECCION.send_keys(row['Direccion'])
            if(row['Telefono'] != ""):
                INPUTTELEFONO.send_keys(row['Telefono'])

            CONTINUARBUTTON.click()
            time.sleep(1)
            URL = driver.current_url
            if(URL == 'https://test.popapp.io/ponline/pedido/keyLeandroDrazic3/new'):
                #Funcionó pedido
                print('Funciono pedido')

                #Verificar informacion = a la mostrada en pantalla
                try:
                    NombreSigPantalla = driver.find_element(By.XPATH, NOMBRESIGPANTALLA_FULLXPATH)
                    if(row['Nombre'] != ""):
                        if(row['Nombre'] != NombreSigPantalla.text):
                            print('Nombre en la siguiente pantalla es incorrecto.')
                except:
                    pass
                
                try:
                    DireccionSigPantalla = driver.find_element(By.XPATH, DIRECCIONSIGPANTALLA_FULLXPATH)
                    if(row['Direccion'] != ""):
                        if(("Direccion: " + row['Direccion']) != DireccionSigPantalla.text):
                            print('Direccion en la siguiente pantalla es incorrecto.')
                except:
                    pass

                try:
                    TelefonoSigPantalla = driver.find_element(By.XPATH, TELEFONOSIGPANTALLA_FULLXPATH)
                    if(row['Telefono'] != ""):
                        if(("Tel: " + row['Telefono']) != TelefonoSigPantalla.text):
                            print('Telefono en la siguiente pantalla es incorrecto.')
                except:
                    pass        

                print("_________________________________")

                #Volver atras
                driver.execute_script("window.history.go(-1)")
                GOBACKBUTTON = driver.find_element(By.XPATH, GOBACKBUTTON_FULLXPATH)
                GOBACKBUTTON.click()

                #Hasta aca funciona perfecto 
                #self.wait.until(Ec.visibility_of_element_located((By.XPATH, self.NUEVO_PEDIDO_XPATH)))
                time.sleep(1)
                driver.find_element(By.XPATH, self.NUEVO_PEDIDO_XPATH).click()
                

            
            else:
                #No pudo apretar el boton
                print('No funcionó')
                try:
                    ERRORTELEFONO = driver.find_element(By.XPATH, ERRORTELEFONO_FULLXPATH)
                    if(ERRORTELEFONO.text != ''):
                        print(ERRORTELEFONO.text)
                except:
                    print('El telefono no tiene error')

                try:
                    ERRORDIRECCION = driver.find_element(By.XPATH, ERRORDIRECCION_FULLXPATH)
                    if(ERRORDIRECCION.text != ''):
                        print(ERRORDIRECCION.text)
                except:
                    print('La direccion no tiene error')

                print("_________________________________")

                INPUTNOMBRE.clear()
                INPUTDIRECCION.clear()
                INPUTTELEFONO.clear()
                time.sleep(1)
                #Verificar que label de error se muestra en pantalla y guardarlo
    
    def test_tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()