  <!-- Sistema para automatizar preenchimento -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Automação</title>
        <link rel="stylesheet" href="./css/estilo.css">
        <!-- Adicionar logo ao título-->
        <link rel="shortcut icon" type="image/x-icon" href="./img/logo.png">
    </head>
    <body>
        <!-- Criar a div principal -->
        <div class="usuario">
            <!-- Criar a área para o formulário -->
            <div class="form">
                <!-- Criar formulário -->
                <form> 
                    <!-- Criar input para Nome do usuário -->
                    <input type="text" name = "usuario" placeholder="Digite seu nome completo" required>
                    
                    <!-- Criar input para o Telefone do usuário --> 
                    <input type="text" name = "telefone" placeholder="(00) 00000-0000" required>
                    
                    <!-- Criar input para a senha do usuário -->
                    <input type="password" name = "senha" placeholder="Digite sua senha" required>
                    
                    <button>Salvar</button>
                </form>
            </div>
        </div>
    </body>
    </html>