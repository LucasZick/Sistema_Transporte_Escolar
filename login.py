from PyQt5 import uic,QtWidgets
from datetime import datetime
import sqlite3

def chamaTelaLogin():
    telaLogin.show()

def chamaTelaRegistro():
    telaRegistro.show()
    telaLogin.close()
        
def chamaTelaPrincipal():
    telaPrincipal.show()
    telaLogin.close()
    if telaRegistro:
        telaRegistro.close()
    atualizarTabela()

def chamaTelaInserirPessoa():
    telaPrincipal.close()
    telaInserirPessoa.show()

def chamaTelaRemoverPessoa():
    telaPrincipal.close()
    telaRemoverPessoa.show()

def chamaTelaAtualizarPessoa():
    telaPrincipal.close()
    telaAtualizarPessoa.show()

def login():
    login_usuario = telaLogin.lineEdit_login.text()
    senha_usuario = telaLogin.lineEdit_senha.text()
    if senha_usuario != '' and login_usuario != '':
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()   
        try:
            cursor.execute(f"SELECT senha FROM cadastro WHERE login = '{login_usuario}'")
            senha_bd = cursor.fetchall()
            banco.close()
            if senha_usuario == senha_bd[0][0]:
                chamaTelaPrincipal()
            else:
                telaLogin.label_aviso.setText('A senha está incorreta.')
        except:
            telaLogin.label_aviso.setText('Registro incompatível.')
    else:
        telaLogin.label_aviso.setText('Dados insuficientes para realizar o login.')

def logout():
    telaPrincipal.close()
    telaLogin.show()
    telaLogin.lineEdit_login.setText('')
    telaLogin.lineEdit_senha.setText('')
    telaLogin.label_aviso.setText('')

def cadastrar():
    nome = telaRegistro.lineEdit_nome.text()
    login = telaRegistro.lineEdit_loginCadastro.text()
    senha = telaRegistro.lineEdit_senhaCadastro.text()
    senhaConfirma = telaRegistro.lineEdit_senhaConfirma.text()

    if (login != '' and nome != '' and senha == senhaConfirma):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, login text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit()
            banco.close

            sairRegistro()

        except sqlite3 as erro:
            telaRegistro.label_aviso.setText('Erro ao cadastrar o usuário.', erro)

    else:
        telaRegistro.label_aviso.setText('Cheque se preencheu todos os dados\ne confirme-se que as senhas estão iguais.')

def inserirAluno():
    turno = ''
    van = ''
    try:    
        nome = telaInserirPessoa.lineEdit_nome.text()
        nomePai = telaInserirPessoa.lineEdit_nomePai.text()
        nomeMae = telaInserirPessoa.lineEdit_nomeMae.text()
        telefone = telaInserirPessoa.lineEdit_telefone.text()
        endereco = telaInserirPessoa.lineEdit_endereco.text()
        escola = telaInserirPessoa.lineEdit_escola.text()
        mensalidade = int(telaInserirPessoa.lineEdit_mensalidade.text())
        data = datetime.today().strftime('%d-%m-%Y')
    except ValueError as erro:
        telaInserirPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex(250).{erro}')

    #Molda a variável turno
    if telaInserirPessoa.radioButton_manha.isChecked() == True:
        turno = turno+' Manhã.'
    if telaInserirPessoa.radioButton_tarde.isChecked() == True:
        turno = turno+' Tarde. '
    if telaInserirPessoa.radioButton_noite.isChecked() == True:
        turno = turno+' Noite.'

    #Molda a variável van
    if telaInserirPessoa.radioButton_van1.isChecked() == True:
        van = 'Van 1'
    if telaInserirPessoa.radioButton_van2.isChecked() == True:
        van = 'Van 2'

    try:
        if nome != '' and (nomePai != '' or nomeMae != '') and telefone != '' and endereco != '' and escola != '' and mensalidade:
            try:
                banco = sqlite3.connect('banco_alunos.db')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS alunos (nome text, nome_do_pai text, nome_da_mae text, telefone text, endereco text, escola text, mensalidade int, turno text, van text)")
                cursor.execute(f"INSERT INTO alunos(nome,nome_do_pai,nome_da_mae,telefone,endereco,escola,mensalidade,turno,van,pagou_mes,data_inicio) VALUES ('{nome}','{nomePai}','{nomeMae}','{telefone}','{endereco}','{escola}',{mensalidade},'{turno}','{van}', 0, '{data}')")

                banco.commit()
                banco.close

                atualizarTabela()
                sairInsercao()

            except Exception as erro:
                telaInserirPessoa.label_aviso.setText(f'Erro ao cadastrar o aluno.\n{erro}')

        else:
            telaInserirPessoa.label_aviso.setText('Problema ao inserir aluno, verifique se\n todos os campos foram preenchidos.')
    except:
            telaInserirPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex: (100).')

