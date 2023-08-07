
function send(type,subtype,name,saldo) {
    console.log("send") 
    const url = "http://localhost:8000/catalogo/newActivo";

    const data = {
        type: type,
        subtype: subtype,
        name: name,
        saldo: saldo,
    };

    console.log(data)

    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    };

    console.log(request);
```
    fetch(url, request).then(
        response => response.json())
    .then(
        data => {
            console.log(data);

        }
    ); 
```    
}



document.addEventListener('DOMContentLoaded', function () {
    const type = document.querySelector('#type')
    const subtype = document.querySelector('#subtype')
    const name = document.querySelector('#name')
    const saldo = document.querySelector('#saldo')
    
    document.querySelector('#create-new-activo').onsubmit = () => {
        createActivo(type.value,subtype.value,name.value,saldo.value)
        return false;
    }
})
