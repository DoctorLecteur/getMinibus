function doShowStops(objAnswer) {

    if (objAnswer['httpcode'] === 200) {

        alert('Остановки - ' + objAnswer['stops']);
        document.getElementById("RouteId").value = "";

    } else {
        alert("Неудачный запрос на сервер");
    }

}

function getStops() {

    const nRouteId = document.getElementById("RouteId").value;

    if (nRouteId) {

        const answer = doHttpRequest(nRouteId);
        answer.then(
            result => doShowStops(result)
        );

    } else {
        alert("Введите номер маршрута");
    }

}

async function doHttpRequest(nRouteId) {

    const route = {
        routeId: nRouteId
    }

    const URL = 'http://127.0.0.1:5000/stops';

    const response = await fetch(URL, {
        method: 'POST',
        headers: {
            'Access-Control-Request-Method': 'POST',
            'Content-type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(route)
    });

    const result = await response.json();

    return result;
}