def verificarAluno():
    try:
        codigoAluno = telaRemoverPessoa.lineEdit_codigo.text()
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute(f"SELECT nome FROM alunos WHERE codigo = {codigoAluno}")
        nome = cursor.fetchall()
        banco.close()
        if nome != '':
            telaRemoverPessoa.label_aviso.setText(f'Realmente deseja remover {nome[0][0]}?')
            telaRemoverPessoa.pushButton_remover.setEnabled(True)
    except:
        telaRemoverPessoa.label_aviso.setText('Erro ao buscar o aluno.\nVerifique se este código existe.\n\nObs: códigos de alunos são numéricos.')

def resetVerificarAluno():
    telaAtualizarPessoa.pushButton_editar.setEnabled(False)

    telaAtualizarPessoa.lineEdit_nome.setText('')
    telaAtualizarPessoa.lineEdit_nome.setEnabled(False)

    telaAtualizarPessoa.lineEdit_nomePai.setText('')
    telaAtualizarPessoa.lineEdit_nomePai.setEnabled(False)

    telaAtualizarPessoa.lineEdit_nomeMae.setText('')
    telaAtualizarPessoa.lineEdit_nomeMae.setEnabled(False)

    telaAtualizarPessoa.lineEdit_telefone.setText('')
    telaAtualizarPessoa.lineEdit_telefone.setEnabled(False)

    telaAtualizarPessoa.lineEdit_endereco.setText('')
    telaAtualizarPessoa.lineEdit_endereco.setEnabled(False)

    telaAtualizarPessoa.lineEdit_escola.setText('')
    telaAtualizarPessoa.lineEdit_escola.setEnabled(False)

    telaAtualizarPessoa.lineEdit_mensalidade.setText('')
    telaAtualizarPessoa.lineEdit_mensalidade.setEnabled(False)

    telaAtualizarPessoa.radioButton_manha.setEnabled(False)
    telaAtualizarPessoa.radioButton_tarde.setEnabled(False)
    telaAtualizarPessoa.radioButton_noite.setEnabled(False)
    telaAtualizarPessoa.radioButton_van1.setEnabled(False)
    telaAtualizarPessoa.radioButton_van2.setEnabled(False)

def verificarAlunoMOD():
    try:
        resetVerificarAluno()
        codigoAluno = telaAtualizarPessoa.lineEdit_codigo.text()
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute(f'SELECT * FROM alunos WHERE codigo = {codigoAluno}')
        aluno = cursor.fetchall()
        banco.close()
        telaAtualizarPessoa.label_aviso.setText('')
        if aluno[0][0] != '':

            telaAtualizarPessoa.lineEdit_nome.setText(f'{aluno[0][1]}')
            telaAtualizarPessoa.lineEdit_nome.setEnabled(True)

            telaAtualizarPessoa.lineEdit_nomePai.setText(f'{aluno[0][2]}')
            telaAtualizarPessoa.lineEdit_nomePai.setEnabled(True)

            telaAtualizarPessoa.lineEdit_nomeMae.setText(f'{aluno[0][3]}')
            telaAtualizarPessoa.lineEdit_nomeMae.setEnabled(True)

            telaAtualizarPessoa.lineEdit_telefone.setText(f'{aluno[0][4]}')
            telaAtualizarPessoa.lineEdit_telefone.setEnabled(True)

            telaAtualizarPessoa.lineEdit_endereco.setText(f'{aluno[0][5]}')
            telaAtualizarPessoa.lineEdit_endereco.setEnabled(True)

            telaAtualizarPessoa.lineEdit_escola.setText(f'{aluno[0][6]}')
            telaAtualizarPessoa.lineEdit_escola.setEnabled(True)

            telaAtualizarPessoa.lineEdit_mensalidade.setText(f'{aluno[0][7]}')
            telaAtualizarPessoa.lineEdit_mensalidade.setEnabled(True)

            telaAtualizarPessoa.radioButton_manha.setEnabled(True)
            telaAtualizarPessoa.radioButton_tarde.setEnabled(True)
            telaAtualizarPessoa.radioButton_noite.setEnabled(True)
            telaAtualizarPessoa.radioButton_van1.setEnabled(True)
            telaAtualizarPessoa.radioButton_van2.setEnabled(True)

            telaAtualizarPessoa.pushButton_editar.setEnabled(True)

            telaAtualizarPessoa.label_aviso.setText(f'Os dados TURNO e VAN\nprecisam ser inseridos novamente\na cada modificação.')

    except Exception as erro:
        telaAtualizarPessoa.label_aviso.setText(f'Erro: {erro}')

