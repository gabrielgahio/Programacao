$(function() { // quando o documento estiver pronto/carregado
    
    // função para exibir pessoas na tabela
    function exibir_esportes() {
        mostrar_conteudo("tabelaEsportes");
        $.ajax({
            url: 'http://localhost:5000/listar_modalidades',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
            alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (esportes) {
            // Limpa a tabela
            $('#corpoTabelaEsportes').empty();

            console.log(esportes);

            // Percorre a lista
            for (esp of esportes) { //i vale a posição no vetor
                lin = '<tr id="linha_'+esp.id+'">' + 
                '<td>' + esp.id + '</td>' + 
                '<td>' + esp.nome + '</td>' + 
                '<td>' + esp.modalidade + '</td>' +
                '<td>' + esp.pais_favorito + '</td>' +
                '<td>' + esp.atleta + '</td>' +
                '<td>' + esp.nivel_de_dificuldade + '</td>' +
                '<td><a href=# id="excluir_' + esp.id + '" ' + 
                  'class="excluir_modalidades"><img src="../img/excluir.png" '+
                  'alt="Excluir Modalidades" title="Excluir Modalidades"></a>' + 
                '</td>' + 
                '</tr>';

                console.log(lin);
                // adiciona a linha no corpo da tabela
                console.log(esp.nome,esp.atleta);
                $('#corpoTabelaEsportes').append(lin);
            }
            
        }
    }
    
    function mostrar_conteudo(identificador) {
        $("#tabelaEsportes").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');
    }

    $(document).on("click", "#linkListarModalidades", function(e) {
        e.preventDefault();
        exibir_esportes();
        //Isso ta mec, ele só ta chamando a função
        //n sei pq krlos ele apaga o console
        //nunca vi isso
        
    });

    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirModalidade", function(e) {
        //pegar dados da tela
        e.preventDefault();
        id = $("#campoId").val();
        nome = $("#campoNome").val();
        modalidade = $("#campoModalidade").val();
        pais_favorito = $("#campoPais_favorito").val();
        atleta = $("#campoAtleta").val();
        nivel_de_dificuldade = $("#campoNivel_de_dificuldade").val();

        // preparar dados no formato json
        var dados = JSON.stringify({ id: id, nome: nome, modalidade: modalidade, pais_favorito: pais_favorito, atleta: atleta, nivel_de_dificuldade: nivel_de_dificuldade });
        // fazer requisição para o back-end
        console.log(dados);
        
        $.ajax({
            url: 'http://localhost:5000/incluir_modalidades',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: modaldiadeIncluida, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });

        function modaldiadeIncluida (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Modalidade incluída com sucesso!");
                // limpar os campos
                $("#campoId").val("");
                $("#campoNome").val("");
                $("#campoModalidade").val("");
                $("#campoPais_favorito").val("");
                $("#campoAtleta").val("");
                $("#campoNivel_de_dificuldade").val("");

            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
    

    $('#modalIncluirModalidade').on('hide.bs.modal', function (e) {
        // se a página de listagem não estiver invisível
        if (! $("#tabelaEsportes").hasClass('invisible')) {
            // atualizar a página de listagem
            exibir_esportes();
            
        }
    });

    // a função abaixo é executada quando a página abre
    mostrar_conteudo("conteudoInicial");

    $(document).on("click", ".excluir_modalidades", function() {
        var componente_clicado = $(this).attr('id');
        var nome_icone = "excluir_";
        var id_modalidades = componente_clicado.substring(nome_icone.length);
        $.ajax({
            url: 'http://localhost:5000/excluir_modalidades/'+id_modalidades,
            type: 'DELETE',
            dataType: 'json',
            success: modalidadesExcluida,
            error: erroAoExcluir
        });
        function modalidadesExcluida (retorno) {
            if (retorno.resultado == "ok") { 
                $("#linha_" + id_modalidades).fadeOut(1000, function(){   
                    alert("Modalidade removida com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoExcluir (retorno) {
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });  
    
    function exibir_campeonatos_realizados() {
        $.ajax({
            url: 'http://localhost:5000/listar_campeonatos_realizados',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar, // chama a função listar para processar o resultado
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });
        function listar (campeonatos_realizados) {
            $('#corpoTabelaCampeonatosRealizados').empty();
            mostrar_conteudo("cadastroCampeonatosRealizados");

            for (var i in campeonatos_realizados) {
                lin = '<tr id="linha_campeonato_realizado_'+exames_realizados[i].id+'">' + 
                '<td>' + campeonatos_realizados[i].data + '</td>' + 
                '<td>' + campeonatos_realizados[i].ganhador + '</td>' + 

                '<td>' + campeonatos_realizados[i].esporte.nome + '</td>' + 
                '<td>' + campeonatos_realizados[i].esporte.modalidade + '</td>' + 
                '<td>' + campeonatos_realizados[i].esporte.pais_favorito + '</td>' + 
                '<td>' + campeonatos_realizados[i].esporte.atleta + '</td>' + 
                '<td>' + campeonatos_realizados[i].esporte.nivel_de_dificuldade + '</td>' + 

                '<td><a href=# id="excluir_campeonato_realizado_' + campeonatos_realizados[i].id + '" ' + 
                    'class="excluir_campeonatos_realizado"><img src="img/excluir.png" '+
                    'alt="Excluir Campeonato realizado" title="Excluir Campeonato realizado"></a>' + 
                '</td>' + 
                '</tr>';
                $('#corpoTabelaCampeonatosRealizados').append(lin);


            }
        }
    }

    $(document).on("click", "#linkListarCampeonatosRealizados", function() {
        exibir_campeonatos_realizados();
    });

});


