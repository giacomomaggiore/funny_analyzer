const analysis_text = document.getElementById("analysis-text")
const analysis_div = document.getElementById("analysis-container")
let index = 0;
let text = "..."
const domain = window.location.origin


function type() {
    if (index < text.length) {
        analysis_text.innerHTML += text.charAt(index);
        index++;
        setTimeout(type, 50); // Regola la velocità di digitazione qui
    }
}


function submitForm() {
    let portfolio_value = document.getElementById("portfolio-value").value;
    let salary = document.getElementById("salary").value;
    let country = document.getElementById("country").value;
    let age = document.getElementById("age").value;
    let job = document.getElementById("job").value;
    
    if (!portfolio_value){
        portfolio_value = "none"
    }
    if (!salary){
        salary = "none"
    }
    if (!country){
        country = "none"
    }
    if (!age){
        age = "none"
    }
    if (!job){
        job = "none"
    }


    let asset_1 = document.getElementById("asset-1").value; 
    let asset_2 = document.getElementById("asset-2").value;
    let asset_3 = document.getElementById("asset-3").value;
    let asset_4 = document.getElementById("asset-4").value;
    let asset_5 = document.getElementById("asset-5").value;
    
    let percentage_1 = Number(document.getElementById("percentage-1").value);
    let percentage_2 = Number(document.getElementById("percentage-2").value);
    let percentage_3 = Number(document.getElementById("percentage-3").value);
    let percentage_4 = Number(document.getElementById("percentage-4").value);
    let percentage_5 = Number(document.getElementById("percentage-5").value);

    console.log(percentage_1, percentage_2, percentage_3, percentage_4)

    let status = 0
    if (asset_1 == asset_2 || asset_1 == asset_3 || asset_1 == asset_4 || asset_1 == asset_5 
        || asset_2 == asset_3 || asset_2 == asset_4 || asset_2 == asset_5 ||
        asset_3 == asset_4 || asset_3 == asset_5 || asset_4 == asset_5){
            status = 0
        }

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
    if (asset_5 && percentage_5){
        status += 1
    }
    else{
        asset_5="none"
        percentage_4=0
    }
    
    if ((asset_1 == asset_2 || asset_1 == asset_3 || asset_1 == asset_4 || asset_1 == asset_5 
        || asset_2 == asset_3 || asset_2 == asset_4 || asset_2 == asset_5 ||
        asset_3 == asset_4 || asset_3 == asset_5 || asset_4 == asset_5)
        && (asset_1 != "none" && asset_2 != "none" && asset_3 != "none" && asset_4 != "none" && asset_5 != "none")
        ){
            status = 0
        }

    if (status < 2){
        alert("Please fill out at least two different asset and two percentages")
        return
    }
    if (percentage_1 + percentage_2 + percentage_3 + percentage_4 > 100){
        alert("Sum of the percentages should be less than 100")
        return
    }

    
    query_parameters = `?asset_1=${asset_1}&percentage_1=${percentage_1}&asset_2=${asset_2}&percentage_2=${percentage_2}&asset_3=${asset_3}&percentage_3=${percentage_3}&asset_4=${asset_4}&percentage_4=${percentage_4}&asset_5=${asset_5}&percentage_5=${percentage_5}&portfolio_value=${portfolio_value}&salary=${salary}&country=${country}&age=${age}&job=${job}`
    url = domain + "/analyze" + query_parameters;

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
            console.log(analysis_div)
            data = data.replace("html", '');
            data = data.replace("```", "")
            analysis_div.insertAdjacentHTML("afterbegin", data)
            //type()

        })
        .catch(error => {
            // Handle any errors that occurred during the fetch request
            console.error(error);
        });
    

}