def removerAluno():
    try:
        codigoAluno = telaRemoverPessoa.lineEdit_codigo.text()
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute(f'DELETE FROM alunos WHERE codigo = {codigoAluno}')
        banco.commit()
        banco.close()
        atualizarTabela()
        sairRemocao()
    except:
        telaAtualizarPessoa.label_aviso.setText('Erro ao editar aluno.')

def ModificarAluno():
    codigoAluno = telaAtualizarPessoa.lineEdit_codigo.text()
    turno = ''
    van = ''
    try:    
        nome = telaAtualizarPessoa.lineEdit_nome.text()
        nomePai = telaAtualizarPessoa.lineEdit_nomePai.text()
        nomeMae = telaAtualizarPessoa.lineEdit_nomeMae.text()
        telefone = telaAtualizarPessoa.lineEdit_telefone.text()
        endereco = telaAtualizarPessoa.lineEdit_endereco.text()
        escola = telaAtualizarPessoa.lineEdit_escola.text()
        mensalidade = int(telaAtualizarPessoa.lineEdit_mensalidade.text())
    except ValueError as erro:
        telaAtualizarPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex(250).{erro}')

    #Molda a variável turno
    if telaAtualizarPessoa.radioButton_manha.isChecked() == True:
        turno = turno+' Manhã.'
    if telaAtualizarPessoa.radioButton_tarde.isChecked() == True:
        turno = turno+' Tarde. '
    if telaAtualizarPessoa.radioButton_noite.isChecked() == True:
        turno = turno+' Noite.'

    #Molda a variável van
    if telaAtualizarPessoa.radioButton_van1.isChecked() == True:
        van = 'Van 1'
    if telaAtualizarPessoa.radioButton_van2.isChecked() == True:
        van = 'Van 2'

    try:
        if nome != '' and (nomePai != '' or nomeMae != '') and telefone != '' and endereco != '' and escola != '' and mensalidade:
            try:
                banco = sqlite3.connect('banco_alunos.db')
                cursor = banco.cursor()
                
                cursor.execute(f"UPDATE alunos SET nome = '{nome}', nome_do_pai = '{nomePai}', nome_da_mae = '{nomeMae}', telefone = '{telefone}', endereco = '{endereco}', escola = '{escola}', mensalidade = {mensalidade}, turno = '{turno}', van = '{van}' WHERE codigo = {codigoAluno}")
                
                banco.commit()
                banco.close

                atualizarTabela()
                telaAtualizarPessoa.label_aviso.setText(f'Dados de {nome} atualizados!')

            except Exception as erro:
                telaAtualizarPessoa.label_aviso.setText(f'Erro ao cadastrar o aluno.\n{erro}')

        else:
            telaAtualizarPessoa.label_aviso.setText('Problema ao inserir aluno, verifique se\n todos os campos foram preenchidos.')
    except:
            telaAtualizarPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex: (100).')

def sairRegistro():
    telaRegistro.close()
    telaLogin.show()
    telaRegistro.lineEdit_nome.setText('')
    telaRegistro.lineEdit_loginCadastro.setText('')
    telaRegistro.lineEdit_senhaCadastro.setText('')
    telaRegistro.lineEdit_senhaConfirma.setText('')
    telaRegistro.label_aviso.setText('')


