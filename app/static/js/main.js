function atualizarRelogio(){

    const agora = new Date();

    document.getElementById("relogio").innerHTML =
        agora.toLocaleString("pt-BR");

}

setInterval(atualizarRelogio,1000);

atualizarRelogio();
