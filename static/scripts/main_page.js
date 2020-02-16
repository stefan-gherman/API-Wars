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
            planetData = planetPeopleData.slice(0,numberOfPlanets);
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
    text.innerHTML = 'Something';
    let dataFromAPI = await getData();
    let planetData = dataFromAPI[0];
    let peopleData = dataFromAPI[1];
    text.innerHTML = 'Loaded';
    console.log(dataFromAPI);
    console.log(planetData);
    console.log(peopleData);
};

main();

