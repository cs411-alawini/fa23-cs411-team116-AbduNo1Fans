let availablePremis = [
    'Southwest',
    'Central',
    '77th Street',
    'N Hollywood',
    'Mission',
    'Southeast',
    'Devonshire',
    'Harbor',
    'West Valley',
    'West LA',
    'Pacific',
    'Wilshire',
    'Hollywood',
    'Northeast',
    'Hollenbeck',
    'Olympic',
    'Newton',
    'Topanga',
    'Van Nuys',
    'Foothill',
    'Rampart',
];

const premisvalid_results = document.querySelector(".premisvalid_results");
const premiscode_input = document.getElementById("premiscode_input");

premiscode_input.onkeyup = function(){
    let result = []; 
    let input = premiscode_input.value; //filter
    if(input.length){
        result = availablePremis.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    displayPremis(result);
    if(!result.length){
        premisvalid_results.innerHTML = '';
    }
}

function displayPremis(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInputPremis(this)>" + list + "</li>";
    });
    premisvalid_results.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInputPremis(list){
    premiscode_input.value = list.innerHTML;
    premisvalid_results.innerHTML = '';
}