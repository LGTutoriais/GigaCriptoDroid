from kivymd.app import App, MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu_Inicial(Screen):
    pass

class Tipo_Criptografia(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "menu_inicial"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    pass

class Tipo_Descriptografia(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "menu_inicial"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    pass

class Criptografia_Chave_Simples(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "tipo_criptografia"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def criptografar_chave_simples(self):
        msg = str(self.ids.mensagem_cripto_chave_simples.text).upper().replace(" ","")
        msg += "@" * ((5 - (len(msg) % 5)) % 5 - 2)
        msg_crypto = ""

        chave_simples = str(self.ids.cripto_chave_simples.text).upper().replace(" ","").replace("-","")
        chave_simples_em_ordem_alfabetica = ''.join(sorted(chave_simples.replace(" ", "")))

        num_linhas = len(msg) // len(chave_simples)
        letras_ultima_linha = len(msg) % len(chave_simples)
        num_colunas = len(chave_simples)

        if letras_ultima_linha != 0:
            num_linhas += 1

        chave_simples_ordenada = chave_simples

        for i in range(0, len(chave_simples)):
            chave_simples_ordenada = chave_simples_ordenada.replace(
                chave_simples_ordenada[
                    chave_simples_ordenada.find(str(chave_simples_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_simples_ordenada = chave_simples_ordenada.split(" ")

        ordem_colunas = []
        for i in range(0, len(chave_simples_ordenada) - 1):
            ordem_colunas.append(int(chave_simples_ordenada[i]))

        batalha_naval = {}
        cont = 0

        for i in range(1, num_linhas + 1):
            for a in range(1, num_colunas + 1):
                try:
                    batalha_naval[f"{i}-{ordem_colunas[a - 1]}"] = str(msg[cont])
                    cont += 1
                except:
                    break
                if cont == len(msg):
                    break
            if cont == len(msg):
                break

        for a in range(1, num_colunas + 1):
            for i in range(1, num_linhas + 1):
                try:
                    msg_crypto += str(batalha_naval[f"{i}-{a}"])
                except:
                    continue

        self.ids.resultado_cripto_chave_simples.text = str(f"MENSAGEM CRIPTOGRAFADA:\n{msg_crypto}")
    pass

class Criptografia_Chave_Dupla(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "tipo_criptografia"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def criptografar_chave_dupla(self):
        msg = str(self.ids.mensagem_cripto_chave_dupla.text).upper().replace(" ","")
        msg += "@" * ((5 - (len(msg) % 5)) % 5 - 2)
        msg_crypto=""

        # Processo de criptografia por chave dupla

        chave_dupla1 = str(self.ids.cripto_chave_dupla_1.text).upper().replace(" ","")
        chave_dupla2 = str(self.ids.cripto_chave_dupla_2.text).upper().replace(" ","")

        chave_dupla2 += "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

        chave1_em_ordem_alfabetica = ''.join(sorted(chave_dupla1.replace(" ", "")))
        chave2_em_ordem_alfabetica = ''.join(sorted(chave_dupla2.replace(" ", "")))

        num_linhas = len(msg) // len(chave_dupla1)
        letras_ultima_linha = len(msg) % len(chave_dupla1)
        num_colunas = len(chave_dupla1)

        if letras_ultima_linha != 0:
            num_linhas += 1

        chave_dupla1_ordenada = chave_dupla1

        for i in range(0, len(chave_dupla1)):
            chave_dupla1_ordenada = chave_dupla1_ordenada.replace(
                chave_dupla1_ordenada[chave_dupla1_ordenada.find(str(chave1_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_dupla1_ordenada = chave_dupla1_ordenada.split(" ")

        chave_dupla2_ordenada = chave_dupla2
        for i in range(0, len(chave_dupla2)):
            chave_dupla2_ordenada = chave_dupla2_ordenada.replace(
                chave_dupla2_ordenada[chave_dupla2_ordenada.find(str(chave2_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_dupla2_ordenada = chave_dupla2_ordenada.split(" ")

        ordem_colunas = []
        for i in range(0, len(chave_dupla1_ordenada) - 1):
            ordem_colunas.append(int(chave_dupla1_ordenada[i]))

        ordem_linhas = []
        for i in range(0, len(chave_dupla2_ordenada) - 1):
            ordem_linhas.append(int(chave_dupla2_ordenada[i]))

        batalha_naval = {}
        cont = 0

        for i in range(1, num_linhas + 1):
            for a in ordem_colunas:
                try:
                    batalha_naval[f"{ordem_linhas[i - 1]}-{a}"] = str(msg[cont])
                    cont += 1
                except:
                    if cont == len(msg):
                        break
            if cont == len(msg):
                break

        for i in range(1, num_colunas + 1):
            for a in range(1, num_linhas + 1):
                try:
                    msg_crypto += str(batalha_naval[f"{a}-{i}"])
                except:
                    continue

        self.ids.resultado_cripto_chave_dupla.text = str(msg_crypto)

    pass

class Descriptografia_Chave_Simples(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "tipo_descriptografia"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def descriptografar_chave_simples(self):
        msg = str(self.ids.mensagem_descripto_chave_simples.text).upper().replace(" ","")
        msg_decrypto=""
        chave_simples = str(self.ids.descripto_chave_simples.text).upper().replace(" ", "")
        chave_simples_em_ordem_alfabetica = ''.join(sorted(chave_simples.replace(" ", "")))
        num_linhas = len(msg) // len(chave_simples)
        letras_ultima_linha = len(msg) % len(chave_simples)
        num_colunas = len(chave_simples)

        if letras_ultima_linha != 0:
            num_linhas += 1

        num_letras_mortas = (num_colunas * num_linhas) - len(msg)

        chave_simples_ordenada = chave_simples

        for i in range(0, len(chave_simples)):
            chave_simples_ordenada = chave_simples_ordenada.replace(
                chave_simples_ordenada[
                    chave_simples_ordenada.find(str(chave_simples_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_simples_ordenada = chave_simples_ordenada.split(" ")

        ordem_colunas = []
        for i in range(0, len(chave_simples_ordenada) - 1):
            ordem_colunas.append(int(chave_simples_ordenada[i]))

        linhas = []
        for i in range(1, num_linhas + 1):
            linhas.append(i)

        batalha_naval = {}

        cont = 0

        for i in range(num_linhas, 0, -1):
            try:
                for a in range(num_colunas, 0, -1):
                    batalha_naval[f"{i}-{ordem_colunas[a - 1]}"] = "@"
                    cont += 1
                    if cont == num_letras_mortas:
                        break
                if cont == num_letras_mortas:
                    break
            except:
                continue

        cont = 0

        for i in range(1, num_colunas + 1):
            for a in range(1, num_linhas + 1):
                try:
                    if batalha_naval[f"{a}-{i}"] == "@":
                        continue
                except:
                    try:
                        batalha_naval[f"{a}-{i}"] = str(msg[cont])
                        cont += 1
                    except:
                        break
                    if cont == len(msg):
                        break
            if cont == len(msg):
                break

        loop_break = False

        for line in range(1, num_linhas + 1):
            for column in ordem_colunas:
                try:
                    if str(batalha_naval[f"{line}-{column}"]) == "@":
                        loop_break = True
                        break

                    msg_decrypto += str(batalha_naval[f"{line}-{column}"])
                except:
                    continue

            if loop_break:
                break

        self.ids.resultado_descripto_chave_simples.text = str(f"A MENSAGEM DESCRIPTOGRAFADA É:\n{msg_decrypto}")

    pass

class Descriptografia_Chave_Dupla(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "tipo_descriptografia"
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def descriptografar_chave_dupla(self):
        msg = str(self.ids.mensagem_descripto_chave_dupla.text).upper().replace(" ", "")
        msg_decrypto = ""

        chave_dupla1 = str(self.ids.descripto_chave_dupla1.text).upper().replace(" ", "").replace("-", "")
        chave_dupla2 = str(self.ids.descripto_chave_dupla2.text).upper().replace(" ", "").replace("-", "")
        chave_dupla2 += "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

        chave1_em_ordem_alfabetica = ''.join(sorted(chave_dupla1.replace(" ", "")))
        chave2_em_ordem_alfabetica = ''.join(sorted(chave_dupla2.replace(" ", "")))

        num_colunas = len(chave_dupla1)
        num_linhas = len(chave_dupla2)
        num_letras_mortas = (num_linhas * num_colunas) - len(msg)

        chave_dupla1_ordenada = chave_dupla1
        chave_dupla2_ordenada = chave_dupla2

        for i in range(0, len(chave_dupla1)):
            chave_dupla1_ordenada = chave_dupla1_ordenada.replace(
                chave_dupla1_ordenada[chave_dupla1_ordenada.find(str(chave1_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_dupla1_ordenada = chave_dupla1_ordenada.split(" ")

        ordem_colunas = []
        for i in range(0, len(chave_dupla1_ordenada) - 1):
            ordem_colunas.append(int(chave_dupla1_ordenada[i]))

        for i in range(0, len(chave_dupla2)):
            chave_dupla2_ordenada = chave_dupla2_ordenada.replace(
                chave_dupla2_ordenada[chave_dupla2_ordenada.find(str(chave2_em_ordem_alfabetica[i]))],
                str(i + 1) + " ", 1)

        chave_dupla2_ordenada = chave_dupla2_ordenada.split(" ")

        ordem_linhas = []
        for i in range(0, len(chave_dupla2_ordenada) - 1):
            ordem_linhas.append(int(chave_dupla2_ordenada[i]))

        batalha_naval = {}
        cont = 0

        for i in range(1, num_linhas + 1):
            for a in range(1, num_colunas + 1):
                batalha_naval[f"{i}-{a}"] = ""

        for i in range(num_linhas, 0, -1):
            for a in range(num_colunas, 0, -1):
                try:
                    batalha_naval[f"{ordem_linhas[i - 1]}-{ordem_colunas[a - 1]}"] = "@"
                    cont += 1
                except:
                    break
                if cont == num_letras_mortas:
                    break
            if cont == num_letras_mortas:
                break

        cont = 0

        for a in range(1, num_colunas + 1):
            for i in range(1, num_linhas + 1):
                if batalha_naval[f"{i}-{a}"] == "@":
                    continue
                else:
                    batalha_naval[f"{i}-{a}"] = str(msg[cont])
                    cont += 1
                    if cont == len(msg):
                        break
            if cont == len(msg):
                break

        break_loop = False

        for i in range(1, num_linhas + 1):
            for a in range(1, num_colunas + 1):
                if batalha_naval[f"{ordem_linhas[i - 1]}-{ordem_colunas[a - 1]}"] == "@":
                    break_loop = True
                    break
                msg_decrypto += str(batalha_naval[f"{ordem_linhas[i - 1]}-{ordem_colunas[a - 1]}"])
            if break_loop:
                break

        self.ids.resultado_descripto_chave_dupla.text = str(f"A MENSAGEM DESCRIPTOGRAFADA É:\n{msg_decrypto}")

    pass

class main(MDApp):
    def build(self):
        return Gerenciador()

main().run()