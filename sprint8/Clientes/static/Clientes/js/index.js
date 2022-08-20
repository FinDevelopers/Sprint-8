const d = document;
//Contenedor donde van a estar las cards de los diferentes dólares
const dolar = d.getElementById('dolar');
//Arreglo que contiene Los nombres de los dólares que se van a mostrar
//Los nombres salen de la propiedad 'nombre' de los distintos objetos 'casa' (ver link de la función fetch)
//Para agregar o eliminar alguno, basta con sacar o agregar su nombre al array
const dolaresAUsar = ['Dolar Oficial', 'Dolar Blue', 'Dolar Contado con Liqui', 'Dolar Bolsa','Dolar turista'];

//Función que actualiza el contenedor que tiene la información de los dólares
function updateDolarContainer(){
    
    //Limpia contenedor
    dolar.innerHTML = '';

    //Trae el array de la API 
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(res => res.json()) 
    .then(datos => {
        //La variable 'datos' es el array de objetos
        //Cada objeto tiene adentro otro objeto cuyo nombre es 'casa'
        //Cada objeto 'casa' es el que tiene la información de cada tipo de dólar (ej. casa.nombre, casa.venta)

        let datosFiltrados = [];
        //Filtra array de datos para descartar los objetos 'casa' cuyo 'nombre' no está en el array de dolaresAUsar
        datosFiltrados = datos.filter(dato => dolaresAUsar.indexOf(dato.casa.nombre) !== -1);
        for(let dato of datosFiltrados){
            //Cada 'dato' sería el objeto que adentro tiene al objeto 'casa'

            // Concatena la string que devuelve createDolarCardHTML() al innerHTML del contenedor
            dolar.innerHTML += createDolarCardHTML(dato);
        }  
    })
}

//Crea una string que tiene el código HTML de las cards 
//Importante: hay algunos dólares que no cotizan la compra, en ese caso no se muestra y la venta pasa a tener col-12 (en vez de col-6)
function createDolarCardHTML(dato){
    // Asignando un ícono (y su color) dependiendo del valor de la variación
    let variacionIcon;
    let variacion = normalizeNumber(dato.casa.variacion);
    if(variacion > 0){
     variacionIcon = "bi bi-arrow-up text-success";
    }else if(variacion < 0){
        variacionIcon = "bi bi-arrow-down text-danger";
    }else{
        variacionIcon = "bi bi bi-pause text-primary rotado90";
    };
    

    // Primera parte invariable de las cards
    let result = ` 
    <div class="card text-center text-dark m-3">
        <div class="card-body">
        <h2 class="card-title ">${dato.casa.nombre}</h2>
            <div class="row">`;
    
    // Parte variable de las cards
    // Varía según si cotiza la compra
    if(dato.casa.compra !== "No Cotiza"){
        result += `
        <div class="col-6">
            <p class="card-text">Compra <b>$${dato.casa.compra}</b></p>
        </div>
        <div class="col-6">
            <p class="card-text">Venta <b>$${dato.casa.venta}</b></p>
        </div>`
    }
    else{
        result += `
        <div class="col-12">
            <p class="card-text">Venta<br><b>$${dato.casa.venta}</b></p>
        </div> `
    }

    // Última parte invariable de las cards
    result += `
    <div class="col-12">
            <p class="card-text d-flex align-items-center justify-content-center mt-3">
                <span>${formatNumber(variacion)}</span>
                <i class="${variacionIcon}"></i>
            </p>
        </div>
            </div>
        </div>
    </div>`
    
    return result;
    
}

//Transforma las strings de los números que vienen con coma para que tengan punto, y los transforma en number
//ej. '4,21' -> '4.21' -> 4.21 
function normalizeNumber(num){
    return Number(num.replace(',','.'))
}

//Transforma una variable de tipo number a una de tipo string, y remplaza el '.' decimal con una coma ','
//ej. 4.21 -> '4.21' -> '4,21' 
function formatNumber(num){
    return String(num).replace('.',',');
}

//Dada una cantidad de minutos devuelve cuantos milisegundos hay en esa cantidad de minutos
function minutosAMilsegundos(mins){
    return mins * 60000; 
}

//Actualiza el contenedor cuando carga la página y despues cada 10 minutos
updateDolarContainer();
var intervalID = window.setInterval(updateDolarContainer,minutosAMilsegundos(10));
 


//Ocultar Saldo
let eye = d.getElementById('eye')
eye.addEventListener('click', clickOnEye);
function clickOnEye(){
    h2_elements = document.querySelectorAll('#balance-container h2')
    if (eye.className == 'bi bi-eye'){
        eye.className = 'bi bi-eye-slash';
        h2_elements[0].className = 'd-none';
        h2_elements[1].className = '';
    }else {
        eye.className = 'bi bi-eye';
        h2_elements[0].className = '';
        h2_elements[1].className = 'd-none';
    }
}