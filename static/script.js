const analysis_text = document.getElementById("analysis-text")
let index = 0;
let text = "..."

function type() {
    if (index < text.length) {
        analysis_text.innerHTML += text.charAt(index);
        index++;
        setTimeout(type, 50); // Regola la velocità di digitazione qui
    }
}


function submitForm() {
    let asset_1 = document.getElementById("asset-1").value; 
    let asset_2 = document.getElementById("asset-2").value;
    let asset_3 = document.getElementById("asset-3").value;
    let asset_4 = document.getElementById("asset-4").value;
    
    let percentage_1 = document.getElementById("percentage-1").value;
    let percentage_2 = document.getElementById("percentage-2").value;
    let percentage_3 = document.getElementById("percentage-3").value;
    let percentage_4 = document.getElementById("percentage-4").value;

    let status = 0
    if (asset_1 && percentage_1){
        status += 1
    }
    else{
        asset_1="none"
        percentage_1=0
    }
    if (asset_2 && percentage_2){
        status += 1
    }
    else{
        asset_2="none"
        percentage_2=0
    }
    if (asset_3 && percentage_3){
        status += 1
    }
    else{
        asset_3="none"
        percentage_3=0
    }
    if (asset_4 && percentage_4){
        status += 1
    }
    else{
        asset_4="none"
        percentage_4=0
    }
    if (status < 2){
        alert("Please fill out at least two asset and two percentages")
        return
    }

    base_url = "http://localhost:8000/analyze?"
    query_parameters = `asset_1=${asset_1}&percentage_1=${percentage_1}&asset_2=${asset_2}&percentage_2=${percentage_2}&asset_3=${asset_3}&percentage_3=${percentage_3}&asset_4=${asset_4}&percentage_4=${percentage_4}`
    url = base_url + query_parameters;

    console.log(url)
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            
            // Process the fetched data here
            console.log(data);

            console.log(typeof(data))
            text = data;
            console.log(text)
            index = 0;
            type()

        })
        .catch(error => {
            // Handle any errors that occurred during the fetch request
            console.error(error);
        });
    

}