def sairInsercao():
    telaInserirPessoa.close()
    telaPrincipal.show()
    telaInserirPessoa.lineEdit_nome.setText('')
    telaInserirPessoa.lineEdit_nomePai.setText('')
    telaInserirPessoa.lineEdit_nomeMae.setText('')
    telaInserirPessoa.lineEdit_telefone.setText('')
    telaInserirPessoa.lineEdit_endereco.setText('')
    telaInserirPessoa.lineEdit_escola.setText('')
    telaInserirPessoa.lineEdit_mensalidade.setText('')
    telaInserirPessoa.label_aviso.setText('')
    telaInserirPessoa.radioButton_manha.setChecked(False)
    telaInserirPessoa.radioButton_tarde.setChecked(False)
    telaInserirPessoa.radioButton_noite.setChecked(False)
    telaInserirPessoa.radioButton_van1.setChecked(False)
    telaInserirPessoa.radioButton_van2.setChecked(False)

def sairRemocao():
    telaRemoverPessoa.close()
    telaPrincipal.show()
    telaRemoverPessoa.lineEdit_codigo.setText('')
    telaRemoverPessoa.label_aviso.setText('')
    telaRemoverPessoa.pushButton_remover.setEnabled(False)

def sairAtualizacao():
    telaAtualizarPessoa.close()
    telaPrincipal.show()
    resetVerificarAluno()
    telaAtualizarPessoa.lineEdit_codigo.setText('')

def atualizarTabela():
    try:
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM alunos")
        dadosTabela = cursor.fetchall()
        telaPrincipal.tableWidget_1.setRowCount(len(dadosTabela))
        telaPrincipal.tableWidget_1.setColumnCount(10)

        for i in range(0, len(dadosTabela)):
            for j in range(0,10):
                telaPrincipal.tableWidget_1.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosTabela[i][j])))
        
        banco.close()

    except:
        return


app = QtWidgets.QApplication([])

#ATRIBUIÇÃO DE INTERFACES
telaLogin = uic.loadUi('LoginWindow.ui')
telaRegistro = uic.loadUi('RegisterWindow.ui')
telaPrincipal = uic.loadUi('MainWindow.ui')
telaInserirPessoa = uic.loadUi('InsertPerson.ui')
telaRemoverPessoa = uic.loadUi('RemovePerson.ui')
telaAtualizarPessoa = uic.loadUi('UpdatePerson.ui')

#TELA DE LOGIN
telaLogin.pushButton_login.clicked.connect(login)
telaLogin.pushButton_cadastre.clicked.connect(chamaTelaRegistro)

#TELA DE REGISTRO DE USUARIO
telaRegistro.pushButton_cadastrar.clicked.connect(cadastrar)
telaRegistro.pushButton_cancelar.clicked.connect(sairRegistro)

#TELA DO SISTEMA
telaPrincipal.pushButton_logout.clicked.connect(logout)
telaPrincipal.pushButton_inserir.clicked.connect(chamaTelaInserirPessoa)
telaPrincipal.pushButton_remover.clicked.connect(chamaTelaRemoverPessoa)
telaPrincipal.pushButton_modificar.clicked.connect(chamaTelaAtualizarPessoa)

#TELA DE INSERÇÃO DE ALUNO
telaInserirPessoa.pushButton_cancelar.clicked.connect(sairInsercao)
telaInserirPessoa.pushButton_cadastrar.clicked.connect(inserirAluno)

#TELA DE REMOÇÃO DE ALUNO
telaRemoverPessoa.pushButton_cancelar.clicked.connect(sairRemocao)
telaRemoverPessoa.pushButton_verificar.clicked.connect(verificarAluno)
telaRemoverPessoa.pushButton_remover.clicked.connect(removerAluno)

#TELA DE MODIFICAÇÃO DE ALUNO
telaAtualizarPessoa.pushButton_verificar.clicked.connect(verificarAlunoMOD)
telaAtualizarPessoa.pushButton_editar.clicked.connect(ModificarAluno)
telaAtualizarPessoa.pushButton_cancelar.clicked.connect(sairAtualizacao)

telaLogin.show()
app.exec()