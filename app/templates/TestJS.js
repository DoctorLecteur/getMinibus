function getStops() {

    const nRouteId = document.getElementById("RouteId").value;

    if (nRouteId) {

        const answer = doHttpRequest(nRouteId);

        if (answer['httpcode'] === 200) {

            alert(answer['stops']);
            document.getElementById("RouteId").value = "";

        } else {
            alert("Неудачный запрос на сервер");
        }

    } else {
        alert("Введите номер маршрута");
    }

}

function doHttpRequest(nRouteId) {

    let xmlHttpRequest = function() {
        return new Promise(function(resolve, reject) {

            const request = new XMLHttpRequest();
            const URL = 'http://127.0.0.1:5000/stops';

            const formData = new FormData();
            formData.append("routeId", nRouteId);

            request.open("POST", URL, true);
            let text='empty';

            request.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    text = this.responseText;
                    resolve(text);
                } else {
                    reject(new Error('Error')); // Обработка ошибки
                }
            };

            request.send(formData);

        });
    };

    xmlHttpRequest()
    .then(function(text){
        console.log(text);
    }).catch(function(err){
        console.error(err);
    });

}