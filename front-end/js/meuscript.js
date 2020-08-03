$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_modalidades',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (esporte) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in modalidades) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
              '<td>' + esporte[i].id + '</td>' + 
              '<td>' + esporte[i].nome + '</td>' + 
              '<td>' + esporte[i].modalidade + '</td>' +
              '<td>' + esporte[i].pais_favorito + '</td>' +
              '<td>' + esporte[i].atleta + '</td>' +
              '<td>' + esporte[i].nivel_de_dificuldade + '</td>' +
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaPessoas').append(lin);
        }
    }

});