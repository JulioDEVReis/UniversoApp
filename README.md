Aplicativo Mobile, para Android, desenvolvido em Kivy e KivyMD, com correlacionamento a um banco de dados criado, com frases em Português.
Esse aplicativo foi desenvolvido em resposta a uma demanda para um aplicativo mobile que apresentasse frases aleatórias para motivação e elevação de moral e astral. Veja meu outro repositório chamado App Frases em Português para ver como contornei o problema de somente encontrar frases em inglês na API Forismatic.
O aplicativo possui 3 telas, sendo a HomeScreen desenvolvida para o usuário ver uma mensagem aleatória e ter um campo para digitar um desejo para envio ao Universo.
![Captura de tela 2023-12-26 120453](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/f326a5be-3b74-4100-b96a-0ceee89f09ed)
A segunda tela possui 3 frases, também aleatórias, com um botão para renovar as frases, e assim motivar e aumentar o astral do usuário com várias frases de efeito.
![Captura de tela 2023-12-26 120506](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/57b9dab5-c49f-42bb-9973-59accfe14a68)

![Captura de tela 2023-12-26 120518](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/b70e3f9a-c45a-4bf3-ab2a-e5228dbf1809)

A terceira tela somente é aberta quando o usuário digita seu desejo na primeira tela e clica no botão para enviar. O campo para envio do desejo está na parte inferior da janela principal, como vemos na imagem abaixo. Assim que o usuário solta o botão de envio, a terceira janela é então renderizada com o desejo enviado ao Universo.
![Captura de tela 2023-12-26 120610](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/1d680592-3ac9-4413-b64e-2d9863e4c0a4)
![Captura de tela 2023-12-26 120617](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/643092b2-fd73-48ac-957f-f75faa827c5b)

# O desenvolvimento:
Para a criação e gerenciamento das janelas, usei MDScreenManager, do KivyMD, sendo passado como classe principal à classe UniversoApp.
Em seguida criei as classes correspondente a cada tela, passando a classe MDScreen a cada uma das classes.
Criei em seguida meu arquivo Kivy, com linguagem Kivy, para incluir todos os layouts e widgets de cada tela.
Como meu Aplicativo possui relacionamento com um banco de dados, criei um arquivo Python separadamente, com todas as funções para acesso, seleção e manipulação dos dados. O banco de dados contém as frases que usaremos no próprio aplicativo, na primeira e segunda telas.
Ao final, o aplicativo foi entregue a cliente em formato APK, empacotado via BUILDOZER.


