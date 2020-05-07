import unittest
from appium import webdriver
import time


class AbreGooglePlay(unittest.TestCase):
    desired_capabilities = {}
    driver = None

    def setUp(self):
        self.desired_capabilities['deviceName'] = "0057652396"
        self.desired_capabilities['platformName'] = "Android"
        self.desired_capabilities["platformVersion"] = "9.0"
        self.desired_capabilities['appPackage'] = "com.android.vending"
        self.desired_capabilities['appActivity'] = ".AssetBrowserActivity"
        self.desired_capabilities['appWaitActivity'] = ".AssetBrowserActivity"
        self.desired_capabilities['deviceReadyTimeout'] = "40"
        self.desired_capabilities['newCommandTimeout'] = "180"
        self.desired_capabilities['deviceOrientation'] = "portrait"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def evokeGooglePlay(self):
        test_app_name = "instagram"
        time.sleep(1)  # tempo para esperar o programa aparecer na tela
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().resourceId(\"com.android.vending:id/search_box_idle_text\")").click()

        # pesquisa o nome do aplicativo
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(test_app_name)

        #clica no elemento que aparece o nome do aplicativo desejado
        time.sleep(1) #espera o app abrir
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().resourceId(\"com.android.vending:id/suggest_text\").text(\"" + testAppName.lower() + "\")")\
            .click();

        #espera a página do aplicativo na playstore abrir
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().resourceId(\"com.android.vending:id/li_title\").text(\"" + testAppName + "\")")

        #clica no ponto triplo do tile do app
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//android.widget.TextView[@content-desc=\"App: " + testAppName +
            "\"]/following-sibling::android.widget.ImageView[@resource-id=\"com.android.vending:id/li_overflow\"]"
        ).click()

        #clica no botão instalar
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").resourceId(\"com.android.vending:id/title\").text(\"Install\"
        ).click()

        #clica aceitar instalação
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().resourceId(\"com.android.vending:id/continue_button\")"
        ).click()

        if time.clock_settime(webdriver, INSTALL_DURATION_IN_SECONDS) == True:
            self.driver.find_element_by_android_view_matcher(
                self.driver.find_element_by_xpath(
                    "//android.widget.TextView[@content-desc=\"App: " + testAppName +
                    "\"]/following-sibling::android.view.View[@resource-id=\"com.android.vending:id/li_label\"][@content-desc=\"Installed\"
                )
            )

        self.driver.quit()

    def launchTestApp(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_capabilities)
        self.driver.launch_app("com.android.instagram")
        self.driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"android:id/alertTitle\")")

        #colocando credenciais de usuário teste
        username = "loremipsum@gmail.com"
        pw = "loremipsum"

        time.sleep(1)  # tempo para esperar o programa aparecer na tela
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().resourceId(\"com.android.instagram:id/search_box_idle_text\")").click()
        #insere username
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(username)
        #insere password
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(pw)

        #clica botão login
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").resourceId(\"com.android.instagram:id/title\").text(\"Login\"
        ).click()

if __name__ == '__main__':
    unittest.main()
