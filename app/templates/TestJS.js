function getStops() {

    const nRouteId = document.getElementById("RouteId").value;

    if (nRouteId) {

        const answer = doHttpRequest(nRouteId);
        console.log('answer', answer);
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

async function doHttpRequest(nRouteId) {

    const route = {
        routeId: nRouteId
    }

    const URL = 'http://127.0.0.1:5000/stops';

    const response = await fetch(URL, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(route)
    });

    const result = await response.json();
    console.log('result', result['httpcode']);

    return result;
}