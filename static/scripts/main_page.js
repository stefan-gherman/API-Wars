const getData = async () => {
    let planetPeopleData = [];
    let planetData = [];
    let peopleData = [];
    if (sessionStorage.getItem('planetsData') === null && sessionStorage.getItem('peoplesData') === null) {
        try {
            let response = await fetch('https://swapi.co/api/planets/')
            let payload = await response.json();
            let numberOfPlanets = parseInt(payload.count);
            response = await fetch('https://swapi.co/api/people/')
            payload = await response.json();
            let numberOfPeople = parseInt(payload.count);
            sessionStorage.numberOfPlanets = numberOfPlanets;
            sessionStorage.numberOfPeople = numberOfPeople;
            console.log(numberOfPlanets);
            for (let i = 1; i <= numberOfPlanets; i++) {
                const new_response = await fetch('https://swapi.co/api/planets/' + i.toString() + '/', {mode: 'cors'});
                const payload = await new_response.json()
                planetPeopleData.push(payload);
            }
            for (let i = 1; i <= numberOfPeople; i++) {
                const new_response = await fetch('https://swapi.co/api/people/' + i.toString() + '/', {mode: 'cors'});
                const payload = await new_response.json()
                planetPeopleData.push(payload);
            }
            planetData = planetPeopleData.slice(0, numberOfPlanets);
            peopleData = planetPeopleData.slice(numberOfPlanets);
            sessionStorage.setItem('planetsData', JSON.stringify(planetData));
            sessionStorage.setItem('peoplesData', JSON.stringify(peopleData));
            console.log('Done');
            return ([planetData, peopleData]);
        } catch (error) {
            console.log('Something went rogue');
        }
    } else {
        planetData = JSON.parse(sessionStorage.getItem('planetsData'));
        peopleData = JSON.parse(sessionStorage.getItem('peoplesData'));
        console.log('Loaded from sessionStorage');
        return ([planetData, peopleData]);

    }

};

main = async () => {
    const text = document.getElementById('main')
    const buttons = document.getElementById('buttons');
    buttons.setAttribute('hidden', '');
    text.innerHTML = `<i class="fab fa-empire fa-2x fa-spin"></i> Please Wait while your data is loading... <i class="fab fa-empire fa-2x fa-spin"></i>`;
    let dataFromAPI = await getData();
    let planetData = dataFromAPI[0];
    let peopleData = dataFromAPI[1];
    buttons.removeAttribute('hidden');
    const planetsTable = document.createElement('table');
    planetsTable.setAttribute('class', 'table table-sm table-bordered justify-content-center mt-3')
    const planetsTableHeader = document.createElement('thead');
    let vals = ['Name', 'Diameter', 'Terrain', 'Surface Water Percentage', 'Population', 'Residents'];
    for (let val of vals) {
        const newHeader = document.createElement('th');
        newHeader.innerText = val;
        planetsTableHeader.appendChild(newHeader);
    }

    const planetsTableBody = document.createElement('tbody');

    for (let i = 0; i < planetData.length; i++) {
        const newRow = document.createElement('tr');
        let newCell = document.createElement('td');

        newCell.innerHTML = planetData[i]['name'];
        newRow.appendChild(newCell);

        newCell = document.createElement('td');
        if (planetData[i]['diameter'] != 'unknown') {
            newCell.innerHTML = planetData[i]['diameter'] + ' km';

        } else {
            newCell.innerText = planetData[i]['diameter'];
        }
        newRow.appendChild(newCell);

        newCell = document.createElement('td');
        newCell.innerText = planetData[i]['terrain'];
        newRow.appendChild(newCell);

        newCell = document.createElement('td');
        if (planetData[i]['surface_water'] != 'unknown') {
            newCell.innerText = planetData[i]['surface_water'] + '%';
        } else {
            newCell.innerText = planetData[i]['surface_water'];
        }
        newRow.appendChild(newCell);

        newCell = document.createElement('td');
        if (planetData[i]['population'] != 'unknown') {

            newCell.innerText = planetData[i]['population'] + ' people';
        } else {
            newCell.innerText = planetData[i]['population'];
        }
        newRow.appendChild(newCell);

        newCell = document.createElement('td');
        newCell.innerText = planetData[i]['residents'].length + ' resident(s)';
        console.log(newCell.innerText);
        if (newCell.innerText != '0 resident(s)') {
            const buttonRes = document.createElement('button');

            buttonRes.setAttribute('class', 'btn btn-info my-2');
            buttonRes.innerText = newCell.innerText;
            newCell.innerText = '';
            newCell.appendChild(buttonRes)
            newRow.appendChild(newCell);
        } else {
            newCell = document.createElement('td');
            newCell.innerText = 'No known residents';
            newRow.appendChild(newCell);
        }
        planetsTableBody.appendChild(newRow);
    }

    planetsTable.appendChild(planetsTableHeader);
    planetsTable.appendChild(planetsTableBody);
    text.innerText = '';
    text.appendChild(planetsTable);


};

main();

